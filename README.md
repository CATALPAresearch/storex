# Dialogue system as a trainer for oral exams
## Course: Object-oriented Programming

The system holds a spoken oral exam with a student: it asks questions about the
course material, evaluates the answers, offers help when an answer misses the
point and closes with constructive feedback.

There are two ways to run it:

| | Web app | Command line |
|---|---|---|
| Start | `docker compose up` | `poetry run python start_exam -n <name>` |
| Microphone | in the browser | local microphone |
| Examiner's voice | browser voice or Piper | Bark (`suno/bark-small`) |
| Runs in a container | yes | no, needs PortAudio and ALSA |

A container has no access to the microphone of the host, which is why the web
app records in the browser and sends the audio to the server.

---

## Web app

### Preparation

1. Change into the directory:
   `cd oral-exam-simulation`
2. Copy the configuration and fill in the API key of the text generation
   backend:
   `cp example.env .env`
   The relevant values are `BASE_URL`, `API_KEY` and `MODEL`, see
   [Text generation](#text-generation).
3. Download the models once:
   `docker compose run --rm warmup`
   They are stored in the `oral-exam-hf-cache` volume, and every later start
   loads them from there in a few seconds. This step is required, because the
   app itself runs with `HF_HUB_OFFLINE=1` and does not download anything; set
   `HF_HUB_OFFLINE=0` in `.env` if you would rather have it fetch what is
   missing by itself.

   The warmup uses the host network on purpose: a container on a bridge network
   cannot reach `huggingface.co` on every machine.

### Execution

```
docker compose up
```

Then open **http://localhost:5000**, enter a name and start the exam.

`curl localhost:5000/api/health` reports whether the models are loaded
(`ready`) and whether the text generation backend is configured
(`llm_configured`).

The browser only grants access to the microphone in a secure context.
`http://localhost` counts as one, an address in the local network does not, so
reaching the app from another device needs HTTPS in front of it.

Recording starts by itself once the examiner has finished speaking and stops
after three seconds of silence, the same rule the command line version applies.
Answers can also be typed, which is useful for a demonstration without a
microphone.

### Configuration

Everything is set in `.env`, see `example.env` for the full list.

| Variable | Meaning |
|---|---|
| `BASE_URL`, `API_KEY`, `MODEL` | text generation backend, OpenAI compatible |
| `TTS_ENGINE` | `browser` (default) or `piper` |
| `PARAPHRASE_ENGINE` | `local` (default) or `kiconnect`, see below |
| `MAX_SESSIONS` | parallel exams, default 2 |
| `ANSWER_TIMEOUT` | seconds to wait for an answer before it counts as silence |
| `DISABLE_LLM` | `true` answers from a canned string, for working on the page |
| `HF_HUB_OFFLINE` | `1` (default) runs from the model cache, `0` allows downloads |

---

## Command line

The command line exam uses the local microphone and speakers, so it needs
PortAudio and ALSA and is installed with the `cli` extra.

```
poetry install --extras cli
poetry run python start_exam -n Luna -f
```

On macOS PortAudio comes from Homebrew: `brew install portaudio`.

This argument is mandatory:
```
-n <name> | --name <name>    with <name> being the name which is used during the oral
                             exam simulation
```

The following arguments are optional:
```
-t <time> | --time <time> whereas <time> is the time for the exam training.
                          Default: 25.
-f | --female             set a female voice for the speaker
-m | --male               set a male voice for the speaker

--ai                      let a simulated student answer instead of you.
                          Implies --mute and needs no microphone.
-h | --help               display this help text

--log                     activate logging
--mute                    mute audio output
```

An example is the following: `poetry run python start_exam -n Luna -f`

After starting the exam, answer each question, when the red text
***Recording started*** appears. Each recording stops after three seconds of
silence or with a keyboard interrupt.

---

## Text generation

Greeting, generated questions, hints, feedback and goodbye come from a text
generation backend with an OpenAI compatible API, configured through `BASE_URL`,
`API_KEY` and `MODEL`. The project uses the Mistral-small model provided by
KI:connect.

The published version called the Hugging Face inference API at
`api-inference.huggingface.co`. That host has been shut down and no longer
resolves, so this path was replaced; `llm.py` holds the client.

Everything else runs locally in the container:

| Model | Purpose | Size |
|---|---|---|
| `paraphrase-multilingual-MiniLM-L12-v2` | answer similarity and context search | ~470 MB |
| `symanto/xlm-roberta-base-snli-mnli-anli-xnli` | entailment and contradiction | ~1.1 GB |
| `openai/whisper-base` | transcription | ~290 MB |
| `LunaticTanuki/oop-de-qg-flan-t5-base-v6` | paraphrasing for hints | ~1 GB |
| `de_DE-thorsten-medium` | Piper voice, only with `TTS_ENGINE=piper` | ~60 MB |

`PARAPHRASE_ENGINE` decides how hints are generated. `local` runs the
fine-tuned question generation model of the paper, which is how the published
pipeline worked; `kiconnect` asks the text generation backend instead.

---

## Content of the repository

- The main folder contains the web app ***app.py***, the start script
  ***start_exam***, the exam manager, the evaluation manager, the feedback
  manager, the text generation client ***llm.py***, the shared model registry
  ***models.py*** and the test script ***invoke_submodules.py***.
- The ***web*** folder bridges the exam conversation to HTTP: the channel, the
  session registry and the thread the exam runs in.
- The ***static*** folder contains the single page of the web app.
- The ***audio*** folder contains the Input Decoder and Output Decoder
  components; ***audio/microphone.py*** is only used by the command line exam.
- The ***questions*** folder contains the components for question generation,
  assistance generation and the question manager.
- The ***utils*** folder contains helpers and functions for pre-processing
  scripts for the dialog system.
- The ***finetuning*** folder contains scripts for fine-tuning the T5 and
  Flan-T5 models.
- The ***data*** folder contains the raw and post-processed teaching materials,
  lists of technical terms, training data sets and vector databases.
- The ***dataprocessing*** folder contains scripts for data processing.
- The ***testing*** folder contains test results of the evaluation of the dialog
  system. Transcripts of new runs are written to ***output***.

## Testing the components separately

`invoke_submodules.py` runs one component at a time, which is the quickest way
to check a change:

```
docker compose run --rm exam python invoke_submodules.py -m qa_selection
```

`qa_selection`, `evaluation`, `qa_generation`, `paraphrasing`, `feedback` and
`other_prompts` need no microphone. `speech_recognition` and `text_to_speech` do
and therefore only work outside the container.

## Minimal system requirements

Python 3.11. Newer versions do not work: `torch` 2.0.1 publishes no wheels for
3.12 and above.

The dialogue system has been tested with
* Ubuntu 22.04.3 LTS, 32 GB Memory, AMD® Ryzen 7 5800x 8-core processor × 16, NVIDIA Corporation GP107 (GeForce GTX 1050 Ti)
* MacOS 14.4.1, Apple M1 (2020), MacBookPro, 16 GB Memory, 8 CPU cores, 8‑Core GPU, 16‑Core Neural Engine
* Docker on macOS 15, Apple Silicon, with the web app

Two parallel exams need roughly 4 GB of memory for the shared models.

# Roadmap
* describe how content integration works
* install GPU support for mac: https://github.com/ggerganov/whisper.cpp
