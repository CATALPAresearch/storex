"""
Class of a text generator.
"""
from oral_exam import llm


class TextGenerator:
    """
    Class of a text generator.

    Wraps every query in the examiner persona and sends it to the configured
    text generation backend (see llm.py).
    """
    PERSONA = ("Du bist ein Professor an einer deutschen Universität. "
               "Du hältst online mündliche Prüfungen ab.")

    def get_text(self, query):
        """
        Generates text for the given query.

        :raises llm.LLMError: if the text generation backend is unavailable.
        """
        return llm.chat(f"{self.PERSONA}\n{query}")
