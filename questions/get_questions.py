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


if __name__ == "__main__":
    print(question_ke6())
