import random
import data.questions as questions


def question_ke6():
    """
    'Kurseinheit 6: Probleme der objektorientierten Programmierung'
    :return:
    """
    question = random.choice(questions.KE6_problems)
    # if question['follow-up']:
    #     pass
    return question
