"""Two exams at once: the shared question data must not bleed between them."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.support import call, check, drain, finish, require_free_slots  # noqa: E402

require_free_slots()

print("start two exams")
ids = []
for name in ("Luna", "Linus"):
    status, created = call("POST", "/api/exam", {"name": name, "minutes": 10})
    check(f"exam for {name} created", status == 201, created)
    ids.append(created["exam_id"])

status, busy = call("POST", "/api/exam", {"name": "Dritte", "minutes": 10})
check("third exam refused with 503", status == 503, busy)

print("walk both through the greeting to the first topic question")
questions = {}
for exam_id, name in zip(ids, ("Luna", "Linus")):
    events, since, _state = drain(exam_id, 0, {"listen"})
    call("POST", "/api/answer/text", {"exam_id": exam_id, "text": "Hallo, ich bin da."})
    events, since, _state = drain(exam_id, since, {"listen"})
    spoken = [e["text"] for e in events if e["type"] == "say"]
    questions[name] = spoken[0] if spoken else ""
    print(f"    {name}: {questions[name][:95]}")

for name, text in questions.items():
    check(f"{name} got a question", bool(text))
    # The prefix is spoken once. It used to be written back into the shared
    # question data, so a later exam saw it accumulated.
    check(f"{name}'s question has no doubled prefix",
          text.count("Dann lassen Sie uns beginnen") <= 1, text[:80])
    check(f"{name}'s question is not stacked with fillers",
          not text.startswith("Ok. Dann lassen Sie uns beginnen. Ok."), text[:60])

check("both exams got the course unit's open question",
      all("Grundkonzept" in text for text in questions.values()), questions)

print("clean up")
for exam_id in ids:
    call("DELETE", f"/api/exam/{exam_id}")
status, health = call("GET", "/api/health")
check("all slots released", health.get("sessions") == 0, health)

finish()
