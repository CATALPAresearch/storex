# Web app for the oral exam simulation.
#
# Python 3.11, because torch 2.0.1 publishes no wheels for 3.12 and newer.
# No PortAudio or ALSA is installed: the microphone lives in the browser, and
# pyaudio and simpleaudio are declared as the optional 'cli' extra, so they are
# not part of this image.
FROM python:3.11-slim-bookworm

WORKDIR /app

# ffmpeg decodes the browser recordings for the transcription pipeline,
# curl serves the health check.
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

# Dependencies first, so that a code change does not reinstall torch
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --only main --no-root

COPY . .

ENV PYTHONPATH=/app \
    PYTHONUNBUFFERED=1 \
    HF_HOME=/cache/huggingface \
    OUTPUT_DIR=/app/output \
    OMP_NUM_THREADS=2

RUN mkdir -p /cache/huggingface /app/output

EXPOSE 5000

# One worker on purpose: the exam sessions and the loaded models live in process
# memory, so a second worker would duplicate several GB of weights and would not
# find the sessions of the first. Threads serve the concurrent long-polls.
# The timeout has to exceed POLL_TIMEOUT.
CMD ["gunicorn", "app:app", \
     "--bind", "0.0.0.0:5000", \
     "--workers", "1", \
     "--threads", "8", \
     "--timeout", "120", \
     "--graceful-timeout", "30", \
     "--access-logfile", "-"]
