# courses — the content

One directory per course. **No code lives here.** A course is read by
[`courselib/`](../courselib/README.md) and produced by
[`content_pipeline/`](../content_pipeline/README.md).

Adding a course means adding a directory. If it ever requires a code change,
that is a bug worth reporting.

```
courses/
  oop/                            Objektorientierte Programmierung
    manifest.yaml                 what this course is and what it brings
    units/
      ke1.generated.json          written by the pipeline, overwritten on every run
      ke1.authored.json           written by hand, never touched
      ke2.generated.json  …
    materials/                    read while an exam runs
      technical_terms.txt
      vectorstore/                index.faiss, index.pkl
    source/                       what the course was built from; not deployed
      Kurstext_OOP.pdf
      chapters_raw/  chapters/  dataset/
  grundlagen-db/                  a small example that brings no materials at all
```

## manifest.yaml

```yaml
id: oop                           # required, must equal the directory name
title: Objektorientierte Programmierung   # required: picker, heading, prompts
language: de                      # optional, default de
description: …                    # optional, shown in the picker

units:                            # required, asked in this order
  - id: ke1                       # required, unique within the course
    title: Grundkonzepte der objektorientierten Programmierung   # required
    questions:                    # required: one file, or several to merge
      - units/ke1.generated.json
      - units/ke1.authored.json
    levels: [REMEMBER, APPLY, ANALYZE]   # optional; must match what the files hold
    open_question:                # optional: the broad question the unit starts with
      question: Was ist das Grundkonzept der objektorientierten Programmierung?
      keywords: [Objekt, Beziehung, Zustand, Verhalten]
    chapters:                     # optional, only used by the content pipeline
      files: [KE1]
      numbers_below: 6

materials:                        # optional as a whole
  technical_terms: materials/technical_terms.txt
  vector_store:
    path: materials/vectorstore
    embedding_model: paraphrase-multilingual-MiniLM-L12-v2
  paraphrase_model: LunaticTanuki/oop-de-qg-flan-t5-base-v6

source:                           # optional, only used by the content pipeline
  document: source/Kurstext_OOP.pdf
  chapters_raw: source/chapters_raw
  chapters: source/chapters
  dataset: source/dataset
```

A question file holds the questions of one unit, grouped by level:

```json
{
  "REMEMBER": [{"question": "Was ist ein Literal?", "answer": "Ein Literal ist …"}],
  "APPLY": [],
  "ANALYZE": []
}
```

The three levels follow Bloom's taxonomy and are fixed; a course only declares
which of them it has questions for.

## Your own questions

Pipeline step 3 **overwrites** `units/<unit>.generated.json` every time it runs.
Questions written by hand therefore belong in a separate file, by convention
`units/<unit>.authored.json`, which no script ever reads or touches. List both
and they are merged per level; a hand written question is then drawn just like
a generated one.

A hand written question may carry its own `keywords`. The evaluation then checks
exactly those terms instead of deriving them from the sample answer:

```json
{
  "question": "Woran erkennen Sie, ob zwei Variablen dasselbe Objekt bezeichnen?",
  "answer": "Zwei Variablen bezeichnen dasselbe Objekt, wenn sie identisch sind …",
  "keywords": ["Identität", "Gleichheit", "Verweis"]
}
```

`courses/oop/units/ke1.authored.json` is a worked example.
`python -m courselib.validate --verbose` shows how many questions each file
contributed, so you can see your additions arrive.

## Leaving material out

Everything under `materials` is optional, and the exam does without the
capability rather than failing. The course `grundlagen-db` declares none of it
and exists to demonstrate exactly that.

| Missing | Consequence |
|---|---|
| `technical_terms` | answers are not checked for technical vocabulary, so no follow-up question is targeted at a missed topic |
| `vector_store` | no question is written from the teaching material; a predefined one is asked instead |
| `paraphrase_model` | hints are phrased by the text generation backend instead of a fine-tuned model |
| `source` | the content pipeline cannot rebuild the course, but the exam is unaffected |

`embedding_model` is required as soon as a vector store is declared. An index
built with a different encoder loads without complaint and returns unrelated
context, so the validator compares it against the model the application uses.

A short course is not a problem: when its questions run out the exam ends early
with its closing feedback.

## Checking a course

```shell
docker compose run --rm validate                        # all courses, strict
python -m courselib.validate --course oop --verbose     # one, with its units
```

The same checks run when the application starts. A broken course is logged and
left out; the others are still served. `COURSE_STRICT=true` turns that into a
refusal to start.

After adding a course that names its own `paraphrase_model`, run
`docker compose run --rm warmup` again so the model is in the cache.

## What is not a course concern

Prompts, the feedback wording, the German stop word list and the morphology
rules of the keyword matching describe the *language*, not a course, and stay
in the application. `language:` is therefore recorded but currently
informational: everything else is German, and the validator warns if a course
claims otherwise.
