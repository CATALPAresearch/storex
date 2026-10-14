"""
Class for managing predefined questions.
"""
import copy
import logging
import random
import re

from oral_exam.utils.helpers import Level
from oral_exam.utils.preprocessing import preprocess_text

logger = logging.getLogger(__name__)


class NoQuestionsLeft(Exception):
    """Raised when every course unit and level has run out of questions."""


class QuestionManager:
    """
    Class for a question manager.
    """
    def __init__(self, topic_manager, course):
        self.topic_manager = topic_manager
        # Asking a question removes it from the pool, so the course data, which
        # is shared by every exam in this process, is copied per exam.
        self.question_list = copy.deepcopy([[list(level) for level in unit.questions]
                                            for unit in course.units])
        # The open question of a unit, or '' once it has been asked
        self.topic_list = [unit.open_question.as_dict() if unit.open_question else ''
                           for unit in course.units]

    def get_question(self):
        """
        Gets the next predefined question for the current course unit and level.
        Raises NoQuestionsLeft if no question is available any more.
        """
        while True:
            ke_index = self.topic_manager.get_topic()
            ke_level = self.topic_manager.get_level().value

            # Check if the course units open question was already asked
            open_question = self.topic_list[ke_index] if ke_level == 0 else ''
            if open_question:
                self.topic_list[ke_index] = ''
                return open_question

            # Check if there are predefined questions for the current course unit and level
            if self.question_list[ke_index][ke_level]:
                return self.random_question(ke_index, ke_level)

            # The level is exhausted, so move on. TopicManager.increase_level is
            # a no-op at the last level of the last course unit, which would
            # spin this loop forever, so give up once nothing changes any more.
            self.topic_manager.increase_level()
            if (self.topic_manager.get_topic() == ke_index
                    and self.topic_manager.get_level().value == ke_level):
                raise NoQuestionsLeft("All predefined questions have been asked.")

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
        ke_index = self.topic_manager.get_topic()
        # Escaped, because a technical term may hold regex syntax such as 'c++'
        keyword = re.escape(preprocess_text(keyword))
        question = ''

        for ke_level in range(len(Level)):
            # Check if there are predefined questions for the current course unit and increasing level
            if not self.question_list[ke_index][ke_level]:
                continue

            possible_questions = []
            # Search in questions
            for question_dict in self.question_list[ke_index][ke_level]:
                if re.search(keyword, preprocess_text(question_dict['question'])):
                    possible_questions.append(question_dict)
            logger.info("Found in questions: %s", len(possible_questions))
            # Search in answers, if no questions were found
            if not possible_questions:
                for question_dict in self.question_list[ke_index][ke_level]:
                    if re.search(keyword, preprocess_text(question_dict['answer'])):
                        possible_questions.append(question_dict)
                logger.info("Found in answers: %s", len(possible_questions))
            # Select question and break increasing the level
            if possible_questions:
                question = random.choice(possible_questions)
                self.question_list[ke_index][ke_level].remove(question)
                logger.debug("Found: %s for keyword '%s'", question, keyword)
                break

        if question == '':
            question = self.get_question()
        return question


class TopicManager:
    """
    Training exam topic and level manager.

    The topic is an index into the units of the course being examined.
    """
    def __init__(self, course):
        self.course = course
        self.topic = 0
        self.level = Level.REMEMBER

    def get_topic(self):
        return self.topic

    def get_level(self):
        return self.level

    def current_unit(self):
        return self.course.units[self.topic]

    def unit_count(self):
        return len(self.course.units)

    def increase_topic(self):
        if self.topic < (self.unit_count() - 1):
            self.topic += 1
            self.level = Level.REMEMBER
            logger.info("Increased topic to %s at level %s!",
                        self.current_unit().id, self.level.name)

    def increase_level(self):
        if self.level.value < (len(Level) - 1):
            self.level = Level(self.level.value + 1)
            logger.info("Increased level to %s!", self.level)
        else:
            self.increase_topic()
