"""
Class for training exam conversation manager.
"""
import logging
import os
import random
import time

from audio.speech_recognition import SpeechRecognition
from audio.text_to_speech import TextToSpeech
from evaluation import Evaluator
from questions.paraphrasing import QuestionParaphraser
from questions.question_generation import QuestionGenerator
from questions.question_managing import QuestionManager
from text_generation import TextGenerator
from utils import colours, preprocessing
from utils.helpers import QuestionType, FeedbackType

logger = logging.getLogger()


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
        preprocessing.setup_word_lists()

        # Check if vector store is loaded TODO: Not necessary?
        directory = os.path.dirname(__file__)
        if not os.path.exists(os.path.join(directory, 'data/vectorStore/index.faiss')):
            from dataprocessing import process_vectorstore
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
        """Outputs the given text via the speakers and in the terminal."""
        colours.print_blue(text)
        if not self.no_audio:
            self.audio.get_audio(text)

    def ask_question(self, question):
        """Outputs the given question and gets the students answer."""
        if self.prepend_question:
            question = f"{self.prepend_question} {question}"
            self.prepend_question = ""
        self.speak(question)
        answer = self.transcription.get_audio_to_text()
        print("Ihre Antwort lautet (in etwa):")
        colours.print_yellow(answer)
        return answer

    def get_feedback(self, question, student_answer):
        """
        Gets feedback by comparing the given students answer to the given correct answer.
        Checks the mentioning of keywords.
        Sets the type for the next question.
        TODO: Add multiple random vague "Aha" before next question.
        """
        # Get feedback by comparing the students answer to the correct answer.
        if 'answer' in question:
            result = self.evaluation.evaluate_answer(question['answer'], student_answer)
            logger.info(f"Result: {result.name}")
        # Only check keywords for topic questions
        else:
            result = FeedbackType.MISSING_TOPIC

        # Set next question type
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
                if 'keywords' not in question:
                    # TODO: Get keywords (same in question manager for pre-defined?)
                    question['keywords'] = preprocessing.extract_keywords(question['answer'])  # self.evaluation.get_keywords(correct_answer)
                self.targets.extend(self.evaluation.evaluate_keywords(question['keywords'], student_answer))
                if self.targets:
                    self.next_question = QuestionType.GENERATE
                else:
                    self.next_question = QuestionType.CONNECT

            case _:
                raise ValueError(f"Cannot assign {result}.")

        logger.info(f"The next question should be: {self.next_question.name}")

    def ask_predefined_question(self):
        """
        Gets, asks and returns a predefined question.
        """
        # Get predefined question
        predefined_question = self.manager.get_question()
        logger.info(f"Predefined question: {predefined_question}")

        # Get the students answer to the question and get feedback on the answer
        answer = self.ask_question(predefined_question['question'])
        self.get_feedback(predefined_question, answer)

        return predefined_question

    def ask_generated_question(self):
        """
        Gets, asks and returns a generated question.
        """
        # Get a random target TODO: different probabilities?
        target = random.choice(self.targets)
        self.targets.remove(target)
        logger.info(f"Target: {target}")

        # Get a generated question
        generated_question = self.question_generator.generate_question(target)
        logger.info(f"Generated question: {generated_question}")

        # Get the students answer to the question and get feedback on the answer
        answer = self.ask_question(generated_question['question'])
        self.get_feedback(generated_question, answer)

        return generated_question

    def ask_repeating_question(self):
        """
        Gets, asks and returns a reiterated question.
        """
        # Get a Reiteration of the last question
        repeating_question = self.last_question
        repeating_question['question'] = self.paraphraser.paraphrase(self.last_question['answer'])
        logger.info(f"Generated reiteration: {repeating_question}")

        # Get the students answer to the question and get feedback on the answer
        answer = self.ask_question(repeating_question['question'])
        self.get_feedback(repeating_question, answer)

        return repeating_question

    def start_exam(self):
        """
        Starts the exam and loops through questions while the time is not up.
        """
        # Greet the student
        greeting_query = (f"Begrüße {self.student} namens {self.student_name} kurz zu einer mündlichen Prüfung. "
                          f"Gib nur die Begrüßung zurück:")
        logger.info(greeting_query)
        greeting = self.text_generator.get_text(greeting_query)
        self.speak(greeting)

        current_question = ''
        self.next_question = QuestionType.PREDEFINE

        # Match next question type while the exam time is not up
        while time.time() < self.end_time:
            logger.info(f"Remaining time: {(self.end_time - time.time()) / 60} min")
            self.last_question = current_question
            match self.next_question.value:

                case 0:  # Ask a predefined question
                    repeated = False
                    current_question = self.ask_predefined_question()

                case 1:  # Generate a specific question
                    repeated = False
                    current_question = self.ask_generated_question()

                case 2:  # Generate a reiteration of the question
                    if repeated is False:  # TODO: How often should we reiterate? Currently: Once
                        current_question = self.ask_repeating_question()
                        repeated = True
                    else:
                        self.next_question = QuestionType.CONNECT  # TODO: Connected question?

                case 3:  # Ask a connected question
                    # TODO
                    self.next_question = QuestionType.PREDEFINE

                case _:
                    raise ValueError(f"Cannot assign {self.next_question}.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.disabled = False

    dev_parameters = {"name": "Luna", "time": 5, "female": False, "male": False, "no_audio": True}
    exam = ExamManager(dev_parameters)
    exam.start_exam()
