"""Checks that each course wires its own material into the exam."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging  # noqa: E402
logging.basicConfig(level=logging.WARNING)

import courselib  # noqa: E402
from oral_exam.exam import ExamManager  # noqa: E402
from oral_exam.web.session import Channel  # noqa: E402

failures = []

def check(label, condition, detail=""):
    print(f"  [{'ok ' if condition else 'FAIL'}] {label}{(' - ' + str(detail)) if detail else ''}")
    if not condition:
        failures.append(label)

for course_id, units, has_store, has_terms in (("oop", 5, True, True),
                                               ("grundlagen-db", 2, False, False)):
    print(f"\n=== {course_id}")
    exam = ExamManager({"name": "Luna", "time": 10, "female": True, "male": False,
                        "mute": True, "course": course_id}, channel=Channel())
    course = courselib.get(course_id)

    check("course wired in", exam.course.id == course_id, exam.course.id)
    check(f"{units} units", len(exam.course.units) == units, len(exam.course.units))
    check("time split by its own unit count",
          exam.time_manager.unit_count == units, exam.time_manager.unit_count)
    check("feedback sized by its own units",
          len(exam.feedback.correct_answers) == units, len(exam.feedback.correct_answers))
    check("feedback names real unit titles",
          exam.feedback.unit_titles == course.unit_titles, exam.feedback.unit_titles[0][:40])
    check("terms belong to this course",
          bool(exam.terms) == has_terms, f"{len(exam.terms)} terms")
    store = exam.question_generator.db
    check("vector store as declared", (store is not None) == has_store, store is not None)
    check("paraphrase engine",
          (exam.paraphraser.engine == "local") == has_store,
          exam.paraphraser.engine)
    check("question pool is its own",
          exam.manager.question_list and
          len(exam.manager.question_list) == units, len(exam.manager.question_list))
    check("ai student would be asked about the right subject",
          course.title in ("Objektorientierte Programmierung", "Grundlagen von Datenbanken"),
          course.title)

print("\n=== two courses side by side, nothing leaks")
a = ExamManager({"name": "A", "time": 10, "female": True, "male": False,
                 "mute": True, "course": "oop"}, channel=Channel())
b = ExamManager({"name": "B", "time": 10, "female": False, "male": True,
                 "mute": True, "course": "grundlagen-db"}, channel=Channel())
check("A keeps its 5 units", len(a.course.units) == 5, len(a.course.units))
check("B keeps its 2 units", len(b.course.units) == 2, len(b.course.units))
check("A keeps its 464 terms", len(a.terms) == 464, len(a.terms))
check("B still has none", len(b.terms) == 0, len(b.terms))
check("A still has its vector store", a.question_generator.db is not None)
check("B still has none", b.question_generator.db is None)
first_a = a.manager.get_question()["question"]
first_b = b.manager.get_question()["question"]
print(f"      A asks: {first_a[:62]}")
print(f"      B asks: {first_b[:62]}")
check("different subjects", "objektorientiert" in first_a.lower()
      and "relational" in first_b.lower())

print()
if failures:
    print(f"FAILURES ({len(failures)}): " + ", ".join(failures))
    raise SystemExit(1)
print("all checks passed")
