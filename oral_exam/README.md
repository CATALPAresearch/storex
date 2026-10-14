# oral_exam — the application

Everything that holds an examination. Course content is *not* here; it lives in
[`courses/`](../courses/README.md) and is read by
[`courselib/`](../courselib/README.md).

## How an exam runs

`ExamManager` (`exam.py`) is the conversation. It loops until the clock runs
out, and in each turn it decides which kind of question to ask next:

| Question type | When |
|---|---|
| `PREDEFINE` | default: the next question from the course's pool |
| `GENERATE` | the answer was incomplete: a new question is written from the teaching material about a topic the student missed |
| `REPEAT` | the answer contradicted or went off topic: the same question, rephrased |
| `SELECTED` | a predefined question is picked that covers a missed topic |

The decision is made in `get_evaluation()` from the result of the evaluation,
and the question is then asked through two methods — and those two are the only
places where the exam touches the outside world:

```python
ExamManager.speak(text)    # everything the examiner says
ExamManager.get_answer()   # everything the student answers
```

That is what lets the same conversation run in a terminal and in a browser
without a second implementation of the dialogue.

### The two front ends

**Command line** (`start_exam` in the repository root): `speak()` prints and
plays audio through the local speakers, `get_answer()` records from the local
microphone. Needs the `cli` extra (PortAudio, ALSA).

**Web** (`web/`): `ExamManager` is handed a `Channel` and runs in a background
thread, one per browser session. The channel replaces terminal and microphone:

```
browser ──POST /api/answer──▶ transcription ──▶ Channel.submit() ──▶ get_answer()
browser ◀──GET /api/events─── event log     ◀── Channel.say()    ◀── speak()
```

The outbound side is an append-only event log rather than a queue, because the
thread must also report that it finished or failed, and because a retried poll
or a page reload must not lose an utterance. `web/runner.py` turns every
outcome of the thread into an event; nothing is allowed to escape silently.

## Modules

| Module | Responsibility |
|---|---|
| `exam.py` | the conversation, the question types, `TimeManager` |
| `evaluation.py` | scores an answer: entailment, similarity, technical vocabulary |
| `feedback.py` | collects performance data and phrases the closing feedback |
| `text_generation.py` | the examiner persona around the text generation backend |
| `llm.py` | the backend client (KI:connect, OpenAI-compatible) |
| `models.py` | loads the machine learning models once and shares them |
| `ai_student.py` | answers in place of a person, for testing without a microphone |
| `diagnostics.py` | runs one component on its own |
| `warmup.py` | downloads every model into the cache |
| `audio/` | microphone, transcription, synthesis, playback |
| `questions/` | question generation, paraphrasing, the question manager |
| `utils/` | helpers, German text preprocessing, colours, paths |
| `resources/` | the German stop word list: language, not course |
| `web/` | Flask app, session bridge, and the single page under `static/` |

### Audio, four modules with four jobs

The names say which side they are on. Two of them synthesize speech, and it is
worth keeping them apart:

| Module | Direction | Used by |
|---|---|---|
| `audio/microphone.py` | records from the local microphone | command line only |
| `audio/transcription.py` | Whisper: audio → text | both |
| `audio/synthesis.py` | Piper: text → WAV for the browser | web |
| `audio/playback.py` | Bark: text → the local speakers | command line only |

Silence is detected from the **audio level**, not from the transcript: Whisper
does not answer silence with nothing, it invents a plausible sentence, and that
sentence is not predictable. The threshold is the one the microphone path uses.

## Shared models

`models.py` is a small registry of lazily built singletons behind a reentrant
lock. The models are stateless at inference time, so every exam in the process
shares them — which is what keeps roughly 1.6 GB of weights in memory once
rather than per session.

```python
models.get_evaluator()          # similarity + entailment
models.get_speech_recognition() # Whisper
models.get_vectorstore(course)  # per course, None when the course has none
models.get_paraphraser_pipeline(name)
```

`warmup()` loads them at start-up; without it the first exam request would
block for minutes. A per-course model that cannot be loaded is logged and the
exam continues without that capability.

## What is per course and what is shared

| | Scope |
|---|---|
| question pools, unit titles, technical terms, vector store, paraphrase model | **course** |
| prompts, feedback wording, German morphology, stop words, Bloom levels | **language and pedagogy**, shared |
| the models themselves | **process**, shared |

The technical terms are passed into `evaluation.evaluate_keywords()` as an
argument rather than read from a module global. That is deliberate: with two
exams running on different courses, a global would let one course's vocabulary
score the other's answers.

## Entry points

```shell
gunicorn oral_exam.web.app:app        # the web app, one worker, several threads
python -m oral_exam.warmup            # fill the model cache
python -m oral_exam.diagnostics -c oop -m qa_selection
python start_exam -n Luna --course oop   # from the repository root
```

One worker on purpose: sessions and models live in process memory, so a second
worker would duplicate the weights and would not find the first one's sessions.
