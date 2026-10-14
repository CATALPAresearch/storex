"""Deterministic checks of the channel state machine and the time clamp."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import threading  # noqa: E402
import time  # noqa: E402

from oral_exam.exam import ExamAborted, TimeManager  # noqa: E402
from oral_exam.web.session import Channel  # noqa: E402

failures = []


def check(label, condition, detail=""):
    print(f"  [{'ok ' if condition else 'FAIL'}] {label}{(' - ' + str(detail)) if detail else ''}")
    if not condition:
        failures.append(label)


print("1) out-of-turn guard")
channel = Channel()
check("fresh channel is not listening", channel.state == "starting", channel.state)
channel.say("Eine Frage?")
check("state is speaking while talking", channel.state == "speaking", channel.state)
# This is the condition app.py checks before accepting an answer
check("answer would be refused while speaking", channel.state != "listening")

print("2) the queue only holds one answer")
channel2 = Channel()
check("first submit accepted", channel2.submit("erste") is True)
check("second submit refused", channel2.submit("zweite") is False)

print("3) a missing answer becomes silence, then aborts")
channel3 = Channel(answer_timeout=1, max_timeouts=3)
start = time.time()
first = channel3.listen()
check("timeout returns None (silence)", first is None, first)
check("timeout took about one second", 0.9 <= time.time() - start < 3, round(time.time() - start, 2))
check("timeout counted", channel3.consecutive_timeouts == 1, channel3.consecutive_timeouts)
channel3.listen()
try:
    channel3.listen()
    check("third timeout aborts the exam", False, "no exception")
except ExamAborted as error:
    check("third timeout aborts the exam", True, error)

print("4) an answer resets the timeout counter")
channel4 = Channel(answer_timeout=1, max_timeouts=3)
channel4.listen()
threading.Timer(0.2, lambda: channel4.submit("eine Antwort")).start()
answer = channel4.listen()
check("answer received", answer == "eine Antwort", answer)
check("counter reset", channel4.consecutive_timeouts == 0, channel4.consecutive_timeouts)

print("5) cancelling unblocks a waiting exam")
channel5 = Channel(answer_timeout=30)
aborted = []


def waiter():
    try:
        channel5.listen()
    except ExamAborted:
        aborted.append(True)


thread = threading.Thread(target=waiter, daemon=True)
thread.start()
time.sleep(0.3)
channel5.abort()
thread.join(timeout=5)
check("waiting exam was released", not thread.is_alive())
check("it raised ExamAborted", aborted == [True], aborted)

print("6) the event log is replayable")
channel6 = Channel()
channel6.say("eins")
channel6.say("zwei")
events, _, _ = channel6.poll(since=0, timeout=0.1)
check("both utterances in the log", [e["text"] for e in events] == ["eins", "zwei"], events)
again, _, _ = channel6.poll(since=0, timeout=0.1)
check("a repeated poll loses nothing", len(again) == 2, len(again))
rest, _, _ = channel6.poll(since=1, timeout=0.1)
check("since skips what was seen", [e["text"] for e in rest] == ["zwei"], rest)

print("7) one turn cannot eat the whole exam clock")


class FakeTopics:
    """The slice of TopicManager that TimeManager uses."""
    def get_topic(self):
        return 0

    def get_level(self):
        from oral_exam.utils.helpers import Level
        return Level.REMEMBER

    def unit_count(self):
        return 5

    def current_unit(self):
        from courselib.model import Unit
        return Unit(id="ke1", title="Grundkonzepte", questions=((), (), ()))


manager = TimeManager(600, FakeTopics(), feedback=None, turn_cap=5)
with manager:
    # Pretend the student walked away for an hour
    manager.start_time = time.time() - 3600
check("elapsed time clamped to the cap", manager.get_remaining_time() == 595,
      manager.get_remaining_time())

print()
if failures:
    print(f"FAILURES ({len(failures)}): " + ", ".join(failures))
    raise SystemExit(1)
print("all checks passed")
