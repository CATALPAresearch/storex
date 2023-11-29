"""
Class for managing predefined questions.
"""
import random
import questions.questions as questions


# TODO: Predefine questions and their probabilities
class QuestionManager:
    def __init__(self):
        self.question_list = []
        # Append all questions per KE into the list of questions
        for i in questions.KE:
            ke_questions = f"{i.name}_questions"
            self.question_list.append(getattr(questions, ke_questions))
        # [[KE1_questions][KE2_questions][KE3_questions][KE4_questions][KE5_questions][KE6_questions][KE7_questions]]

    def get_question(self):
        if self.question_list[questions.KE.KE6.value]:
            return self.question_ke6()
        return "No question found"

    def question_ke6(self):
        """
        'Kurseinheit 6: Probleme der objektorientierten Programmierung'

        :return question: Question from KE6.
        """
        random_index = random.randrange(len(self.question_list[questions.KE.KE6.value]))
        question = self.question_list[questions.KE.KE6.value].pop(random_index)
        # question = random.choice(self.question_list[questions.KE.KE6.value])
        # if question['follow-up']:
        #     pass
        return question
