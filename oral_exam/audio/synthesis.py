"""
Text-to-speech for the web app.

TTS_ENGINE selects where the examiner's voice is produced:
    piper    (default) the server renders WAV audio with Piper and the page
             plays it. A proper German voice model, about ten times faster than
             real time on CPU, and it sounds the same for everyone.
    browser  the page speaks the text itself via the Web Speech API. No model
             needed, but the voice is whatever the operating system happens to
             ship, and on many systems it reads German poorly.

Bark, the engine used for the command line exam (see audio/text_to_speech.py),
is deliberately not offered here: there is no Metal acceleration inside the
container, so it needs tens of seconds per utterance and truncates anything
longer than about 14 seconds.
"""
import io
import logging
import os
import re
import threading
import wave

logger = logging.getLogger(__name__)

VOICE_REPO = "rhasspy/piper-voices"
# Highest quality German voice in the Piper collection. Measured against the
# other German voices it was both the most intelligible and the most natural,
# at about ten times real time on CPU.
VOICE_NAME = os.getenv("PIPER_VOICE", "de_DE-thorsten-high")

# A voice is published under <language>/<locale>/<speaker>/<quality>
VOICE_PATTERN = re.compile(r"^(?P<language>[a-z]{2,3})_(?P<region>[A-Z]{2})"
                           r"-(?P<speaker>.+)-(?P<quality>[a-z_]+)$")

_lock = threading.Lock()
_voice = None


def engine():
    """Returns the configured engine name, 'piper' or 'browser'."""
    name = os.getenv("TTS_ENGINE", "piper").lower()
    if name not in ("browser", "piper"):
        logger.warning("Unknown TTS_ENGINE '%s', falling back to 'piper'.", name)
        return "piper"
    return name


def is_server_side():
    """True if the server has to synthesize audio for the page."""
    return engine() == "piper"


def voice_directory(name):
    """
    Returns the directory a voice lives in, derived from its name.

    'de_DE-thorsten-high' is published as 'de/de_DE/thorsten/high'. Deriving it
    keeps the name and the path from drifting apart; PIPER_VOICE_DIR overrides
    it for a voice that does not follow the convention.
    """
    override = os.getenv("PIPER_VOICE_DIR")
    if override:
        return override

    match = VOICE_PATTERN.match(name)
    if not match:
        raise ValueError(f"Cannot derive a path for the voice '{name}'. "
                         "Set PIPER_VOICE_DIR to its directory in the voice repository.")
    parts = match.groupdict()
    return f"{parts['language']}/{parts['language']}_{parts['region']}/{parts['speaker']}/{parts['quality']}"


def get_voice():
    """Loads the Piper voice once per process, downloading it on first use."""
    global _voice
    if _voice is not None:
        return _voice

    with _lock:
        if _voice is None:
            from huggingface_hub import hf_hub_download
            from piper import PiperVoice

            logger.info("Loading Piper voice %s ...", VOICE_NAME)
            directory = voice_directory(VOICE_NAME)
            model = hf_hub_download(VOICE_REPO, f"{directory}/{VOICE_NAME}.onnx")
            config = hf_hub_download(VOICE_REPO, f"{directory}/{VOICE_NAME}.onnx.json")
            _voice = PiperVoice.load(model, config_path=config)
            logger.info("Loaded Piper voice %s.", VOICE_NAME)
    return _voice


def synthesize(text):
    """
    Renders the given text into a WAV file.

    :return: the WAV file as bytes, or None if no audio could be produced.
    """
    if not text or not text.strip():
        return None

    buffer = io.BytesIO()
    try:
        with wave.open(buffer, "wb") as wav_file:
            get_voice().synthesize_wav(text, wav_file)
    except Exception as error:  # noqa: BLE001 - a voice failure must not end an exam
        logger.exception("Speech synthesis failed: %s", error)
        return None

    return buffer.getvalue()
