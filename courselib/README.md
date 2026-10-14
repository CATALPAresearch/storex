# courselib — reading and validating course content

The contract between the content in [`courses/`](../courses/README.md), the
application in [`oral_exam/`](../oral_exam/README.md) and the
[`content_pipeline/`](../content_pipeline/README.md). It sits beside the
application package rather than inside it because all three use it.

It depends only on `pyyaml`, the standard library and two helpers from
`oral_exam.utils`. Loading a course never touches a model, so the validator
runs in well under a second.

## Using it

```python
import courselib

courselib.all_courses()        # loadable courses, the default first
courselib.get("oop")           # one course, raises UnknownCourse
courselib.default_course_id()  # DEFAULT_COURSE, else the first by id
courselib.errors()             # {course_id: [problems]} of what was skipped
```

Everything is read once into frozen dataclasses at the first call and kept in a
module-level registry behind a lock. No file is touched while an exam runs.
Whatever an exam mutates — the question pools, which shrink as questions are
asked — is copied by the question manager, not by the loader.

```python
course.units[0].title            # 'Grundkonzepte der objektorientierten Programmierung'
course.units[0].questions[Level.APPLY]   # positional, like the Level enum
course.units[0].sources          # (('units/ke1.generated.json', 173), ('units/ke1.authored.json', 2))
course.materials.technical_terms # already parsed, synonyms as lists
course.materials.vector_store_path
course.unit_titles, course.question_count
```

`Unit.questions` is a tuple of three tuples, in the order of
`oral_exam.utils.helpers.Level`, so `questions[Level.APPLY]` works without a
lookup table. `Unit.sources` records how many questions each file contributed —
that is how a teacher sees whether an `*.authored.json` arrived.

## Modules

| Module | Contents |
|---|---|
| `model.py` | `Course`, `Unit`, `OpenQuestion`, `Materials` — frozen dataclasses |
| `loader.py` | discovery, reading, the registry, every validation rule |
| `validate.py` | the `python -m courselib.validate` command |

Loader and validator share the same code on purpose: the validator cannot drift
away from what the application actually accepts, because it *is* what the
application does, with the problems collected instead of raised.

## What is checked

The loader collects problems rather than stopping at the first one, so a content
author gets everything wrong with a manifest in one report.

**Errors** — the course is skipped:

- `manifest.yaml` missing, unparseable, or not a mapping
- `id` missing, malformed, or not equal to the directory name
- `title` missing; `units` missing or empty; a unit without `id`, `title` or `questions`
- a unit id used twice
- a path that does not exist, or that resolves outside the course directory
- a question file that is not an object keyed by level, or an entry without a non-empty `question` and `answer`
- a level key outside `REMEMBER`, `APPLY`, `ANALYZE` — never silently dropped
- a declared `levels` list that disagrees with what the files hold
- a vector store without `embedding_model`, or one that disagrees with the application's
- a course that holds no questions at all

**Warnings** — reported, course still usable:

- unknown manifest or unit keys, which catches typos such as `unit:`
- `language` other than `de`
- a `source` path that is not present

That last one matters: build material is deliberately excluded from the
container image, so treating it as an error would make every course unloadable
in production.

## The command

```shell
python -m courselib.validate                        # all courses
python -m courselib.validate --course oop --verbose # one, with its units
python -m courselib.validate --strict               # warnings fail too
python -m courselib.validate --json                 # for CI
```

Exit code 0 when every course loads, 1 when any fails, and with `--strict` also
1 on warnings. In Docker: `docker compose run --rm validate`.

```
OK    oop  Objektorientierte Programmierung  (5 units, 1282 questions, 464 technical terms, vector store, own paraphrase model)
        ke1   175 questions  (173 from units/ke1.generated.json, 2 from units/ke1.authored.json)
        ke2   224 questions  (units/ke2.generated.json)
```

## Where the courses are

`COURSES_DIR`, otherwise `courses/` beside the repository root. Every direct
subdirectory holding a `manifest.yaml` is a course; names starting with `.` or
`_` are ignored.
