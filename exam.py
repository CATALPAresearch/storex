"""
Class for training exam conversation manager.
"""
import time

from audio.speech_recognition import SpeechRecognition
from audio.text_to_speech import TextToSpeech
from evaluation import Evaluator
from questions.question_manager import QuestionManager
from utils import colours
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
        # Set student parameters
        self.student_name = exam_parameters["name"]
        self.address_form = ''
        if exam_parameters["female"]:
            self.address_form = "Frau"
        elif exam_parameters["male"]:
            self.address_form = "Herr"
        logger.info(f"Parameters are set: {exam_parameters}")

        # Set duration of the exam
        duration = int(exam_parameters["time"]) * 60
        start_time = time.time()
        self.end_time = start_time + duration  # TODO: Add the LLM calculation time to end_time
        # (e.g. end_time = end_time * 1.5)

        # Set question manager
        self.qm = QuestionManager()
        self.last_question = None
        self.next_question = None

        # Set audio models and evaluator
        self.no_audio = True if exam_parameters["no-audio"] else False
        if not self.no_audio:
            self.audio = TextToSpeech()
        self.transcription = SpeechRecognition()
        self.evaluation = Evaluator()

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

    def get_feedback(self, correct_answer, student_answer):
        """Get and give feedback to the student comparing their answer to the correct answer."""
        result = self.evaluation.evaluate_answer(correct_answer, student_answer)
        logger.info(f"Result: {result.name}")

        # Give feedback and set next question type
        match result.value:
            case 0:  # Correct answer
                correct = "Korrekt!"
                if not self.no_audio:
                    self.audio.get_audio(correct)
                colours.print_green(correct)
                self.next_question = QuestionType.PREDEFINED

            case 1:  # No or too short answer
                self.speak("Ich habe Sie nicht verstanden. Bitte wiederholen Sie Ihre Antwort.")
                self.next_question = QuestionType.REPEAT

            case 2:  # Off-topic answer
                self.speak('Sie haben das Thema leider verfehlt.')
                self.next_question = QuestionType.REPEAT

            case 3:  # Contradicting answer
                self.speak('Mit dieser Antwort wiedersprechen Sie dem Kurstext.')
                self.next_question = QuestionType.REPEAT

            case 4:  # The answer is missing topics
                # TODO: Get missing topics and give feedback
                missing_topics = self.evaluation.get_missing_keys(correct_answer, student_answer)
                self.next_question = QuestionType.GENERATED

            case _:
                raise ValueError(f"Cannot assign {result}.")

    def start_exam(self):
        """Exam flow."""
        # Greet the student
        greeting = (f"Guten Tag {self.address_form} {self.student_name}!".replace('  ', ' '))
        self.speak(greeting)

        # TODO: Ask first question
        question_and_answer = {"question": "Was ist objektorientierte Programmierung?",
                               "answer": "..."}
        # answer = self.ask_question(question_and_answer["question"])
        # self.get_feedback(question_and_answer["answer"], answer)

        self.next_question = QuestionType.PREDEFINED
        targets = []
        repeated = False

        # Match next question type while the exam time is not up
        while time.time() < self.end_time:
            logger.info(f"The next question should be: {self.next_question.name}")
            logger.info(f"Remaining time: {(self.end_time - time.time()) / 60} min")
            self.last_question = question_and_answer
            match self.next_question.value:

                case 0:  # Ask predefined question
                    repeated = False
                    question_and_answer = self.qm.get_question()
                    answer = self.ask_question(question_and_answer["question"])
                    self.get_feedback(question_and_answer["answer"], answer)

                case 1:  # Generate specific question
                    repeated = False
                    question_and_answer = "What is OOP?"
                    self.next_question = QuestionType.PREDEFINED

                    # TODO: Find answer for target keyword in database
                    # TODO: Generate question for target keyword
                    # specific = generate_questions
                    # ask_question(specific["question"])
                    # answer = get_answer()
                    # get_feedback(specific["answer"], answer)

                case 2:  # Repeat question once due to silence or no entailment
                    if repeated is False:
                        # TODO: Frage mittels LLM umformulieren
                        answer = self.ask_question(self.last_question["question"])
                        self.get_feedback(self.last_question["answer"], answer)
                        repeated = True
                    else:
                        # TODO: Hilfestellung geben
                        self.next_question = QuestionType.GENERATED

                case _:
                    raise ValueError(f"Cannot assign {self.next_question}.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.disabled = False

    dev_parameters = {"name": "Luna", "time": 5, "female": False, "male": False, "no-audio": True}
    exam = ExamManager(dev_parameters)
    exam.start_exam()
