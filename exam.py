"""
Class for training exam conversation manager.
"""
import random
import time

from audio.speech_recognition import SpeechRecognition
from audio.text_to_speech import TextToSpeech
from evaluation import Evaluator
from questions.paraphrasing import QuestionParaphraser
from questions.question_generation import QuestionGenerator
from questions.question_managing import QuestionManager
from utils import colours, preprocessing
from utils.helpers import QuestionType, FeedbackType

import logging
logger = logging.getLogger()

# TODO: Supress test output of imported modules


class ExamManager:
    # Global variables
    def __init__(self, exam_parameters):
        """
        Set the students parameters, set up the QuestionManager, greet the student and start the timer.

        :param exam_parameters: Dictionary with parameters for the exam.
        """
        logger.info(f"Setting parameters: {exam_parameters}")
        # Set student parameters
        self.student_name = exam_parameters["name"]
        self.address_form = ''
        if exam_parameters["female"]:
            self.address_form = "Frau"
        elif exam_parameters["male"]:
            self.address_form = "Herr"

        # Set duration of the exam
        duration = int(exam_parameters["time"]) * 60
        start_time = time.time()
        self.end_time = start_time + duration  # TODO: Add the LLM calculation time to end_time
        # (e.g. end_time = end_time * 1.5)

        # Setup stopwords for preprocessing
        preprocessing.setup_stopwords()

        # Set question manager and question models
        self.manager = QuestionManager()
        self.last_question = None
        self.next_question = None
        self.paraphraser = QuestionParaphraser()
        self.generator = QuestionGenerator()

        # Set audio models and evaluator
        self.no_audio = True if exam_parameters["no_audio"] else False
        if not self.no_audio:
            self.audio = TextToSpeech()
        self.transcription = SpeechRecognition()
        self.evaluation = Evaluator()

        # Set specific topics to be targeted for questions
        self.targets = []

    def speak(self, text):
        """Output text via speaker and terminal."""
        colours.print_blue(text)
        if not self.no_audio:
            self.audio.get_audio(text)

    def ask_question(self, question):
        """Output question and get the students answer."""
        self.speak(question)
        answer = self.transcription.get_audio_to_text()
        print("Ihre Antwort lautet:")
        colours.print_yellow(answer)
        return answer

    def get_feedback(self, correct_answer, student_answer, keywords=None):
        """
        Get feedback by comparing the students answer to the correct answer.
        """
        result = self.evaluation.evaluate_answer(correct_answer, student_answer)
        logger.info(f"Result: {result.name}")

        # Give feedback and set next question type
        match result.value:
            case 0:  # Correct answer
                correct = "Korrekt!"
                # if not self.no_audio:
                #     self.audio.get_audio(correct)
                colours.print_green(correct)
                self.next_question = QuestionType.PREDEFINE

            case 1:  # No answer or really short answer  TODO: Move this case to ASR
                colours.print_blue("Ich habe Sie nicht verstanden. Bitte wiederholen Sie Ihre Antwort.")
                self.next_question = QuestionType.REPEAT

            case 2:  # Off-topic answer
                colours.print_blue('Sie haben das Thema leider verfehlt.')
                self.next_question = QuestionType.REPEAT

            case 3:  # Contradicting answer
                colours.print_blue('Mit dieser Antwort wiedersprechen Sie dem Kurstext.')
                self.next_question = QuestionType.REPEAT

            case 4:  # The answer is missing topics
                # if not keywords:
                #     keywords = self.evaluation.get_keywords(correct_answer)  # TODO: Paragraph as input?
                self.targets.extend(self.evaluation.evaluate_keywords(keywords, student_answer))
                self.next_question = QuestionType.GENERATE

            case _:
                raise ValueError(f"Cannot assign {result}.")

    def start_exam(self):
        """Exam flow."""
        # Greet the student
        greeting = (f"Guten Tag {self.address_form} {self.student_name}!".replace('  ', ' '))
        self.speak(greeting)

        # TODO: Ask first question
        current_question = {'question': "Was ist objektorientierte Programmierung?",
                            'answer': "..."}
        # answer = self.ask_question(current_question['question'])
        # self.get_feedback(current_question['answer'], answer)

        self.next_question = QuestionType.PREDEFINE

        repeated = False

        # Match next question type while the exam time is not up
        while time.time() < self.end_time:
            logger.info(f"The next question should be: {self.next_question.name}")
            logger.info(f"Remaining time: {(self.end_time - time.time()) / 60} min")
            self.last_question = current_question
            match self.next_question.value:

                case 0:  # Ask predefined question
                    repeated = False
                    current_question = self.manager.get_question()
                    logger.info(f"Predefined question: {current_question}")
                    answer = self.ask_question(current_question['question'])
                    self.get_feedback(current_question['answer'], answer, current_question['keywords'])

                case 1:  # Generate specific question
                    repeated = False
                    if not self.targets:
                        logger.info("No targets")
                        self.next_question = QuestionType.PREDEFINE  # TODO: Question for connected topic
                    else:
                        target = random.choice(self.targets)
                        self.targets.remove(target)
                        logger.info(f"Target: {target}")
                        current_question = self.generator.generate_question(target)
                        logger.info(f"Generated question: {current_question}")
                        answer = self.ask_question(current_question['question'])
                        self.get_feedback(current_question['answer'], answer, current_question['keywords'])
                        repeated = True  # Todo: Reiterate generated questions with another model

                case 2:  # Generate reiteration of question
                    if repeated is False:  # TODO: How often should we reiterate? Currently: Once
                        current_question = self.last_question
                        current_question['question'] = self.paraphraser.paraphrase(self.last_question['answer'])
                        logger.info(f"Generated reiteration: {current_question}")
                        answer = self.ask_question(current_question['question'])
                        self.get_feedback(current_question['answer'], answer, current_question['keywords'])
                        repeated = True
                    else:
                        self.next_question = QuestionType.PREDEFINE

                case _:
                    raise ValueError(f"Cannot assign {self.next_question}.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.disabled = False

    dev_parameters = {"name": "Luna", "time": 5, "female": False, "male": False, "no_audio": True}
    exam = ExamManager(dev_parameters)
    exam.start_exam()
