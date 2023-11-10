"""
Helpers
"""
from enum import IntEnum


class QuestionType(IntEnum):
    PREDEFINED = 0
    GENERATED = 1
    REPEAT = 2


class FeedbackType(IntEnum):
    CORRECT = 0
    SILENCE = 1
    OFF_TOPIC = 2
    CONTRADICTS = 3
    MISSING_TOPIC = 4
