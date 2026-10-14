"""
Questions a teacher writes must survive a run of the content pipeline.

Step 3 regenerates the unit files of a course. This checks that it writes only
its own file, leaves hand written ones untouched, and that both end up in the
loaded course.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import courselib  # noqa: E402

from tests.support import check, finish  # noqa: E402

REPOSITORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSE = os.path.join(REPOSITORY, "courses", "oop")
AUTHORED = os.path.join(COURSE, "units", "ke1.authored.json")


def digest(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


print("1) the hand written file is part of the course")
course = courselib.get("oop")
unit = course.units[0]
sources = dict(unit.sources)
check("unit ke1 reads two files", len(unit.sources) == 2, unit.sources)
check("the generated file contributes 173", sources.get("units/ke1.generated.json") == 173, sources)
check("the authored file contributes 2", sources.get("units/ke1.authored.json") == 2, sources)

questions = [q["question"] for level in unit.questions for q in level]
check("a hand written question is in the pool",
      any("dasselbe Objekt bezeichnen" in q for q in questions))

print("2) a hand written question keeps its own keywords")
authored = json.loads(open(AUTHORED, encoding="utf-8").read())
first = authored["REMEMBER"][0]
check("it declares keywords", first.get("keywords") == ["Identität", "Gleichheit", "Verweis"], first.get("keywords"))
in_course = next(q for level in unit.questions for q in level
                 if q["question"] == first["question"])
check("the loader passes them through", in_course.get("keywords") == first["keywords"], in_course)

print("3) step 3 does not touch it")
before = digest(AUTHORED)
target = tempfile.mkdtemp(prefix="collect-")
try:
    result = subprocess.run(
        [sys.executable, os.path.join(REPOSITORY, "content_pipeline", "03_collect_questions.py"),
         "--course", "oop", "--output-dir", target],
        capture_output=True, text=True, timeout=600)
    check("step 3 ran", result.returncode == 0, result.stderr.strip()[-200:])
    written = sorted(os.listdir(target))
    check("it wrote one file per unit", len(written) == 5, written)
    check("named .generated.json", all(n.endswith(".generated.json") for n in written), written)
    check("it never wrote an authored file",
          not any("authored" in n for n in written), written)
    check("the hand written file is unchanged", digest(AUTHORED) == before)
finally:
    shutil.rmtree(target, ignore_errors=True)

finish()
