"""
Class for paraphrasing questions.
"""
import logging
import os

logger = logging.getLogger(__name__)

TEMPLATE = ("Du bist ein Professor an einer deutschen Universität. "
            "Erstelle eine einfache Prüfungsfrage zu dieser Antwort: {context}")


class QuestionParaphraser:
    def __init__(self):
        """
        Initializes the question paraphraser.

        PARAPHRASE_ENGINE selects the backend:
        'local'     runs the fine-tuned question generation model of the paper
                    locally, which is how the published pipeline worked before
                    the Hugging Face inference API was shut down.
        'kiconnect' asks the general purpose text generation backend instead.
        """
        self.engine = os.getenv("PARAPHRASE_ENGINE", "local").lower()
        logger.info("Paraphrasing engine: %s", self.engine)

    def paraphrase(self, answer):
        """
        Generates a new question for a given answer.
        """
        prompt = TEMPLATE.format(context=answer)

        if self.engine == "local":
            import models
            generated = models.get_paraphraser_pipeline()(prompt, max_new_tokens=250)
            return generated[0]["generated_text"].strip()

        import llm
        return llm.chat(prompt, max_tokens=250)
