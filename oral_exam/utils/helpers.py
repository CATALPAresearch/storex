"""
Helpers
"""
from enum import IntEnum


class KE(IntEnum):
    KE1 = 0
    KE2 = 1
    KE3 = 2
    KE4 = 3  # Combination of both KE 4 and 5
    KE6 = 4  # Combination of both KE 6 and 7


def topic_from_ke(ke):
    if ke == KE.KE1.value:
        return "Grundkonzepte der objektorientierten Programmierung"
    if ke == KE.KE2.value:
        return "Systematik der objektorientierten Programmierung"
    if ke == KE.KE3.value:
        return "Typen in der objektorientierten Programmierung"
    if ke == KE.KE4.value:
        return "Programmiermodelle von Java, C-Sharp, C++ und EIFFEl"
    if ke == KE.KE6.value:
        return "Probleme der objektorientierten Programmierung und objektorientierter Programmierstil"


class Level(IntEnum):
    REMEMBER = 0
    APPLY = 1
    ANALYZE = 2


class QuestionType(IntEnum):
    PREDEFINE = 0
    GENERATE = 1
    REPEAT = 2
    SELECTED = 3


class EvaluationType(IntEnum):
    CORRECT = 0
    SILENCE = 1
    OFF_TOPIC = 2
    CONTRADICTS = 3
    MISSING_TOPIC = 4


class FeedbackType(IntEnum):
    nie = 0
    kaum = 1
    einzelne = 2
    einige = 3
    mehrere = 4
    viele = 5
    permanent = 6


class FeedbackLevel(IntEnum):
    niedriges = 0
    mittleres = 1
    hohes = 2
