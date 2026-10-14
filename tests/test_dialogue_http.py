"""End-to-end check of the web app over HTTP, without a microphone."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.support import call, check, drain, finish, require_free_slots  # noqa: E402

require_free_slots()

print("1) health")
status, health = call("GET", "/api/health")
check("health answers 200", status == 200, status)
check("ffmpeg available", health and health.get("ffmpeg"), health)
check("no session yet", health and health.get("sessions") == 0, health)

print("2) validation is enforced")
check("empty name rejected", call("POST", "/api/exam", {"name": ""})[0] == 400)
check("5 minutes rejected", call("POST", "/api/exam", {"name": "Luna", "minutes": 5})[0] == 400)
check("unknown exam is 404", call("GET", "/api/events?exam_id=nope")[0] == 404)

print("3) start an exam")
status, created = call("POST", "/api/exam", {"name": "Luna", "gender": "female", "minutes": 10})
check("exam created", status == 201, created)
if status != 201:
    sys.exit(1)
exam_id = created["exam_id"]

print("4) greeting and microphone check")
events, since, state = drain(exam_id, 0, {"listen", "error", "mic_failed"})
check("examiner spoke", any(e["type"] == "say" for e in events))
check("asked to listen", any(e["type"] == "listen" for e in events), state)

print("5) answer the microphone check")
# Whether a second answer right afterwards is refused depends on how far the
# exam thread has got, so that guard is checked deterministically in the
# channel unit test instead.
status, _ = call("POST", "/api/answer/text", {"exam_id": exam_id, "text": "Hallo, hier ist Luna."})
check("answer accepted", status == 200, status)

print("6) first real question and its evaluation")
events, since, state = drain(exam_id, since, {"listen"})
check("transcript echoed", any(e["type"] == "transcript" for e in events))
check("question asked", any(e["type"] == "say" for e in events))
check("listening again", any(e["type"] == "listen" for e in events), state)

print("7) a wrong answer must keep the dialogue going")
status, _ = call("POST", "/api/answer/text",
                 {"exam_id": exam_id, "text": "Ein Literal ist ein Fahrrad mit drei Raedern."})
check("wrong answer accepted", status == 200, status)
events, since, state = drain(exam_id, since, {"listen"})
check("examiner responded", any(e["type"] == "say" for e in events), state)

print("8) clock and transcript")
status, data = call("GET", f"/api/events?exam_id={exam_id}&since={since}")
check("clock is counting", isinstance(data.get("remaining_seconds"), (int, float))
      and 0 < data["remaining_seconds"] <= 600, data.get("remaining_seconds"))
status, data = call("GET", f"/api/transcript/{exam_id}")
check("transcript has turns", status == 200 and len(data["transcript"]) >= 4, len(data.get("transcript", [])))

print("9) session accounting and cancel")
status, health = call("GET", "/api/health")
check("one session active", health.get("sessions") == 1, health)
check("cancel returns 204", call("DELETE", f"/api/exam/{exam_id}")[0] == 204)
status, health = call("GET", "/api/health")
check("slot released", health.get("sessions") == 0, health)

finish()
