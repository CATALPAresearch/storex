"""Synthesize German speech with Piper, then transcribe it with Whisper."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import os  # noqa: E402
import wave  # noqa: E402

os.environ.setdefault("TTS_ENGINE", "piper")

from oral_exam import models  # noqa: E402
from oral_exam.audio import synthesis as tts  # noqa: E402
from oral_exam.audio.transcription import is_silence  # noqa: E402

failures = []


def check(label, condition, detail=""):
    print(f"  [{'ok ' if condition else 'FAIL'}] {label}{(' - ' + str(detail)) if detail else ''}")
    if not condition:
        failures.append(label)


SENTENCE = "Ein Literal ist eine Repräsentation eines Objekts in der Syntax der Programmiersprache."

print("1) speech synthesis")
wav = tts.synthesize(SENTENCE)
check("piper produced audio", wav is not None and len(wav) > 10000, len(wav or b""))
with open("/tmp/answer.wav", "wb") as handle:
    handle.write(wav)
with wave.open("/tmp/answer.wav") as handle:
    seconds = handle.getnframes() / handle.getframerate()
    print(f"      {len(wav)} bytes, {seconds:.1f}s, {handle.getframerate()} Hz, "
          f"{handle.getnchannels()} channel(s), {handle.getsampwidth() * 8} bit")
check("audio is a few seconds long", 2 < seconds < 15, round(seconds, 1))

print("2) transcription of those raw bytes (ffmpeg decode + whisper)")
transcript = models.get_speech_recognition().transcribe(wav, "audio/wav")
print(f"      spoken:      {SENTENCE}")
print(f"      transcribed: {transcript}")
check("something was transcribed", transcript is not None)
if transcript:
    lowered = transcript.lower()
    hits = [word for word in ("literal", "objekt", "syntax", "programmiersprache") if word in lowered]
    check("key terms recognised", len(hits) >= 2, hits)

print("3) silence is reported as silence")
# One second of digital silence, the shape a muted microphone produces
silent = bytearray()
with wave.open("/tmp/silence.wav", "wb") as handle:
    handle.setnchannels(1)
    handle.setsampwidth(2)
    handle.setframerate(16000)
    handle.writeframes(b"\x00\x00" * 16000)
with open("/tmp/silence.wav", "rb") as handle:
    silent = handle.read()
result = models.get_speech_recognition().transcribe(silent, "audio/wav")
check("silence transcribes to None", result is None, repr(result))
check("stock phrases count as silence", is_silence("Vielen Dank.") and is_silence("") and is_silence("  "))
check("a real answer does not", not is_silence("Ein Objekt ist eine Instanz."))

print()
if failures:
    print(f"FAILURES ({len(failures)}): " + ", ".join(failures))
    raise SystemExit(1)
print("all checks passed")
