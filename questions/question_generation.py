"""
Class for generating questions.
"""
import logging
import re

import llm
import models

logger = logging.getLogger(__name__)

# The model is asked for 'Frage: ... / Antwort: ...', but instruction tuned
# models like to decorate that ("**Frage:**") or to add a preamble, so the
# labels are matched instead of split on positionally. They are anchored to the
# start of a line, otherwise a preamble like "Hier ist eine Pruefungsfrage:"
# would be mistaken for the label.
QUESTION_PATTERN = re.compile(r"^[ \t>*\-]*Frage[ \t*]*:[ \t]*(.+?)[ \t]*$",
                              re.IGNORECASE | re.MULTILINE)
ANSWER_PATTERN = re.compile(r"^[ \t>*\-]*Antwort[ \t*]*:[ \t]*(.+?)(?=\n[ \t]*\n|\Z)",
                            re.IGNORECASE | re.MULTILINE | re.DOTALL)


def get_query(context):
    query = f"""Erstelle eine Prüfungsfrage und ihre Musterantwort für eine mündliche Prüfung.
    Schreibe die Musterantwort in 1 Satz.
    Nutze nur Informationen aus folgendem Text:
    {context}

    Passe die Ausgabe an folgendes Template an:
    Frage: [Prüfungsfrage]
    Antwort: [Musterantwort]"""

    return query


def parse_question_answer(generated_text):
    """
    Extracts the question and the sample answer from the model output.
    Returns None if the output does not hold both.
    """
    question_match = QUESTION_PATTERN.search(generated_text)
    answer_match = ANSWER_PATTERN.search(generated_text)
    if not question_match or not answer_match:
        logger.warning("Could not find a question and an answer in: %r", generated_text)
        return None

    question = question_match.group(1).strip().strip('*').strip()
    answer = ' '.join(answer_match.group(1).split()).strip('*').strip()
    if not question or not answer:
        logger.warning("Question or answer was empty in: %r", generated_text)
        return None

    return {'question': question, 'answer': answer}


class QuestionGenerator:
    def __init__(self, text_generator):
        """
        Sets the text generation model. The vector store and its embeddings are
        shared across exams, see models.py.
        """
        self.question_generator = text_generator

    @property
    def db(self):
        return models.get_vectorstore()

    def generate_question_answer(self, keyword, k=2):
        """
        Generates a question-answer pair for the context from the given keyword.
        Returns None if no usable pair could be generated, so that the caller
        can fall back to a predefined question.
        """
        # Get a context for the keyword
        context = self.get_context(keyword, k)
        logger.debug("Context: %s", context)
        if not context:
            logger.warning("No context found for keyword '%s'.", keyword)
            return None

        # Generate a question and answer from the context
        try:
            question_answer = self.question_generator.get_text(get_query(context))
        except llm.LLMError as error:
            logger.warning("Question generation failed: %s", error)
            return None

        question_dict = parse_question_answer(question_answer)
        if question_dict:
            logger.debug("Question: %s / Answer: %s", question_dict['question'], question_dict['answer'])
        return question_dict

    def get_context(self, query, k):
        """
        Retrieves the k most fitting context documents for the given query.
        Returns the concatenated context.
        """
        # Get context for query
        context_docs = self.db.similarity_search(query, k=k)
        # Skip documents that start with a chapter number instead of prose
        context_docs = [doc for doc in context_docs if doc.page_content and not doc.page_content[0].isdigit()]

        return ' '.join(doc.page_content for doc in context_docs)
