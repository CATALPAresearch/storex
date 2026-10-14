"""Answer a real question with real synthesized speech, over HTTP."""
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
import uuid

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.support import BASE, call, check, drain, finish, require_free_slots  # noqa: E402

require_free_slots()


def post_audio(exam_id, wav):
    """Uploads a WAV as multipart/form-data, the way the browser does."""
    boundary = uuid.uuid4().hex
    parts = [
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"exam_id\"\r\n\r\n{exam_id}\r\n".encode(),
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"answer.wav\"\r\n"
        f"Content-Type: audio/wav\r\n\r\n".encode(),
        wav,
        f"\r\n--{boundary}--\r\n".encode(),
    ]
    request = urllib.request.Request(
        BASE + "/api/answer", data=b"".join(parts), method="POST",
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            return response.status, json.loads(response.read() or b"null")
    except urllib.error.HTTPError as error:
        return error.code, json.loads(error.read() or b"null")


print("0) synthesize an answer inside the container")
SENTENCE = "Ein Objekt hat einen Zustand und ein Verhalten und steht in Beziehung zu anderen Objekten."
script = (
    "import sys; from oral_exam.audio import synthesis;"
    f"sys.stdout.buffer.write(synthesis.synthesize({SENTENCE!r}))"
)
wav = subprocess.run(
    ["docker", "compose", "exec", "-T", "-e", "TTS_ENGINE=piper", "exam", "python", "-c", script],
    capture_output=True, timeout=300).stdout
check("got a WAV to upload", wav[:4] == b"RIFF" and len(wav) > 10000, f"{len(wav)} bytes")
if not wav:
    sys.exit(1)

print("1) start an exam and reach a question")
status, created = call("POST", "/api/exam", {"name": "Luna", "gender": "female", "minutes": 10})
check("exam created", status == 201, created)
exam_id = created["exam_id"]
check("tts engine reported as piper", created.get("tts") == "piper", created)

events, since, _state = drain(exam_id, 0, {"listen"})
greeting = next((e for e in events if e["type"] == "say"), None)
check("greeting arrived", greeting is not None)

print("2) the greeting is available as server rendered audio")
request = urllib.request.Request(f"{BASE}/api/tts/{exam_id}/{greeting['seq']}")
with urllib.request.urlopen(request, timeout=120) as response:
    audio = response.read()
    check("tts endpoint serves WAV", response.headers["Content-Type"] == "audio/wav"
          and audio[:4] == b"RIFF", f"{response.status}, {len(audio)} bytes")

print("3) answer the microphone check by uploading speech")
status, result = post_audio(exam_id, wav)
check("upload accepted", status == 200, status)
check("speech was transcribed", result and result.get("text"), result)
check("not treated as silence", result and not result.get("silence"), result)
print(f"      transcribed: {result.get('text')}")

print("4) the exam continues with a real question")
events, since, _state = drain(exam_id, since, {"listen"})
question = next((e["text"] for e in events if e["type"] == "say"), None)
check("next question asked", bool(question), question)
print(f"      question: {str(question)[:95]}")

print("5) answer that question with the same speech")
status, result = post_audio(exam_id, wav)
check("second upload accepted", status == 200, status)
events, since, _state = drain(exam_id, since, {"listen", "finished", "error"})
check("examiner reacted", any(e["type"] == "say" for e in events))
print(f"      reaction: {str(next((e['text'] for e in events if e['type'] == 'say'), ''))[:95]}")

call("DELETE", f"/api/exam/{exam_id}")
finish()
