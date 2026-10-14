# oral-exam-simulation

_Oral Exam Trainer_ is a speech-based dialogue system that holds a mock oral
examination with a student: it asks questions about a course, listens to the
spoken answer, evaluates it, offers help when an answer misses the point and
closes with constructive feedback. It was built for the course _Objektorientierte
Programmierung_ at the FernUniversität in Hagen and now runs any course that
brings its own content directory.

<!-- development-related badges -->

![](https://img.shields.io/badge/Python-3.11-green)
![](https://img.shields.io/badge/Flask-3.0-green)
![](https://img.shields.io/badge/Docker-compose-green)
![](https://img.shields.io/badge/Poetry-dependency_management-green)
[![MIT license](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

<!-- maturity-related badges -->

[![stability-beta](https://img.shields.io/badge/stability-beta-33bbff.svg)](https://github.com/mkenney/software-guides/blob/master/STABILITY-BADGES.md#beta)
![](https://img.shields.io/badge/research_prototype-ECTEL_2024-blue)
![](https://img.shields.io/badge/courses_included-2-blue)
![](https://img.shields.io/badge/questions_included-1292-blue)

<!-- AI-related and data-related badges -->

![](https://img.shields.io/badge/collects_audio_data-yes-blue)
![](https://img.shields.io/badge/audio_leaves_the_server-no-blue)
![](https://img.shields.io/badge/transcripts_sent_to_LLM_vendor-yes-blue)
![](https://img.shields.io/badge/speech_recognition-Whisper_(local)-blue)
![](https://img.shields.io/badge/speech_synthesis-Piper_(local)-blue)
![](https://img.shields.io/badge/text_generation-Mistral_via_KI:connect-blue)
![](https://img.shields.io/badge/human_in_the_loop-no-blue)

**Examination Dialogue**

- _Spoken question and answer_ in German, in the browser or in the terminal
- _Three difficulty levels_ per course unit, following Bloom's taxonomy
- _Adaptive follow-up_: a question is rephrased when an answer contradicts or misses
- _Targeted questions_ generated from the teaching material for topics the student missed
- _Time management_ that distributes the exam over the units of the course

**Answer Evaluation**

- _Entailment and contradiction_ detection against the sample answer
- _Semantic similarity_ scoring rather than keyword matching alone
- _Technical vocabulary check_ against the course's own term list
- _Constructive closing feedback_ phrased from the collected performance data

**Speech**

- _Transcription with Whisper_, running locally; recordings never leave the server
- _Silence detection_ from the audio level, so a muted microphone is not invented into text
- _A German voice model_ (Piper), or the voice of the viewer's browser

**Course Content**

- _Content lives outside the code_, one directory per course with a manifest
- _Several courses_ side by side, picked at the start of an exam
- _Graceful degradation_ when a course brings less material
- _Questions written by teachers_ alongside the generated ones, never overwritten

## Installation

Requires Docker. The command line variant additionally requires Python 3.11,
Poetry and PortAudio.

```shell
cp example.env .env             # fill in BASE_URL, API_KEY and MODEL
docker compose run --rm warmup  # once: downloads ~2.9 GB of models
docker compose up               # -> http://localhost:5000
```

The browser only grants microphone access over `http://localhost` or HTTPS, not
over a LAN address.

## Usage

Open <http://localhost:5000>, pick a course, enter a name and start. Recording
begins once the examiner has finished speaking and stops after three seconds of
silence. Answers can also be typed, which is useful for a demonstration without
a microphone.

In the terminal, using the local microphone:

```shell
poetry install --extras cli
poetry run python start_exam --list-courses
poetry run python start_exam -n Luna -f --course oop
```

Configuration is read from `.env`; see [example.env](./example.env) for every
option.

## Repository structure

Each part carries its own documentation:

| Directory | Contents | |
|---|---|---|
| `oral_exam/` | the application: dialogue, evaluation, speech, web interface | [readme](./oral_exam/README.md) |
| `courses/` | the content, one directory per course, no code | [readme](./courses/README.md) |
| `courselib/` | reads and validates that content | [readme](./courselib/README.md) |
| `content_pipeline/` | turns a course document into a course | [readme](./content_pipeline/README.md) |
| `finetuning/` | training scripts for the question generation models | |
| `docs/` | the roadmap, and the evaluation results of the paper | |
| `tests/` | the checks | |
| `runs/` | whatever a local run produces; not versioned | |

## Troubleshooting

- **The first start hangs for minutes.** The application runs with
  `HF_HUB_OFFLINE=1` and expects the model cache to be filled. Run
  `docker compose run --rm warmup` once, or set `HF_HUB_OFFLINE=0`.
- **`docker compose run --rm warmup` cannot reach huggingface.co.** It already
  uses the host network for that reason; on some machines a Docker bridge
  network cannot resolve or reach that host.
- **A course does not appear.** Run `docker compose run --rm validate`; a broken
  manifest is skipped at start-up and reported under `/api/health`.
- **No microphone in the browser.** Use `http://localhost`, not a LAN address.
- **The examiner reads out whole exam tasks.** The course declares no
  `paraphrase_model`, so hints come from the chat backend; see
  [courses/README.md](./courses/README.md).

## Testing

The checks under `tests/` are plain scripts, each printing one line per
assertion and exiting non-zero on failure. Those that need the models run inside
the container, those that drive the HTTP API run against it:

```shell
docker compose exec -T exam python -m tests.test_channel
python tests/test_dialogue_http.py
docker compose run --rm validate          # every course manifest
poetry run ruff check .
```

Single components can be exercised without holding a whole exam:

```shell
docker compose run --rm exam python -m oral_exam.diagnostics -c oop -m qa_selection
```

## Contributing

The application is a Python package; content is data and never code. Before
opening a pull request, run `ruff check .`, the test scripts above and the
course validator. Adding a course means adding a directory under `courses/` —
see [courses/README.md](./courses/README.md); it should not require a code
change, and if it does, that is the bug to report.

## Credits

This software uses the following open source models and packages:
[Whisper](https://github.com/openai/whisper),
[Piper](https://github.com/OHF-Voice/piper1-gpl),
[Bark](https://github.com/suno-ai/bark),
[sentence-transformers](https://www.sbert.net/),
[transformers](https://huggingface.co/docs/transformers),
[FAISS](https://github.com/facebookresearch/faiss),
[LangChain](https://www.langchain.com/),
[Flask](https://flask.palletsprojects.com/).

Text generation runs on [KI:connect](https://chat.kiconnect.nrw/), the language
model service of the state of North Rhine-Westphalia.

## Citation

**Cite this software:**

```bibtex
@inproceedings{Seidel2024-OralExamTrainer,
	title = {A Speech-based Dialogue System for Training Oral Examinations},
	booktitle = {Proceedings of the 19th European Conference on Technology Enhanced Learning (EC-TEL)},
	author = {Seidel, Niels and Hammesfahr, Luna},
	year = {2024},
	keywords = {oral examination, speech-based dialogue system},
}
```

## Research articles about the Oral Exam Trainer

- Seidel, N., & Hammesfahr, L. (2024). A Speech-based Dialogue System for
  Training Oral Examinations. _Proceedings of the 19th European Conference on
  Technology Enhanced Learning (EC-TEL)._

The measurements behind the paper are kept unchanged in
[docs/evaluation/](./docs/evaluation/README.md).

## You may also like ...

- [mod_longpage](https://github.com/CATALPAresearch/mod_longpage) — Moodle plugin for reading and annotating long course texts
- [mod_hypercast](https://github.com/nise/mod_hypercast) — hyperaudio player for course texts
- [format_serial3](https://github.com/catalparesearch/format_serial3) — learning analytics dashboard for Moodle courses

## Contributors

- Luna Hammesfahr (original development)
- Niels Seidel (project lead)

## Licence

[MIT](./LICENSE)

---

<a href="https://www.fernuni-hagen.de/english/research/clusters/catalpa/">CATALPA</a> ·
<a href="https://www.fernuni-hagen.de/">FernUniversität in Hagen</a>
