"""
Runs one exam in a background thread.

The ExamManager was written for a terminal and used to call exit() when it was
done or when the microphone was dead. In a thread that would be useless:
threading ignores SystemExit without a traceback, so the thread would vanish and
the browser would wait forever. The exam now raises instead, and every outcome
is reported as an event on the channel.
"""
import logging

from oral_exam.exam import ExamAborted, ExamManager, MicrophoneUnavailable
from oral_exam.llm import LLMError

logger = logging.getLogger(__name__)


def run_exam(session):
    """Thread target: runs the exam and reports how it ended."""
    channel = session.channel
    try:
        session.exam = ExamManager(session.parameters, channel=channel)
        session.exam.start_exam()
        channel.emit("finished", "Die Trainingsprüfung ist beendet.")
        channel.close("finished")

    except MicrophoneUnavailable as error:
        channel.emit("mic_failed", str(error))
        channel.close("error")

    except ExamAborted as error:
        logger.info("Exam %s aborted: %s", session.id, error)
        channel.emit("error", str(error))
        channel.close("error")

    except LLMError as error:
        logger.error("Exam %s lost the text generation backend: %s", session.id, error)
        channel.emit("error", "Die Textgenerierung ist nicht erreichbar. "
                              "Bitte prüfen Sie die Konfiguration von BASE_URL, API_KEY und MODEL.")
        channel.close("error")

    except Exception as error:  # noqa: BLE001 - the thread must never die silently
        logger.exception("Exam %s failed: %s", session.id, error)
        channel.emit("error", f"Unerwarteter Fehler: {error}")
        channel.close("error")
