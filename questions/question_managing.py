"""
Class for managing predefined questions.
"""
import logging
import random
import questions.questions as questions

from utils.helpers import KE

logger = logging.getLogger()


# TODO: Predefine questions and their probabilities
class QuestionManager:
    def __init__(self, topic_manager):
        self.topic_manager = topic_manager

        self.question_list = []
        self.topic_list = []
        self.coverage = []
        for i in KE:
            # Append all questions per KE into the list of questions
            ke_questions = f"{i.name}_questions"
            self.question_list.append(getattr(questions, ke_questions))
            # Append all topics per KE into the list of topics
            ke_topic = f"{i.name}_topics"
            self.topic_list.append(getattr(questions, ke_topic))
            # Append a counter per KE into the list of coverage
            self.coverage.append(0)

    def get_question(self):
        ke_index = self.topic_manager.get_topic().value

        # Check if the topics open question was already asked
        open_question = self.topic_list[ke_index]
        if open_question is not '':
            self.coverage[KE.KE1.value] += 1
            self.topic_list[self.topic_manager.get_topic().value] = ''
            return open_question

        # Check if there are predefined questions for the current topics
        if self.question_list[ke_index] is not '':
            return self.random_question(ke_index)
        else:
            self.topic_manager.increase_topic()
            logger.info("Increased topic!")

        lowest_coverage = self.coverage.index(min(self.coverage))
        logger.info(f"Lowest Coverage: {lowest_coverage}")

        if self.topic_list[lowest_coverage] is not '':
            open_question = self.topic_list[lowest_coverage].pop()  # TODO: Pop from an empty list
            self.topic_list.insert(lowest_coverage, '')
            self.coverage[lowest_coverage] += 1
            return open_question
        elif self.question_list[lowest_coverage]:
            return self.random_question(lowest_coverage)
        else:
            return self.random_question(KE.KE6.value)

    def random_question(self, ke_index):
        """
        Get a random question from the list of questions.

        :return question:
        """
        random_index = random.randrange(len(self.question_list[ke_index]))
        question = self.question_list[ke_index].pop(random_index)
        self.coverage[ke_index] += 1
        # question = random.choice(self.question_list[KE.KE6.value])
        # if question['follow-up']:
        #     pass
        return question


class TopicManager:
    """
    Training exam topic manager.
    """
    def __init__(self):
        self.topic = KE.KE1

    def get_topic(self):
        return self.topic

    def increase_topic(self):
        # TODO: Add randomness for next topic?
        if self.topic.value < len(KE):
            self.topic = KE(self.topic.value + 1)
