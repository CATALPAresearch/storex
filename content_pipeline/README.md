# Content pipeline

How a course document becomes a course the exam can use. Every step takes
`--course <id>` and finds its input through that course's `manifest.yaml`;
nothing is hard coded to a particular course any more.

```
courses/<id>/source/<document>.pdf
  │
  │  01_split_pdf.py --course <id>
  ▼
courses/<id>/source/chapters_raw/        one text file per chapter
  │
  │  ⚠ MANUAL STEP, see below
  ▼
courses/<id>/source/chapters/            cleaned, renamed, plus hand written question files
  │
  │  02_generate_questions.py --course <id>      one request per paragraph
  ▼
courses/<id>/source/chapters/            same files, now with Frage:/Antwort: lines
  │
  ├─ 03_collect_questions.py --course <id>  ──▶ courses/<id>/units/<unit>.generated.json
  │                                             ← this is what the application reads
  └─ 04_build_vectorstore.py --course <id>  ──▶ courses/<id>/materials/vectorstore/
```

Afterwards:

```
python -m courselib.validate --course <id> --verbose
```

## The manual step

Between 01 and 02 the raw chapters are reworked by hand, and this is not
automated:

- obvious scanning artefacts are cleaned up
- the course unit overviews are renamed to `KE1.txt` … `KE7.txt`
- hand written question collections are added as `FragenKE2.txt` … `FragenKE7.txt`

The result is `source/chapters/`. For the OOP course this was done once in 2024.

## Questions a teacher writes

Step 03 **overwrites** `<unit>.generated.json` on every run. Questions written
by hand therefore belong in a separate file, by convention
`<unit>.authored.json`, which no script ever touches. List both in the
manifest and they are merged:

```yaml
units:
  - id: ke1
    questions:
      - units/ke1.generated.json
      - units/ke1.authored.json
```

A hand written question may carry its own `keywords`; the evaluation then
checks exactly those terms instead of deriving them from the sample answer.
`courses/oop/units/ke1.authored.json` is a worked example.

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
last unit takes the rest.

## The other scripts

| Script | Purpose |
|---|---|
| `sort_technical_terms.py` | normalises a course's technical term list in place |
| `export_training_data.py` | exports the chapters as a fine-tuning CSV, for `finetuning/` |
| `export_qag_format.py` | not currently runnable, kept for reference; see its docstring |

## A warning about step 01

`01_split_pdf.py` is a scraper for one particular book. The German markers it
looks for, the page offsets and several hand patched special cases are specific
to the OOP course text. For a different document it has to be adapted, not
merely configured.
