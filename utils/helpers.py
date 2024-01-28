"""
Helpers
"""
from enum import IntEnum


class KE(IntEnum):
    KE1 = 0
    KE2 = 1
    KE3 = 2
    KE4 = 3  # TODO: Combine KE 4 and 5 to "Programmiermodelle"
    KE5 = 4
    KE6 = 5
    KE7 = 6


class Level(IntEnum):
    REMEMBER = 0
    APPLY = 1
    ANALYZE = 2


class QuestionType(IntEnum):
    PREDEFINE = 0
    GENERATE = 1
    REPEAT = 2


class EvaluationType(IntEnum):
    CORRECT = 0
    SILENCE = 1
    OFF_TOPIC = 2
    CONTRADICTS = 3
    MISSING_TOPIC = 4
