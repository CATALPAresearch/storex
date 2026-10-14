"""
Bridge between the blocking exam conversation and HTTP requests.

An ExamManager talks through two methods, speak() and get_answer(). A Channel
implements both: utterances are appended to an event log that the browser polls,
and an answer arrives from an HTTP request through a queue. The exam itself runs
unchanged in a background thread, see web/runner.py.
"""
import logging
import os
import queue
import threading
import time
import uuid

from oral_exam.exam import ANSWER_TIMEOUT, ExamAborted

logger = logging.getLogger(__name__)

# How long a single long-poll waits before answering with an empty event list.
# Must stay below the gunicorn request timeout.
POLL_TIMEOUT = float(os.getenv("POLL_TIMEOUT", "25"))
# How many answer timeouts in a row end the exam, so that a closed tab does not
# hold a session slot for the whole exam duration.
MAX_ANSWER_TIMEOUTS = int(os.getenv("MAX_ANSWER_TIMEOUTS", "3"))
# A session nobody polls any more is dropped after this long.
SESSION_IDLE_TIMEOUT = float(os.getenv("SESSION_IDLE_TIMEOUT", "600"))
# A finished session is kept this long so the page can still fetch its last
# events and the transcript. It does not occupy an exam slot in the meantime.
FINISHED_GRACE = float(os.getenv("FINISHED_GRACE", "60"))
MAX_SESSIONS = int(os.getenv("MAX_SESSIONS", "2"))


class SessionsBusy(Exception):
    """Raised when all exam slots are taken."""


class Channel:
    """
    Carries examiner utterances out to the browser and student answers back in.

    The outbound side is an append-only log rather than a queue: the exam thread
    also has to report that it finished or failed, and a retried long-poll or a
    page reload must not lose an utterance.
    """
    def __init__(self, answer_timeout=ANSWER_TIMEOUT, max_timeouts=MAX_ANSWER_TIMEOUTS):
        self.events = []
        self.state = "starting"
        self.closed = False
        self.closed_at = None
        self.answer_timeout = answer_timeout
        self.max_timeouts = max_timeouts
        self.consecutive_timeouts = 0
        self.last_poll = time.time()

        self._condition = threading.Condition()
        self._inbox = queue.Queue(maxsize=1)
        self._aborted = False

    # --- outbound ---------------------------------------------------------
    def emit(self, event_type, text=None, state=None):
        """Appends an event to the log and wakes every waiting poll."""
        with self._condition:
            event = {"seq": len(self.events) + 1, "type": event_type}
            if text is not None:
                event["text"] = text
            self.events.append(event)
            if state:
                self.state = state
            self._condition.notify_all()
        logger.info("[%s] %s", event_type, text if text is not None else "")
        return event

    def say(self, text):
        """ExamManager.speak: the examiner says something."""
        self.emit("say", text, state="speaking")

    def close(self, state="finished"):
        """Marks the exam as over and wakes every waiting poll."""
        with self._condition:
            self.closed = True
            self.closed_at = time.time()
            self.state = state
            self._condition.notify_all()

    def poll(self, since=0, timeout=POLL_TIMEOUT):
        """
        Returns the events after the given sequence number.

        Waits up to timeout seconds for new events, so that an idle browser does
        not have to poll in a tight loop.
        """
        deadline = time.time() + timeout
        with self._condition:
            self.last_poll = time.time()
            while True:
                pending = self.events[since:]
                if pending or self.closed:
                    break
                remaining = deadline - time.time()
                if remaining <= 0:
                    break
                self._condition.wait(remaining)
                self.last_poll = time.time()
            return list(self.events[since:]), self.state, self.closed

    # --- inbound ----------------------------------------------------------
    def listen(self):
        """
        ExamManager.get_answer: waits for the next answer from the browser.

        :return: the transcribed answer, or None if nothing arrived in time. None
            is the signal the exam already uses for silence.
        :raises ExamAborted: if the session was abandoned or cancelled.
        """
        self.emit("listen", state="listening")
        deadline = time.time() + self.answer_timeout

        while True:
            if self._aborted:
                raise ExamAborted("The exam was cancelled.")
            remaining = deadline - time.time()
            if remaining <= 0:
                break
            try:
                # Short waits, so that a cancellation is noticed promptly
                answer, = self._inbox.get(timeout=min(1.0, remaining))
            except queue.Empty:
                continue
            # abort() unblocks this wait by submitting an empty answer, so the
            # flag is checked again before the answer is handed to the exam
            if self._aborted:
                raise ExamAborted("The exam was cancelled.")
            self.consecutive_timeouts = 0
            self.state = "thinking"
            return answer

        self.consecutive_timeouts += 1
        logger.warning("No answer within %s seconds (%s in a row).",
                       self.answer_timeout, self.consecutive_timeouts)
        if self.consecutive_timeouts >= self.max_timeouts:
            raise ExamAborted("No answer was received several times in a row.")
        self.state = "thinking"
        return None

    def submit(self, answer):
        """
        Hands an answer to the waiting exam thread.

        :param answer: the transcribed text, or None for silence.
        :return: True if it was accepted, False if the exam was not listening.
        """
        try:
            self._inbox.put_nowait((answer,))
            return True
        except queue.Full:
            return False

    def abort(self):
        """Asks the exam thread to stop at the next opportunity."""
        self._aborted = True
        self.submit(None)


