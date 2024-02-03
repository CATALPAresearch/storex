"""
Class for managing predefined questions.
"""
import logging
import random
import re

import questions.questions as questions

from utils.helpers import KE, Level

logger = logging.getLogger()


# TODO: Predefine questions and their probabilities
class QuestionManager:
    def __init__(self, topic_manager):
        self.topic_manager = topic_manager
        self.question_list = []
        self.topic_list = []
        for unit in KE:
            # Append all questions per KE into the list of questions
            ke_questions = f"{unit.name}_questions"
            self.question_list.append(getattr(questions, ke_questions))
            # Append all topics per KE into the list of topics
            ke_topic = f"{unit.name}_topics"
            self.topic_list.append(getattr(questions, ke_topic))

    def get_question(self):
        while True:
            ke_index = self.topic_manager.get_topic().value
            ke_level = self.topic_manager.get_level().value

            # Check if the course units open question was already asked
            open_question = self.topic_list[ke_index] if ke_level == 0 else ''
            if open_question != '':
                self.topic_list[self.topic_manager.get_topic().value] = ''
                return open_question

            # Check if there are predefined questions for the current course unit and level
            if self.question_list[ke_index][ke_level] != '':
                question = self.random_question(ke_index, ke_level)
                break
            else:
                self.topic_manager.increase_level()
        return question

    def random_question(self, ke_index, ke_level):
        """
        Get a random question from the list of questions for the specified level in the specified course unit.
        """
        random_index = random.randrange(len(self.question_list[ke_index][ke_level]))
        question = self.question_list[ke_index][ke_level].pop(random_index)
        return question

    def select_question(self, keyword):
        """
        Select a question from the list of questions for the specified level in the specified course unit.
        """
        while True:
            ke_index = self.topic_manager.get_topic().value
            ke_level = self.topic_manager.get_level().value

            # Check if there are predefined questions for the current course unit and level
            if self.question_list[ke_index][ke_level] != '':
                possible_questions = []
                for question_dict in self.question_list[ke_index][ke_level]:
                    if re.search(keyword, question_dict['question']) or re.search(keyword, question_dict['question']):
                        possible_questions.append(question_dict)
                if possible_questions:
                    question = self.random_question(ke_index, ke_level)
                else:
                    question = self.get_question()
                break
            else:
                self.topic_manager.increase_level()
        return question


class TopicManager:
    """
    Training exam topic and level manager.
    """
    def __init__(self):
        self.topic = KE.KE1
        self.level = Level.REMEMBER

    def get_topic(self):
        return self.topic

    def get_level(self):
        return self.level

    def increase_topic(self):
        if self.topic.value < len(KE):
            self.topic = KE(self.topic.value + 1)
            self.level = Level.REMEMBER
            logger.debug(f"Increased topic to {self.topic} at level {self.level}!")

    def increase_level(self):
        if self.level.value < len(Level):
            self.level = Level(self.level.value + 1)
            logger.debug(f"Increased level to {self.level}!")
        else:
            self.increase_topic()
