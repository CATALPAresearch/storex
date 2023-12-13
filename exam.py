"""
Class for training exam conversation manager.
"""
import os
import random
import time

from audio.speech_recognition import SpeechRecognition
from audio.text_to_speech import TextToSpeech
from dataprocessing import process_vectorstore
from evaluation import Evaluator
from questions.paraphrasing import QuestionParaphraser
from questions.question_generation import QuestionGenerator
from questions.question_managing import QuestionManager
from text_generation import TextGenerator
from utils import colours, preprocessing
from utils.helpers import QuestionType, FeedbackType

import logging
logger = logging.getLogger()

# TODO: Supress test output of imported modules


class ExamManager:
    """
    Training exam conversation manager
    """
    def __init__(self, exam_parameters):
        """
        Sets the students parameters, stopwords, vector database, and models for question, text and audio generation,
        and starts the timer for the exam.
        """
        # Set student parameters like name and gender
        logger.info(f"Setting parameters: {exam_parameters}")
        self.student_name = exam_parameters['name']
        self.student = 'eine*n Studentin*en'
        if exam_parameters['female']:
            self.student = "eine Studentin"
        elif exam_parameters['male']:
            self.student = "einen Studenten"

        # Setup stopwords for preprocessing
        preprocessing.setup_stopwords()

        # Check if vector store is loaded
        directory = os.path.dirname(__file__)
        if not os.path.exists(os.path.join(directory, 'data/vectorStore/index.faiss')):
            logger.info("Loading vector store...")
            process_vectorstore.process_vectorstore()

        # Set question manager and question models
        self.manager = QuestionManager()
        self.last_question = None
        self.next_question = None
        self.prepend_question = ''
        self.paraphraser = QuestionParaphraser()
        self.question_generator = QuestionGenerator()

        # Set text generation model
        self.text_generator = TextGenerator()

        # Set specific topics to be targeted for questions
        self.targets = []

        # Set audio models and evaluator
        self.no_audio = True if exam_parameters['no_audio'] else False
        if not self.no_audio:
            self.audio = TextToSpeech()
        self.transcription = SpeechRecognition()
        self.evaluation = Evaluator()

        # Set duration of the exam
        duration = int(exam_parameters['time']) * 60
        start_time = time.time()
        self.end_time = start_time + duration  # TODO: Add the LLM calculation time to end_time (e.g. end_time = end_time * 1.5)
                                               #  or just time the students answers

    def speak(self, text):
        """Output text via speaker and terminal."""
        colours.print_blue(text)
        if not self.no_audio:
            self.audio.get_audio(text)

    def ask_question(self, question):
        """Output question and get the students answer."""
        if self.prepend_question:
            question = f"{self.prepend_question} {question}"
            self.prepend_question = ""
        self.speak(question)
        answer = self.transcription.get_audio_to_text()
        print("Ihre Antwort lautet in etwa:")
        colours.print_yellow(answer)
        return answer

    def get_feedback(self, correct_answer, student_answer, keywords=None):
        """
        Get feedback by comparing the students answer to the correct answer.
        TODO: Add multiple random vague "Aha" before next question.
        """
        result = self.evaluation.evaluate_answer(correct_answer, student_answer)
        logger.info(f"Result: {result.name}")

        # Give feedback and set next question type
        match result.value:
            case 0:  # Correct answer
                self.prepend_question = "Ok."
                self.next_question = QuestionType.PREDEFINE

            case 1:  # No answer or really short answer  TODO: Move this case to ASR
                self.next_question = QuestionType.REPEAT

            case 2:  # Off-topic answer
                self.prepend_question = "Ah?"
                self.next_question = QuestionType.REPEAT

            case 3:  # Contradicting answer
                self.prepend_question = "Achso?"
                self.next_question = QuestionType.REPEAT

            case 4:  # The answer is missing topics
                if not keywords:
                    keywords = preprocessing.extract_keywords(correct_answer)  # self.evaluation.get_keywords(correct_answer)
                self.targets.extend(self.evaluation.evaluate_keywords(keywords, student_answer))
                self.next_question = QuestionType.GENERATE

            case _:
                raise ValueError(f"Cannot assign {result}.")

    def start_exam(self):
        """Exam flow."""
        # Greet the student
        greeting_query = (f"Begrüße {self.student}", "namens" if self.student else '',
                          f"{self.student_name} kurz zu einer mündlichen Prüfung. Gib nur die Begrüßung zurück:")
        logger.info(greeting_query)
        greeting = self.text_generator.get_text(greeting_query)

        self.speak(greeting)

        current_question = ''
        self.next_question = QuestionType.PREDEFINE

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
                    if 'answer' in current_question:
                        self.get_feedback(current_question['answer'], answer, current_question['keywords'])
                    else:
                        self.next_question = QuestionType.PREDEFINE  # TODO: Question for connected topic.
                                                                     #  Search in question list or generate?

                case 1:  # Generate specific question
                    repeated = False
                    if not self.targets:
                        logger.info("No targets")
                        self.next_question = QuestionType.PREDEFINE  # TODO: Question for connected topic
                    else:
                        target = random.choice(self.targets)
                        self.targets.remove(target)
                        logger.info(f"Target: {target}")
                        current_question = self.question_generator.generate_question(target)
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
