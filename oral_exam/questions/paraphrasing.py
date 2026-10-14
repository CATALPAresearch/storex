"""
Class for paraphrasing questions.
"""
import logging
import os
import re

logger = logging.getLogger(__name__)

# Prompt of the published pipeline, used with the fine-tuned model
TEMPLATE = ("Du bist ein Professor an einer deutschen Universität. "
            "Erstelle eine einfache Prüfungsfrage zu dieser Antwort: {context}")

# The fine-tuned model answers with the bare question. A general purpose chat
# model does not: left to itself it returns a whole exam task with a model
# answer and grading criteria, which the examiner would then read out to the
# student. So it is asked much more narrowly, and the reply is cut back to the
# question itself.
LLM_TEMPLATE = (
    "Du bist ein Professor an einer deutschen Universität und hältst eine mündliche Prüfung ab.\n"
    "Formuliere genau eine kurze Prüfungsfrage, die auf die folgende Antwort abzielt.\n"
    "Gib ausschließlich die Frage aus: keine Antwort, keine Begründung, keine Aufzählung, "
    "keine Formatierung, keine Anrede.\n\n"
    "Antwort: {context}")

LABEL_PATTERN = re.compile(r"^\W*(prüfungs)?frage\s*\d*\s*[:.\-]\s*", re.IGNORECASE)


def first_question(text):
    """
    Reduces a chat model's reply to the question it was asked for.

    Returns the first sentence ending in a question mark; if there is none, the
    first non-empty line. Markdown emphasis and labels such as
    'Prüfungsfrage:' are stripped.
    """
    if not text:
        return ""
    cleaned = text.replace("*", "").replace("#", "").replace("`", "")

    for line in cleaned.splitlines():
        line = LABEL_PATTERN.sub("", line.strip()).strip()
        if not line:
            continue
        if "?" in line:
            # Keep only up to the first question mark: a model likes to add
            # "Erläutern Sie ..." after it
            return line[:line.index("?") + 1].strip()
        return line

    return cleaned.strip()


class QuestionParaphraser:
    def __init__(self, course):
        """
        Initializes the question paraphraser.

        PARAPHRASE_ENGINE selects the backend:
        'local'     runs the fine-tuned question generation model the course
                    declares, which is how the published pipeline worked before
                    the Hugging Face inference API was shut down.
        'kiconnect' asks the general purpose text generation backend instead.

        A course that declares no model of its own falls back to the backend
        rather than borrowing another course's model: a question generator
        fine-tuned on one subject phrases confident nonsense about another.
        """
        self.engine = os.getenv("PARAPHRASE_ENGINE", "local").lower()
        self.model = course.materials.paraphrase_model
        if self.engine == "local" and not self.model:
            logger.info("Course %s declares no paraphrase model; hints come from the "
                        "text generation backend.", course.id)
            self.engine = "kiconnect"
        logger.info("Paraphrasing engine: %s", self.engine)

    def paraphrase(self, answer):
        """
        Generates a new question for a given answer.
        """
        if self.engine == "local":
            import models
            generated = models.get_paraphraser_pipeline(self.model)(
                TEMPLATE.format(context=answer), max_new_tokens=250)
            return generated[0]["generated_text"].strip()

        import llm
        return first_question(llm.chat(LLM_TEMPLATE.format(context=answer), max_tokens=250))
