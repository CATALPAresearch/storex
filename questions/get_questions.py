"""
File for managing predefined questions.
"""
import random
import questions.questions as questions


def question_ke6():
    """
    'Kurseinheit 6: Probleme der objektorientierten Programmierung'
    :return:
    """
    question = random.choice(questions.KE6_problems)
    # if question['follow-up']:
    #     pass
    return question
