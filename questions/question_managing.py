"""
Class for managing predefined questions.
"""
import logging
import random
import re

import questions.questions as questions

from utils.helpers import KE, Level
from utils.preprocessing import extract_keywords, preprocess_text

logger = logging.getLogger()


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
        Select a question from the list of questions for the knowledge level in the specified course unit.
        """
        ke_index = self.topic_manager.get_topic().value
        keyword = preprocess_text(keyword)
        question = ''

        for ke_level in range(3):
            # Check if there are predefined questions for the current course unit and increasing level
            if self.question_list[ke_index][ke_level] != '':
                possible_questions = []
                # Search in questions
                for question_dict in self.question_list[ke_index][ke_level]:
                    if re.search(keyword, preprocess_text(question_dict['question'])):
                        possible_questions.append(question_dict)
                print("Found in questions:", len(possible_questions))
                # Search in answers, if no questions were found
                if not possible_questions:
                    for question_dict in self.question_list[ke_index][ke_level]:
                        if re.search(keyword, preprocess_text(question_dict['answer'])):
                            possible_questions.append(question_dict)
                    print("Found in answers:", len(possible_questions))
                # Select question and break increasing the level
                if possible_questions:
                    question_index = random.choice(list(range(len(possible_questions))))
                    question = possible_questions[question_index]
                    self.question_list[ke_index][ke_level].remove(question)
                    logger.debug(f"Found: {question} for keyword '{keyword}'")
                    break
        if question == '':
            question = self.get_question()
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
        if self.topic.value < (len(KE) - 1):
            self.topic = KE(self.topic.value + 1)
            self.level = Level.REMEMBER
            logger.info(f"Increased topic to {self.topic.name} at level {self.level.name}!")

    def increase_level(self):
        if self.level.value < (len(Level) - 1):
            self.level = Level(self.level.value + 1)
            logger.info(f"Increased level to {self.level}!")
        else:
            self.increase_topic()
