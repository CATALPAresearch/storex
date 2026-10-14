"""Two exams at once, in different courses. Nothing may leak between them."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.support import call, check, drain, finish, require_free_slots  # noqa: E402

require_free_slots()

print("1) unknown course is refused")
check("unknown course -> 400", call("POST", "/api/exam",
      {"name": "X", "minutes": 10, "course": "gibtsnicht"})[0] == 400)

print("2) start one exam per course")
exams = {}
for course_id, name in (("oop", "Luna"), ("grundlagen-db", "Linus")):
    status, created = call("POST", "/api/exam",
                           {"name": name, "minutes": 10, "course": course_id})
    check(f"{course_id} started", status == 201, created)
    check(f"{course_id} echoes its course", created.get("course") == course_id, created)
    exams[course_id] = created["exam_id"]
    print(f"      {course_id}: {created.get('course_title')}")

print("3) walk both to their first subject question")
first = {}
for course_id, exam_id in exams.items():
    events, since, _state = drain(exam_id, 0, {"listen"})
    call("POST", "/api/answer/text", {"exam_id": exam_id, "text": "Guten Tag, ich bin bereit."})
    events, since, _state = drain(exam_id, since, {"listen"})
    spoken = [e["text"] for e in events if e["type"] == "say"]
    first[course_id] = spoken[0] if spoken else ""
    exams[course_id] = (exam_id, since)
    print(f"      {course_id}: {first[course_id][:88]}")

check("oop asks about objects", "objektorientiert" in first["oop"].lower(), first["oop"][:50])
check("db asks about the relational model",
      "relational" in first["grundlagen-db"].lower(), first["grundlagen-db"][:50])
check("the two questions differ", first["oop"] != first["grundlagen-db"])

print("4) answer each in its own subject")
for course_id, answer in (("oop", "Ein Objekt hat einen Zustand, ein Verhalten und Beziehungen zu anderen Objekten."),
                          ("grundlagen-db", "Daten werden in Relationen abgelegt, also in Tabellen aus Tupeln und Attributen.")):
    exam_id, since = exams[course_id]
    status, _ = call("POST", "/api/answer/text", {"exam_id": exam_id, "text": answer})
    check(f"{course_id} accepted the answer", status == 200, status)
    events, since, _state = drain(exam_id, since, {"listen", "finished", "error"})
    reaction = next((e["text"] for e in events if e["type"] == "say"), "")
    exams[course_id] = (exam_id, since)
    print(f"      {course_id} reacted: {reaction[:88]}")
    check(f"{course_id} kept going", bool(reaction))

print("5) the db course runs out of questions and ends cleanly")
exam_id, since = exams["grundlagen-db"]
for _ in range(120):
    status, data = call("GET", f"/api/events?exam_id={exam_id}&since={since}")
    since = data["since"]
    for event in data["events"]:
        if event["type"] in ("finished", "error"):
            print(f"      {event['type']}: {event.get('text', '')[:88]}")
    if data["closed"]:
        break
    if data["state"] == "listening":
        call("POST", "/api/answer/text", {"exam_id": exam_id, "text": "Eine Relation ist eine Tabelle."})
status, data = call("GET", f"/api/events?exam_id={exam_id}&since=0")
closed = data["closed"]
check("db exam reached its end", closed, data["state"])
transcript = " ".join(e.get("text", "") for e in data["events"] if e["type"] == "say")
check("db transcript never mentions the other course",
      "objektorientiert" not in transcript.lower())
check("db feedback names its own unit",
      "relational" in transcript.lower() or "SQL" in transcript, transcript[-200:][:120])

print("6) clean up")
for course_id in ("oop", "grundlagen-db"):
    call("DELETE", f"/api/exam/{exams[course_id][0]}")
status, health = call("GET", "/api/health")
check("slots released", health["sessions"] == 0, health["sessions"])

finish()
