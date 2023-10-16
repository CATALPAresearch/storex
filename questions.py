import random


def question_ke6():
    """
    'Kurseinheit 6: Probleme der objektorientierten Programmierung'
    :return:
    """
    problems = ["Problem der Substituierbarkeit",
                "Liskov-Substitutionsprinzip",
                "Fragile-Base-Class-Problem",
                "Problem der schlechten Tracebarkeit",
                "Problem der eindimensionalen Strukturierung",
                "Problem der mangelnden Kapselung",
                "Problem der mangelnden Strukturierung",
                "Problem der mangelnden Eignung"]

    question = "Was ist das " + random.choice(problems) + "?"
    return question
