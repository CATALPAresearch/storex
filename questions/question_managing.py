"""
Class for managing predefined questions.
"""
import random
import questions.questions as questions


# TODO: Predefine questions and their probabilities
class QuestionManager:
    def __init__(self):
        self.first_question = True
        self.question_list = []
        self.topic_list = []
        self.coverage = []
        for i in questions.KE:
            # Append all questions per KE into the list of questions
            ke_questions = f"{i.name}_questions"
            self.question_list.append(getattr(questions, ke_questions))
            # Append all topics per KE into the list of topics
            ke_topic = f"{i.name}_topics"
            self.topic_list.append(getattr(questions, ke_topic))
            # Append a counter per KE into the list of coverage
            self.coverage.append(0)

    def get_question(self):
        if self.first_question is True:
            first_open_question = self.topic_list[questions.KE.KE1.value].pop()
            self.topic_list.insert(questions.KE.KE1.value, '')
            self.coverage[questions.KE.KE1.value] += 1
            self.first_question = False
            return first_open_question

        return self.random_question(questions.KE.KE1.value)

        lowest_coverage = self.coverage.index(min(self.coverage))

        if self.topic_list[lowest_coverage] is not '':
            open_question = self.topic_list[lowest_coverage].pop()  # TODO: Pop from an empty list
            self.topic_list.insert(lowest_coverage, '')
            self.coverage[lowest_coverage] += 1
            return open_question
        elif self.question_list[lowest_coverage]:
            return self.random_question(lowest_coverage)
        else:
            return self.random_question(questions.KE.KE6.value)

    def random_question(self, ke_index):
        """
        Get a random question from the list of questions.

        :return question:
        """
        random_index = random.randrange(len(self.question_list[ke_index]))
        question = self.question_list[ke_index].pop(random_index)
        self.coverage[ke_index] += 1
        # question = random.choice(self.question_list[questions.KE.KE6.value])
        # if question['follow-up']:
        #     pass
        return question
