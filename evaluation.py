"""
File for answer evaluation.
"""
import logging
import re

from feedback_managing import FeedbackManager
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
from utils import preprocessing
from utils.helpers import FeedbackType

logger = logging.getLogger()


class Evaluator:
    """
    Class which evaluates given answers by finding contradictions, checking the similarity, and finding missing topics.
    """
    def __init__(self):
        """
        Initializes the similarity and classifier models used for answer evaluation.
        """
        # Load a sentence similarity model
        self.similarity_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")  # 'LLukas22/all-MiniLM-L12-v2-embedding-all'

        # Load a classifier model, try morit/xlm-t-roberta-base-mnli-xnli?
        classifier_model = "symanto/xlm-roberta-base-snli-mnli-anli-xnli"
        self.congruity_pipeline = pipeline("text-classification", model=classifier_model, truncation=True)
        self.accuracy_pipeline = pipeline("zero-shot-classification", model=classifier_model, truncation=True)

        # Set Feedback Manager
        self.feedback = FeedbackManager()

    def evaluate_keywords(self, keywords, student_answer):
        """
        Checks if the given students answer contains the given keywords and returns the missing topics.
        """
        processed_answer = preprocessing.preprocess_text(student_answer)
        missing_keys = []
        missing_topics = []

        # Check the mention of technical terms in the students answer
        for term in keywords:
            pattern = re.compile(fr"\b{re.escape(term)}(?:\b|\w*en\b|\w*em\b|\w*es\b|\w*s\b|)?", re.IGNORECASE)
            matches = re.findall(pattern, processed_answer)
            if not matches:
                missing_keys.append(term)
        logger.info(f"Missing terms: {missing_keys}")
        # Add information about number of missed terms to feedback
        self.feedback.missed_terms(len(missing_topics))

        # Check the mention of common keywords in the students answer by searching for the preprocessed keywords
        # if 'common' in keywords:
        #     for word in keywords['common']:
        #         processed_word = preprocessing.preprocess_text(word)
        #         if processed_word not in processed_answer:
        #             missing_keys.append(word)
        #             logger.info(f"Common keyword '{word}' not found!")

        # Check if common keywords are indirectly mentioned in the students answer by checking the accuracy with which
        # the students answer hits the topics represented by the word
        if missing_keys:
            accuracy = self.check_accuracy(missing_keys, student_answer)
            # Add missing topics under the threshold of accuracy
            for topic in accuracy:
                if topic[1] < 0.5:  # TODO: What is a good threshold for accuracy?
                    missing_topics.append(topic[0])

        logger.info(f"Missing topics: {missing_topics}")
        return missing_topics

    def evaluate_answer(self, correct_answer, student_answer):
        """
        Compares the given students answer with the given correct answer.
        Returns feedback.
        """
        feedback = None
        # Check for silence, which is turned into a short sentence by speech recognition LLMs (TODO: Move to ASR)
        if len(student_answer) < 20:  # TODO: Understand sentences like "Ich weiß es nicht." oder "Sinnfreie Frage."
            feedback = FeedbackType.SILENCE
            return feedback

        # Check the congruity of the answer via text classification (MNLI)
        congruity = self.check_congruity(correct_answer, student_answer)
        if congruity[0]['label'] != 'ENTAILMENT':
            # Set OFF_TOPIC for neutral entailment
            if congruity[0]['label'] == 'NEUTRAL':
                feedback = FeedbackType.OFF_TOPIC
            # Set CONTRADICTS for contradicting entailment
            if congruity[0]['label'] == 'CONTRADICTION':
                feedback = FeedbackType.CONTRADICTS
            return feedback

        # Check the similarity with similarity search LLM
        similarity = self.check_similarity(correct_answer, student_answer)
        if similarity > 0.75:  # TODO: What similarity is similar??
            feedback = FeedbackType.CORRECT
        else:
            feedback = FeedbackType.MISSING_TOPIC
        return feedback

        # TODO: Identify concrete mistakes (factual inaccuracy, missing information, structural issues)

    def check_similarity(self, correct_answer, student_answer):
        """
        Finds the semantic similarity between the given answers.
        Returns the similarity between both answers.
        """
        # Compute embeddings for both answers
        c_embedding = self.similarity_model.encode(correct_answer, convert_to_tensor=True)
        s_embedding = self.similarity_model.encode(student_answer, convert_to_tensor=True)
        # Calculate similarity
        similarity = util.pytorch_cos_sim(c_embedding, s_embedding)
        logger.info(f"Similarity: {similarity}")
        return similarity

    def check_congruity(self, correct_answer, student_answer):
        """
        Checks if the concatenated given answers contain a contradiction or entail each other.
        Returns entailment, neutral or contradiction lable.
        """
        # Check entailment in concatenated answers
        congruity = self.congruity_pipeline(correct_answer + student_answer)
        logger.info(f"Congruity: {congruity}")
        return congruity

    def check_accuracy(self, keys, student_answer):
        """
        Checks if the given keywords are accurately represented in the given students answer.
        Returns the accuracy.
        """
        # Check the accuracy of the keys for the student answer
        accuracy_scores = self.accuracy_pipeline(student_answer, keys)
        accuracy = list(zip(accuracy_scores.get('labels'), accuracy_scores.get('scores')))
        logger.info(f"Accuracy per keyword: {accuracy}")

        return accuracy
