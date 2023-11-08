"""
Helpers
"""
from enum import IntEnum


class QuestionType(IntEnum):
    PREDEFINED = 0
    GENERATED = 1
    SILENCE = 2
    # Checkup
