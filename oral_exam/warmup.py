"""
Downloads every model the exam needs into the Hugging Face cache.

Run this once before the first start, so that the first exam does not wait for
several gigabytes of downloads:

    docker compose run --rm warmup

The models land in the hf-cache volume and are reused by every later start.
"""
import logging
import os

from oral_exam import models
from oral_exam.audio import synthesis

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-8s %(name)s: %(message)s")
logger = logging.getLogger("warmup")


def main():
    import courselib

    courses = courselib.all_courses()
    logger.info("Courses found: %s", ", ".join(course.id for course in courses) or "none")
    for broken_id, problems in courselib.errors().items():
        logger.error("Course '%s' was skipped: %s", broken_id, "; ".join(problems))

    logger.info("Downloading the evaluation, transcription and context models ...")
    models.warmup(speech=True, paraphrase=True)

    if synthesis.is_server_side():
        logger.info("Downloading the Piper voice ...")
        synthesis.get_voice()
    else:
        logger.info("TTS_ENGINE=%s, no voice model needed.", synthesis.engine())

    logger.info("Done. The models are cached in %s.", os.getenv("HF_HOME", "~/.cache/huggingface"))


if __name__ == "__main__":
    main()