class ExamSession:
    """One exam, its channel and the thread it runs in."""
    def __init__(self, parameters):
        self.id = uuid.uuid4().hex
        self.parameters = parameters
        self.channel = Channel()
        self.created = time.time()
        self.thread = None
        # Set by the runner once the ExamManager exists, used to report the clock
        self.exam = None
        self.audio_cache = {}

    def start(self):
        from oral_exam.web.runner import run_exam
        self.thread = threading.Thread(target=run_exam, args=(self,),
                                       name=f"exam-{self.id[:8]}", daemon=True)
        self.thread.start()

    def remaining_seconds(self):
        if self.exam is None:
            return None
        return max(0.0, round(self.exam.time_manager.get_remaining_time(), 1))

    def transcript(self):
        """The whole conversation so far, useful for export and screenshots."""
        return [event for event in self.channel.events if event["type"] in ("say", "transcript")]

    def is_active(self):
        """True while the exam is still running and holding a slot."""
        return not self.channel.closed

    def is_idle(self, now=None):
        now = now or time.time()
        return now - self.channel.last_poll > SESSION_IDLE_TIMEOUT

    def is_collectable(self, now=None):
        """True once a finished session has been kept around long enough."""
        if self.channel.closed_at is None:
            return False
        return (now or time.time()) - self.channel.closed_at > FINISHED_GRACE


class SessionRegistry:
    """Keeps the running exams of this process."""
    def __init__(self, max_sessions=MAX_SESSIONS):
        self.max_sessions = max_sessions
        self._sessions = {}
        self._lock = threading.Lock()

    def create(self, parameters):
        self.reap()
        with self._lock:
            # A finished exam keeps its events readable for a while but must not
            # hold a slot, otherwise two failed starts would block the system.
            if self.count() >= self.max_sessions:
                raise SessionsBusy(f"All {self.max_sessions} exam slots are in use.")
            session = ExamSession(parameters)
            self._sessions[session.id] = session
        session.start()
        return session

    def get(self, exam_id):
        return self._sessions.get(exam_id)

    def remove(self, exam_id):
        with self._lock:
            return self._sessions.pop(exam_id, None)

    def count(self):
        """Number of exams that are still running, which is what the limit counts."""
        return sum(1 for session in self._sessions.values() if session.is_active())

    def total(self):
        return len(self._sessions)

    def reap(self):
        """Drops sessions that are finished or that nobody polls any more."""
        now = time.time()
        for exam_id, session in list(self._sessions.items()):
            if not session.is_active():
                if session.is_collectable(now):
                    logger.info("Dropping finished session %s", exam_id)
                    self.remove(exam_id)
            elif session.is_idle(now):
                logger.info("Dropping abandoned session %s", exam_id)
                session.channel.abort()
                self.remove(exam_id)
