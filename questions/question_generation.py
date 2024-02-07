"""
Class for generating questions.
"""
import os
import torch

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

import logging
logger = logging.getLogger()


# TODO: Remove api token
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


def get_query(context):
    query = f"""Erstelle eine Prüfungsfrage und ihre Musterantwort für eine mündliche Prüfung.
    Nutze nur Informationen aus folgendem Text:
    {context}

    Passe die Ausgabe an folgendes Template an:
    Frage: [Prüfungsfrage]
    Antwort: [Musterantwort]"""

    return query


class QuestionGenerator:
    def __init__(self, text_generator):
        """
        Initializes the vector store and sets the text generation model.
        """
        # Load vectorstore embeddings
        directory = os.path.dirname(os.path.dirname(__file__))
        vectorstore = (os.path.join(directory, 'data/vectorStore'))
        device = "cuda" if torch.cuda.is_available() else "cpu"
        embedding_model = HuggingFaceEmbeddings(model_name='paraphrase-multilingual-MiniLM-L12-v2',
                                                model_kwargs={'device': device})
        # Load database
        self.db = FAISS.load_local(vectorstore, embedding_model)

        # Load question-answer model and create a question-answer chain
        self.question_generator = text_generator

    def generate_question_answer(self, keyword, k=2):
        """
        Generates a question-answer pair for the context from the given keyword.
        """
        # Get a context for the keyword
        context = self.get_context(keyword, k)
        logger.debug(f"Context: {context}")

        # Generate a question and answer from the context
        question_query = get_query(context)
        question_answer = self.question_generator.get_text(question_query)
        logger.debug(f"Question and answer: {question_answer}")

        # Find the question and the answer in the model output
        question_line = question_answer.split('\n', 1)[0]
        question = question_line.split(': ')[1].strip()
        answer_lines = question_answer.split('\n', 1)[1]
        answer = answer_lines.split(': ')[1].strip()

        question_dict = {'question': question, 'answer': answer}
        return question_dict

    def get_context(self, query, k):
        """
        Retrieves the k most fitting context documents for the given query.
        Returns the concatenated context.
        """
        # Get context for query
        context_docs = self.db.similarity_search(query, k=k)
        context_docs = [docs for docs in context_docs if not docs.page_content[0].isdigit()]
        # TODO: Process context?

        context = ' '.join([doc.page_content for doc in context_docs])
        return context
