"""
Class for feedback managing.
"""
import re

from utils.helpers import FeedbackLevel, FeedbackType, KE, Level, topic_from_ke


def get_grade(percentage):
    if percentage == 1:
        return FeedbackType(0).name
    elif percentage > 0.85:
        return FeedbackType(1).name
    elif percentage > 0.70:
        return FeedbackType(2).name
    elif percentage > 0.60:
        return FeedbackType(3).name
    elif percentage > 0.50:
        return FeedbackType(4).name
    elif percentage > 0.30:
        return FeedbackType(5).name
    else:
        return FeedbackType(6).name


def check_feedback(text):
    text = text.split('\n')
    text = list(filter(None, text))
    for i, line in reversed(list(enumerate(text))):
        if re.search("Grüße", line):
            text = text[:i]
            break

    greeting = text[0].strip().split(' ', 1)
    text[0] = greeting[1] if "Liebe" in greeting[0] else text[0].strip()
    text = ' '.join(text)
    return text


class FeedbackManager:
    """
    Class which collects and constructs performance data.
    """
    def __init__(self):
        self.all_questions = 0  # Counter for the amount of questions that were asked
        self.contradiction_counter = 0  # Counter for contradicting, wrong answer
        self.irrelevant_counter = 0  # Counter for off-topic, irrelevant answers
        self.missed_term_counter = [0, 0]  # Counter for incomplete answers and amount of all keywords
        self.reiteration_counter = 0  # Counter for the amount of help that was given in form of reiteration
        self.non_concise_counter = 0  # Counter for non-concise answers

        self.correct_answers = []  # Counter for correctly answered questions per KE
        self.completed_level = []  # Level reached per KE
        for _ in KE:
            self.correct_answers.append(0)
            self.completed_level.append(0)

    def add_question(self):
        self.all_questions += 1

    def add_contradiction(self):
        self.contradiction_counter += 1

    def remove_contradiction(self):
        if self.contradiction_counter >= 1:
            self.contradiction_counter -= 1

    def remove_irrelevant(self):
        if self.irrelevant_counter >= 1:
            self.irrelevant_counter += 1

    def add_irrelevant(self):
        self.irrelevant_counter += 1

    def add_missed(self, missed_count, all_count):
        if missed_count:
            self.missed_term_counter[0] += missed_count
            self.missed_term_counter[1] += all_count
        else:
            self.non_concise_counter += 1

    def add_reiteration(self):
        self.reiteration_counter += 1

    def add_feedback(self, correct, ke, level):
        self.correct_answers[ke] += correct
        self.completed_level[ke] = level.value

    def construct_feedback(self, student):
        """
        Constructs performance data.
        """
        feedback_string = ""
        questions = self.all_questions - self.reiteration_counter

        # Construct strings for feedback from counters
        contradiction_value = 1 if questions == 0 else 1 - (self.contradiction_counter / questions)
        contradiction_grade = get_grade(contradiction_value)
        feedback_string += f"{student} hat {contradiction_grade} inhaltliche Fehler gemacht.\n"

        relevancy_value = 1 if questions == 0 else 1 - (self.irrelevant_counter / questions)
        relevancy_grade = get_grade(relevancy_value)
        feedback_string += f"{student} hat {relevancy_grade} irrelevante Antworten gegeben.\n"

        completion_value = 1 if self.missed_term_counter[1] == 0 else (
                1 - (self.missed_term_counter[0] / self.missed_term_counter[1]))
        completion_grade = get_grade(completion_value)
        feedback_string += f"{student} hat {completion_grade} unvollständige oder oberflächliche Antworten gegeben.\n"

        reiteration_value = 1 if questions == 0 else 1 - (self.reiteration_counter / questions)
        reiteration_grade = get_grade(reiteration_value)
        feedback_string += f"{student} benötigt {reiteration_grade} Hilfestellungen.\n"

        concise_value = 1 if (questions - (self.irrelevant_counter + self.contradiction_counter)) == 0 else (
                1 - (self.non_concise_counter / (questions - (self.irrelevant_counter + self.contradiction_counter))))
        concise_grade = get_grade(concise_value)
        feedback_string += f"{student} hat {concise_grade} unpräzise Antworten gegeben.\n"

        # Construct feedback strings from information per KE
        average = sum(self.completed_level) / len(self.completed_level)
        level = FeedbackLevel(round(average)).name
        feedback_string += f"{student} hat ein {level} Leistungslevel erreicht.\n"

        highest_level = [i for i, j in enumerate(self.completed_level) if j == max(self.completed_level)]
        lowest_level = [i for i, j in enumerate(self.completed_level) if j == min(self.completed_level)]
        optima = [highest_level, lowest_level]
        topics = []

        for optimum in optima:
            if len(optimum) > 1:
                answers = [self.correct_answers[i] for i in optimum]
                most_level = optimum[answers.index(max(answers))]
            else:
                most_level = optimum[0]
            topic = topic_from_ke(most_level)
            topics.append(topic)

        feedback_string += f"{student} war am besten bei dem Thema '{topics[0]}'.\n"
        feedback_string += f"{student} war am schlechtesten bei dem Thema '{topics[1]}'."

        return feedback_string
