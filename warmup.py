"""
Downloads every model the exam needs into the Hugging Face cache.

Run this once before the first start, so that the first exam does not wait for
several gigabytes of downloads:

    docker compose run --rm warmup

The models land in the hf-cache volume and are reused by every later start.
"""
import logging
import os

import models
import tts

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-8s %(name)s: %(message)s")
logger = logging.getLogger("warmup")


def main():
    logger.info("Downloading the evaluation, transcription and context models ...")
    models.warmup(speech=True, paraphrase=True)

    if tts.is_server_side():
        logger.info("Downloading the Piper voice ...")
        tts.get_voice()
    else:
        logger.info("TTS_ENGINE=%s, no voice model needed.", tts.engine())

    logger.info("Done. The models are cached in %s.", os.getenv("HF_HOME", "~/.cache/huggingface"))


if __name__ == "__main__":
    main()
