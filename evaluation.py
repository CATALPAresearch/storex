"""
File for answer evaluation.
"""
import logging
import re

from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
from utils import preprocessing
from utils.helpers import EvaluationType

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

    def evaluate_keywords(self, question, student_answer):
        """
        Checks if the given students answer contains the given keywords and returns the missing topics.
        """
        # Get keywords from predefined and generated answers
        if 'keywords' not in question:
            keywords = preprocessing.extract_keywords(question['answer'])
        else:
            keywords = question['keywords']
        logger.info(f"Keywords from answer: {keywords}")

        mentioned_words = preprocessing.extract_keywords(student_answer, keywords)
        logger.info(f"Mentioned terms: {mentioned_words}")

        missing_words = list(set(keywords)-set(mentioned_words))
        missing_words = [term if not isinstance(term, list) else term[0] for term in missing_words]

        # Check the mention of common keywords in the students answer by searching for the preprocessed keywords
        # processed_answer = preprocessing.preprocess_text(student_answer)
        # missing_keys = []
        # if 'common' in keywords:
        #     for word in keywords['common']:
        #         processed_word = preprocessing.preprocess_text(word)
        #         if processed_word not in processed_answer:
        #             missing_keys.append(word)
        #             logger.info(f"Common keyword '{word}' not found!")

        # Check if common keywords are indirectly mentioned in the students answer by checking the accuracy with which
        # the students answer hits the topics represented by the word
        # if missing_keys:
        #     accuracy = self.check_accuracy(missing_keys, student_answer)
        #     # Add missing topics under the threshold of accuracy
        #     for topic in accuracy:
        #         if topic[1] < 0.75:
        #             missing_topics.append(topic[0])

        logger.info(f"Missing terms: {missing_words}")
        return missing_words, len(keywords)

    def evaluate_answer(self, correct_answer, student_answer):
        """
        Compares the given students answer with the given correct answer.
        Returns feedback.
        """
        feedback = None

        # Check the congruity of the answer via text classification (MNLI)
        congruity = self.check_congruity(correct_answer, student_answer)
        if congruity[0]['label'] != 'ENTAILMENT':
            # Set OFF_TOPIC for neutral entailment
            if congruity[0]['label'] == 'NEUTRAL':
                feedback = EvaluationType.OFF_TOPIC
            # Set CONTRADICTS for contradicting entailment
            if congruity[0]['label'] == 'CONTRADICTION':
                feedback = EvaluationType.CONTRADICTS
            return feedback

        # Check the similarity with similarity search LLM
        similarity = self.check_similarity(correct_answer, student_answer)
        if similarity > 0.85:
            feedback = EvaluationType.CORRECT
        else:
            feedback = EvaluationType.MISSING_TOPIC
        return feedback

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
