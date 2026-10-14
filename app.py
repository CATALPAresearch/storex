"""
Web app for the oral exam simulation.

The browser records the student, this app transcribes the recording and runs the
same exam conversation the command line version runs. A container has no access
to a microphone, so capturing audio in the browser is what makes the simulation
usable in Docker.

Start it with: docker compose up   ->   http://localhost:5000
"""
import logging
import os
import shutil

from flask import Flask, jsonify, request, send_from_directory

import llm
import models
import tts

from web.session import SessionRegistry, SessionsBusy

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"),
                    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s")
logger = logging.getLogger(__name__)

STATIC_DIRECTORY = os.path.join(os.path.dirname(__file__), "static")

app = Flask(__name__, static_folder=None)
# Whisper runs inside the request, so an oversized upload would occupy a worker
app.config["MAX_CONTENT_LENGTH"] = int(os.getenv("MAX_UPLOAD_MB", "10")) * 1024 * 1024

sessions = SessionRegistry()

# Set if loading the models failed, reported by /api/health and /api/exam
startup_error = None


def _require_session(exam_id):
    """Returns (session, error_response). Exactly one of the two is None."""
    session = sessions.get(exam_id)
    if session is None:
        return None, (jsonify({"error": "unknown exam"}), 404)
    return session, None


@app.route("/")
def index():
    return send_from_directory(STATIC_DIRECTORY, "index.html")


@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(STATIC_DIRECTORY, filename)


@app.route("/api/health")
def health():
    sessions.reap()
    return jsonify({
        "ready": startup_error is None,
        "error": startup_error,
        "sessions": sessions.count(),
        "max_sessions": sessions.max_sessions,
        "retained": sessions.total(),
        # The transcription pipeline decodes browser audio with ffmpeg
        "ffmpeg": shutil.which("ffmpeg") is not None,
        "tts": tts.engine(),
        "llm_configured": bool(llm.BASE_URL) or llm.is_disabled(),
    })


@app.route("/api/exam", methods=["POST"])
def create_exam():
    """Starts a new exam and returns its id."""
    if startup_error:
        return jsonify({"error": startup_error}), 503

    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    if not name:
        return jsonify({"error": "Bitte geben Sie einen Namen an."}), 400

    try:
        minutes = int(data.get("minutes", 25))
    except (TypeError, ValueError):
        return jsonify({"error": "Die Dauer muss eine Zahl sein."}), 400
    if not 10 <= minutes <= 60:
        return jsonify({"error": "Die Trainingsprüfung kann 10 bis 60 Minuten dauern."}), 400

    gender = (data.get("gender") or "").lower()
    parameters = {
        "name": name,
        "time": minutes,
        "female": gender == "female",
        "male": gender == "male",
        "mute": True,  # audio is played by the browser, never by the server process
    }

    try:
        session = sessions.create(parameters)
    except SessionsBusy as error:
        return jsonify({"error": str(error)}), 503

    logger.info("Started exam %s for %s (%s minutes)", session.id, name, minutes)
    return jsonify({"exam_id": session.id, "tts": tts.engine()}), 201


@app.route("/api/events")
def events():
    """Long-polls the examiner's utterances."""
    session, error = _require_session(request.args.get("exam_id", ""))
    if error:
        return error

    try:
        since = max(0, int(request.args.get("since", 0)))
    except ValueError:
        since = 0

    pending, state, closed = session.channel.poll(since=since)
    return jsonify({
        "events": pending,
        "state": state,
        "closed": closed,
        "since": since + len(pending),
        "remaining_seconds": session.remaining_seconds(),
    })


def _accept_answer(session, text, silence):
    """Hands a transcribed answer to the exam thread."""
    # An answer sent while the examiner is still speaking would otherwise sit in
    # the queue and be consumed as the answer to the next question.
    if session.channel.state != "listening" or not session.channel.submit(text):
        return jsonify({"error": "Die Prüfung wartet gerade nicht auf eine Antwort."}), 409

    event = session.channel.emit("transcript", text if text else "")
    return jsonify({"seq": event["seq"], "text": text, "silence": silence})


@app.route("/api/answer", methods=["POST"])
def answer():
    """Transcribes an uploaded recording and submits it as the answer."""
    session, error = _require_session(request.form.get("exam_id", ""))
    if error:
        return error

    upload = request.files.get("audio")
    if upload is None:
        return jsonify({"error": "Es wurde keine Aufnahme übertragen."}), 400

    recording = upload.read()
    if not recording:
        return _accept_answer(session, None, silence=True)

    text = models.get_speech_recognition().transcribe(recording, upload.mimetype)
    return _accept_answer(session, text, silence=text is None)


@app.route("/api/answer/text", methods=["POST"])
def answer_text():
    """Submits a typed answer, for demonstrating the system without a microphone."""
    data = request.get_json(silent=True) or {}
    session, error = _require_session(data.get("exam_id", ""))
    if error:
        return error

    text = (data.get("text") or "").strip() or None
    return _accept_answer(session, text, silence=text is None)


@app.route("/api/tts/<exam_id>/<int:seq>")
def speak(exam_id, seq):
    """Returns the examiner's utterance as WAV audio (TTS_ENGINE=piper)."""
    session, error = _require_session(exam_id)
    if error:
        return error
    if not tts.is_server_side():
        return jsonify({"error": "Server side speech synthesis is disabled."}), 404

    if seq not in session.audio_cache:
        utterance = next((event for event in session.channel.events
                          if event["seq"] == seq and event["type"] == "say"), None)
        if utterance is None:
            return jsonify({"error": "unknown utterance"}), 404
        audio = tts.synthesize(utterance.get("text", ""))
        if audio is None:
            return jsonify({"error": "Die Sprachsynthese ist fehlgeschlagen."}), 500
        session.audio_cache[seq] = audio

    return app.response_class(session.audio_cache[seq], mimetype="audio/wav")


# POST is accepted as well, because navigator.sendBeacon can only send POST and
# the page uses it to free the slot when the tab is closed.
@app.route("/api/exam/<exam_id>", methods=["DELETE", "POST"])
def cancel_exam(exam_id):
    """Cancels an exam and frees its slot."""
    session = sessions.remove(exam_id)
    if session is None:
        return jsonify({"error": "unknown exam"}), 404
    session.channel.abort()
    logger.info("Cancelled exam %s", exam_id)
    return "", 204


@app.route("/api/transcript/<exam_id>")
def transcript(exam_id):
    """The conversation so far."""
    session, error = _require_session(exam_id)
    if error:
        return error
    return jsonify({"exam_id": exam_id, "transcript": session.transcript()})


# Loading the models takes minutes, so it happens at import time rather than
# inside the first request.
if os.getenv("WARMUP", "true").lower() == "true":
    try:
        models.warmup(speech=True)
    except Exception as error:  # noqa: BLE001 - must not crash loop without a hint
        # Most likely the model cache is empty and the hub is unreachable
        startup_error = (
            "Die Modelle konnten nicht geladen werden. Laden Sie sie einmalig mit "
            "'docker compose run --rm warmup' herunter, oder setzen Sie HF_HUB_OFFLINE=0, "
            f"damit die App sie selbst holt. Ursache: {error}")
        logger.error(startup_error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), threaded=True)
