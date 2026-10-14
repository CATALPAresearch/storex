# content_pipeline — turning a document into a course

Produces what [`courses/`](../courses/README.md) describes and
[`courselib/`](../courselib/README.md) reads. Every step takes `--course <id>`
and finds its input through that course's manifest; nothing is hard coded to a
particular course.

```
courses/<id>/source/<document>.pdf
  │
  │  01_split_pdf.py --course <id>
  ▼
courses/<id>/source/chapters_raw/     one text file per chapter
  │
  │  ⚠ MANUAL STEP, see below
  ▼
courses/<id>/source/chapters/         cleaned, renamed, plus hand written question files
  │
  │  02_generate_questions.py --course <id>     one request per paragraph
  ▼
courses/<id>/source/chapters/         same files, now with Frage:/Antwort: lines
  │
  ├─ 03_collect_questions.py --course <id> ──▶ courses/<id>/units/<unit>.generated.json
  │                                            ← this is what the application reads
  └─ 04_build_vectorstore.py --course <id> ──▶ courses/<id>/materials/vectorstore/
```

Then check the result:

```shell
python -m courselib.validate --course <id> --verbose
```

In Docker, where steps 02 to 04 have everything they need:

```shell
docker compose run --rm exam python content_pipeline/03_collect_questions.py --course oop
```

## The steps

| Step | Reads | Writes |
|---|---|---|
| `01_split_pdf.py` | `source.document` | `source.chapters_raw` |
| `02_generate_questions.py` | `source.chapters` | the same files, annotated |
| `03_collect_questions.py` | `source.chapters` | `units/<unit>.generated.json` |
| `04_build_vectorstore.py` | `source.chapters` | `materials.vector_store.path` |

**01** needs `PyPDF2` from the research extra and does **not** run in the
container image. It is also a scraper written for one particular book: the
German markers it looks for, the page offsets and several hand patched special
cases are specific to the OOP course text. For another document it has to be
adapted, not merely configured.

**02** sends one request per paragraph to the text generation backend, so it is
run when the material changes, not routinely. For the OOP course that is
roughly 218 chapters.

**03** sorts every pair into a unit and a level. A question asking what
something *is* counts as recall, *how* or *why* as application, and one asking
for advantages, drawbacks or differences as analysis — the rules of the
published system, unchanged.

**04** embeds the chapter prose; the generated `Frage:`/`Antwort:` lines are
stripped first, so the index holds teaching text only.

## The manual step

Between 01 and 02 the raw chapters are reworked by hand, and this is not
automated:

- obvious scanning artefacts are cleaned up
- the course unit overviews are renamed to `KE1.txt` … `KE7.txt`
- hand written question collections are added as `FragenKE2.txt` … `FragenKE7.txt`

The result is `source/chapters/`. For the OOP course this was done once in 2024.

## Which chapter belongs to which unit

Declared per unit in the manifest, not in the code:

```yaml
units:
  - id: ke1
    chapters:
      files: [KE1]          # chapter files with these names
      numbers_below: 6      # and numbered chapters below this
```

A numbered chapter goes to the first unit whose `numbers_below` exceeds it; the
last unit takes the rest. A single unit with an empty `chapters:` block takes
every chapter, which is how a one-unit course is written.

## Questions written by hand are safe

Step 03 overwrites only `<unit>.generated.json`. It never reads or writes a file
named otherwise, so `<unit>.authored.json` survives every run. See
[courses/README.md](../courses/README.md) for how to add one.

`--output-dir` writes elsewhere, which is useful to inspect what a run would
produce before replacing the current files.

## The other scripts

| Script | Purpose |
|---|---|
| `sort_technical_terms.py` | normalises a course's technical term list in place |
| `export_training_data.py` | exports the chapters as a fine-tuning CSV, for `finetuning/` |
| `export_qag_format.py` | not currently runnable; its input directory has never existed in this repository. Kept for reference, see its docstring |
| `_course.py` | shared helper: finds a course and resolves its manifest paths |
