"""
File for answer evaluation.
"""
import logging

from sentence_transformers import util

import models

from utils import preprocessing
from utils.helpers import EvaluationType

logger = logging.getLogger(__name__)

# Above this cosine similarity a students answer counts as correct.
SIMILARITY_THRESHOLD = 0.85


class Evaluator:
    """
    Class which evaluates given answers by finding contradictions, checking the similarity, and finding missing topics.

    The models are shared across exams, see models.py.
    """
    def __init__(self):
        self.similarity_model = models.get_similarity_model()
        self.congruity_pipeline = models.get_congruity_pipeline()

    def evaluate_keywords(self, question, student_answer):
        """
        Checks if the given students answer contains the given keywords and returns the missing topics.
        """
        # Get keywords from predefined and generated answers
        if 'keywords' not in question:
            keywords = preprocessing.extract_keywords(question['answer'])
        else:
            keywords = question['keywords']
        logger.info("Keywords from answer: %s", keywords)

        mentioned_words = preprocessing.extract_keywords(student_answer, keywords)
        logger.info("Mentioned terms: %s", mentioned_words)

        # extract_keywords reports preprocessed labels, while the keywords of a
        # question are written in prose ("dynamisch Binden"), so the comparison
        # runs over the labels while the readable spelling is kept for the report.
        missing_words = []
        for term in keywords:
            spellings = term if isinstance(term, list) else [term]
            if preprocessing.term_label(term) not in mentioned_words:
                missing_words.append(spellings[0])

        logger.info("Missing terms: %s", missing_words)
        return missing_words, len(keywords)

    def evaluate_answer(self, correct_answer, student_answer):
        """
        Compares the given students answer with the given correct answer.
        Returns feedback.
        """
        # Check the congruity of the answer via text classification (MNLI)
        label = self.check_congruity(correct_answer, student_answer)[0]['label'].upper()

        if label != 'ENTAILMENT':
            if label == 'CONTRADICTION':
                return EvaluationType.CONTRADICTS
            # Neutral entailment means the answer did not address the question.
            # Any unexpected label is treated the same way, so that an unknown
            # label can never be returned as None.
            if label != 'NEUTRAL':
                logger.warning("Unexpected classifier label '%s', treating it as off-topic.", label)
            return EvaluationType.OFF_TOPIC

        # Check the similarity with similarity search LLM
        similarity = self.check_similarity(correct_answer, student_answer)
        if similarity > SIMILARITY_THRESHOLD:
            return EvaluationType.CORRECT
        return EvaluationType.MISSING_TOPIC

    def check_similarity(self, correct_answer, student_answer):
        """
        Finds the semantic similarity between the given answers.
        Returns the similarity between both answers as a float.
        """
        # Compute embeddings for both answers
        c_embedding = self.similarity_model.encode(correct_answer, convert_to_tensor=True)
        s_embedding = self.similarity_model.encode(student_answer, convert_to_tensor=True)
        # Calculate similarity
        similarity = util.pytorch_cos_sim(c_embedding, s_embedding).item()
        logger.info("Similarity: %s", similarity)
        return similarity

    def check_congruity(self, correct_answer, student_answer):
        """
        Checks if the concatenated given answers contain a contradiction or entail each other.
        Returns entailment, neutral or contradiction label.
        """
        # Check entailment in concatenated answers
        congruity = self.congruity_pipeline(correct_answer + student_answer)
        logger.info("Congruity: %s", congruity)
        return congruity
