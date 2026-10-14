"""
The content pipeline must end in a course the application can load.

Builds a throwaway course from two short chapter texts and runs steps 02, 03
and 04 over it. The full OOP course is deliberately not rebuilt: step 02 costs
one request per paragraph over 218 chapters. What is checked here is the chain
and the format, not the regeneration of the published data set.

Step 01 is not covered: it needs PyPDF2 from the research extra and is a
scraper for one particular book.
"""
import json
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.support import check, finish  # noqa: E402

REPOSITORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIPELINE = os.path.join(REPOSITORY, "content_pipeline")

CHAPTERS = {
    "1.txt": """Das Flussdiagramm

Ein Flussdiagramm stellt den Ablauf eines Programms grafisch dar. Jeder Kasten
steht für einen Arbeitsschritt, jede Raute für eine Verzweigung.

Eine Schleife wird im Flussdiagramm durch einen Pfeil dargestellt, der zu einem
früheren Schritt zurückführt.
""",
    "2.txt": """Der Struktogramm

Ein Struktogramm beschreibt denselben Ablauf ohne Pfeile. Es besteht aus
geschachtelten Rechtecken und erzwingt dadurch strukturierte Programmierung.
""",
}

MANIFEST = """\
id: {course_id}
title: Testkurs Programmablauf
language: de
units:
  - id: diagramme
    title: Ablaufdarstellungen
    questions: units/diagramme.generated.json
    chapters:
      files: []
source:
  chapters: source/chapters
materials:
  vector_store:
    path: materials/vectorstore
    embedding_model: paraphrase-multilingual-MiniLM-L12-v2
"""


def run(script, *arguments):
    result = subprocess.run([sys.executable, os.path.join(PIPELINE, script), *arguments],
                            capture_output=True, text=True, timeout=1800)
    return result


courses_root = os.path.join(REPOSITORY, "courses")
course_id = "zz-pipeline-test"
course = os.path.join(courses_root, course_id)
shutil.rmtree(course, ignore_errors=True)

try:
    chapters = os.path.join(course, "source", "chapters")
    os.makedirs(chapters)
    os.makedirs(os.path.join(course, "units"))
    for name, text in CHAPTERS.items():
        with open(os.path.join(chapters, name), "w", encoding="utf-8") as handle:
            handle.write(text)
    with open(os.path.join(course, "manifest.yaml"), "w", encoding="utf-8") as handle:
        handle.write(MANIFEST.format(course_id=course_id))

    print("1) step 02 writes question-answer pairs into the chapters")
    result = run("02_generate_questions.py", "--course", course_id)
    check("step 02 ran", result.returncode == 0, result.stderr.strip()[-300:])
    annotated = open(os.path.join(chapters, "1.txt"), encoding="utf-8").read()
    check("the chapter now holds a question", "Frage:" in annotated,
          annotated[:120].replace("\n", " "))
    check("and an answer", "Antwort:" in annotated)

    print("2) step 03 collects them into the unit file")
    result = run("03_collect_questions.py", "--course", course_id)
    check("step 03 ran", result.returncode == 0, result.stderr.strip()[-300:])
    unit_file = os.path.join(course, "units", "diagramme.generated.json")
    check("the unit file exists", os.path.isfile(unit_file))
    payload = json.loads(open(unit_file, encoding="utf-8").read())
    check("it is keyed by level", sorted(payload) == ["ANALYZE", "APPLY", "REMEMBER"], sorted(payload))
    collected = sum(len(payload[key]) for key in payload)
    check("it holds questions", collected > 0, f"{collected} questions")
    sample = next(q for key in payload for q in payload[key])
    check("each entry has question and answer",
          bool(sample.get("question")) and bool(sample.get("answer")), sample)

    print("3) step 04 builds the vector store")
    result = run("04_build_vectorstore.py", "--course", course_id)
    check("step 04 ran", result.returncode == 0, result.stderr.strip()[-300:])
    store = os.path.join(course, "materials", "vectorstore")
    check("index.faiss written", os.path.isfile(os.path.join(store, "index.faiss")))
    check("index.pkl written", os.path.isfile(os.path.join(store, "index.pkl")))

    print("4) the result is a course the application accepts")
    import courselib
    courselib.load_all(force=True)
    loaded = courselib.get(course_id)
    check("courselib loads it", loaded.question_count == collected,
          f"{loaded.question_count} questions")
    check("its vector store is declared", loaded.materials.vector_store_path is not None)

    result = subprocess.run([sys.executable, "-m", "courselib.validate",
                             "--course", course_id, "--strict"],
                            capture_output=True, text=True, cwd=REPOSITORY, timeout=120)
    check("the validator accepts it", result.returncode == 0, result.stdout.strip()[-300:])
    print("      " + result.stdout.strip().splitlines()[-1])
finally:
    shutil.rmtree(course, ignore_errors=True)

finish()
