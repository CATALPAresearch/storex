"""
Helpers
"""
from enum import IntEnum


# The course units used to be an enum here, with their German titles hard
# coded below it. They are course content and now live in courses/<id>/
# manifest.yaml, see courselib.

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
