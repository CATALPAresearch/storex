"""
Class for training exam conversation manager.
"""
import logging
import os
import random
import threading
import time

from audio.speech_recognition import SpeechRecognition
from audio.text_to_speech import TextToSpeech
from evaluation import Evaluator
from feedback_managing import FeedbackManager
from questions.paraphrasing import QuestionParaphraser
from questions.question_generation import QuestionGenerator
from questions.question_managing import QuestionManager, TopicManager
from text_generation import TextGenerator
from utils import colours, preprocessing
from utils.helpers import EvaluationType, KE, Level, QuestionType

# TODO: Remove once langchain updated to InferenceClient
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

logger = logging.getLogger()


class ExamManager:
    """
    Training exam conversation manager.
    """
    def __init__(self, exam_parameters):
        """
        Sets the students parameters, stopwords, vector database, and models for question, text and audio generation,
        and starts the timer for the exam.
        """
        # Set student parameters like name and gender
        logger.info(f"Setting parameters: {exam_parameters}")
        self.student = {
            'name': exam_parameters['name'],
            'nominative': "der*die Student*in",
            'accusative': "eine*n Studentin*en",
            'dative': "einem*r Studenten*in",
            'possessive': "seine*ihre"}
        if exam_parameters['female']:
            self.student['nominative'] = "die Studentin"
            self.student['accusative'] = "eine Studentin"
            self.student['dative'] = "einer Studentin"
            self.student['possessive'] = "ihre"
        elif exam_parameters['male']:
            self.student['nominative'] = "der Student"
            self.student['accusative'] = "einen Studenten"
            self.student['dative'] = "einen Studenten"
            self.student['possessive'] = "seine"

        # Setup stopwords for preprocessing
        preprocessing.setup_word_lists()

        # Check if vector store is loaded TODO: Not necessary?
        directory = os.path.dirname(__file__)
        if not os.path.exists(os.path.join(directory, 'data/vectorStore/index.faiss')):
            from dataprocessing import process_vectorstore
            logger.info("Loading vector store...")
            process_vectorstore.process_vectorstore()

        # Set question manager and question models
        topic_manager = TopicManager()
        self.manager = QuestionManager(topic_manager)
        self.last_question = None
        self.next_question = None
        self.prepend_question = "Dann lassen Sie uns beginnen."
        self.paraphraser = QuestionParaphraser()
        self.question_generator = QuestionGenerator()

        # Set text generation model
        self.text_generator = TextGenerator()

        # Set specific topics to be targeted for questions
        self.targets = []

        # Set audio models
        self.mute = True if exam_parameters['mute'] else False
        if not self.mute:
            self.audio = TextToSpeech()
        self.transcription = SpeechRecognition()

        # Set evaluator and feedback manager
        self.evaluation = Evaluator()
        self.feedback = FeedbackManager()

        # Set time manager with the exam duration
        duration = int(exam_parameters['time']) * 60
        self.time_manager = TimeManager(duration, topic_manager, self.feedback)

    def speak(self, text):
        """Outputs the given text via the speakers and in the terminal."""
        # colours.print_blue(text)
        print_thread = threading.Thread(target=colours.print_blue, args=text)
        print_thread.start()
        if not self.mute:
            self.audio.get_audio(text)
        print_thread.join()

    def get_answer(self):
        """Gets the students answer."""
        answer = self.transcription.get_audio_to_text()
        if answer is not None:
            print("Ihre Antwort lautet (in etwa):")
            colours.print_yellow(answer)
        return answer

    def ask_question(self, question):
        """Outputs the given question, gets the students answer and evaluates the answer."""
        if self.prepend_question:
            question['question'] = f"{self.prepend_question} {question['question']}"
            self.prepend_question = ""
        self.speak(question['question'])

        with self.time_manager:
            answer = self.get_answer()
        self.get_evaluation(question, answer)

    def get_evaluation(self, question, student_answer):
        """
        Gets feedback by comparing the given students answer to the given correct answer.
        Checks the mentioning of keywords.
        Sets the type for the next question.
        """
        if student_answer is None:
            result = EvaluationType.SILENCE
        # Get evaluation by comparing the students answer to the correct answer.
        elif 'answer' in question:
            result = self.evaluation.evaluate_answer(question['answer'], student_answer)
            logger.info(f"Result: {result.name}")
        # Only check keywords for topic questions
        else:
            result = EvaluationType.MISSING_TOPIC

        questioning_sounds = ["Ah?", "Achso?", "Hmm.", "Hm?", '']

        # Set next question type
        match result.value:
            case 0:  # Correct answer
                self.prepend_question = "Ok."
                self.next_question = QuestionType.PREDEFINE
                self.time_manager.increase_correct_answers()

            case 1:  # No answer given TODO: Feedback?
                self.prepend_question = "Ich habe leider keine Antwort gehört."
                self.next_question = QuestionType.REPEAT

            case 2:  # Off-topic answer
                self.prepend_question = random.choice(questioning_sounds)
                self.next_question = QuestionType.REPEAT
                self.feedback.add_irrelevant()  # TODO: Don't count if question is repeated

            case 3:  # Contradicting answer
                self.prepend_question = random.choice(questioning_sounds)
                self.next_question = QuestionType.REPEAT
                self.feedback.add_contradiction()  # TODO: Don't count if question is repeated

            case 4:  # Check the answer for missing topics
                # Get missed topics and add them as targets and save the data for feedback
                missed_topics, max_topics = self.evaluation.evaluate_keywords(question, student_answer)
                self.targets.extend(missed_topics)
                self.feedback.add_missed(len(missed_topics), max_topics)
                if self.targets:
                    self.next_question = QuestionType.GENERATE
                else:
                    self.next_question = QuestionType.PREDEFINE

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
        self.ask_question(predefined_question)

        return predefined_question

    def ask_generated_question(self):
        """
        Gets, asks and returns a generated question.
        """
        # Get a random target (higher probability with more occurrences)
        target = random.choice(self.targets)

        # Remove all occurrences of the selected target from the targets
        self.targets = [t for t in self.targets if t != target]
        logger.info(f"Target: {target}")

        # Get a generated question
        generated_question = self.question_generator.generate_question_answer(target)
        logger.info(f"Generated question: {generated_question}")

        # Get the students answer to the question and get feedback on the answer
        self.ask_question(generated_question)

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
        self.ask_question(repeating_question)

        return repeating_question

    def mic_test(self):
        """Checks the microphone and greets the students."""
        # Greet the student and check the microphone
        mic_query = (
            f"""[INST] Du bist ein Professor an einer deutschen Universität. Du hältst online mündliche Prüfungen ab.
            Begrüße {self.student['accusative']} namens {self.student['name']} in 2 Sätzen zu einer mündlichen Prüfung.
            Sage in der Begrüßung, dass ihr als Erstes das Mikrofon testen müsst und {self.student['name']} dafür gleich hineinsprechen soll.
            Gib nur die Begrüßung zurück:[/INST]""")
        logger.info(mic_query)
        greeting = self.text_generator.get_text(mic_query)
        self.speak(greeting)
        mic_check = self.get_answer()

        # Exit the exam if no sound was detected
        if mic_check is None:
            colours.print_red("Leider ist kein Audio über Ihr Mikrofon zu vernehmen. Bitte überprüfen Sie Ihr "
                              "Mikrophon und starten die Trainingsprüfung dann erneut.")
            exit(1)

    def start_exam(self):
        """
        Starts the exam and loops through questions while the time is not up.
        """
        # Test the microphone and greet the students
        self.mic_test()

        current_question = ''
        repeated = False
        self.next_question = QuestionType.PREDEFINE

        # Check if the exam time is not up
        while self.time_manager.get_remaining_time() > 0:
            self.last_question = current_question
            self.feedback.add_question()

            # Set the question type to predefined if a new topic started or if there should be no generated questions
            # at the current level
            if (self.time_manager.check_topic() or
                    (self.time_manager.check_level() and self.next_question == QuestionType.GENERATE)):
                self.next_question = QuestionType.PREDEFINE

            # Match the question type for the next question
            match self.next_question.value:

                case 0:  # Ask a predefined question
                    repeated = False
                    current_question = self.ask_predefined_question()

                case 1:  # Generate a specific question
                    repeated = False
                    current_question = self.ask_generated_question()

                case 2:  # Generate a reiteration of the question (once per question)
                    if repeated is False:
                        current_question = self.ask_repeating_question()
                        self.feedback.add_reiteration()
                        repeated = True
                    else:
                        self.next_question = QuestionType.PREDEFINE  # TODO: Generate or Predefine question?

                case _:
                    raise ValueError(f"Cannot assign {self.next_question}.")

        # Give a feedback to the students
        feedback_rules = self.feedback.construct_feedback(self.student['nominative'])
        feedback_query = (
            f"""[INST] Du bist ein Professor an einer deutschen Universität.
            Gib {self.student['dative']} ein konstruktives Feedback für {self.student['possessive']} Leistungen in einer mündlichen Prüfung.
            Nutze folgende Informationen zu {self.student['possessive']}n Leistungen:
            {feedback_rules}
            Gib nur das Feedback zurück:[/INST]"""
        )
        logger.info(feedback_query)
        goodbye = self.text_generator.get_text(feedback_query)
        self.speak(goodbye)

        # See the student off
        goodbye_query = (
            f"""[INST] Du bist ein Professor an einer deutschen Universität. Du hältst online mündliche Prüfungen ab.
            Verabschiede {self.student['accusative']} namens {self.student['name']} in 1 Satz nach einer mündlichen Prüfung.
            Gib nur die Verabschiedung zurück:[/INST]"""
        )
        logger.info(goodbye_query)
        goodbye = self.text_generator.get_text(goodbye_query)
        self.speak(goodbye)


class TimeManager:
    """
    Training exam time manager.
    """
    def __init__(self, duration, topic_manager, feedback):
        self.remaining_time = duration
        self.topic_manager = topic_manager
        self.last_known_topic = topic_manager.get_topic()
        self.topic_time = duration / len(KE)
        self.correct_answers = 0
        self.feedback = feedback

        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self.start_time
        logger.info(f"Answer took {elapsed_time:.6f} seconds.")
        self.remaining_time = self.remaining_time - elapsed_time
        self.topic_time = self.topic_time - elapsed_time
        logger.info(f"Remaining time: {self.remaining_time:.6f} seconds ({self.topic_time:.6f} seconds in this topic).")

    def get_remaining_time(self):
        return self.remaining_time

    def increase_correct_answers(self):
        self.correct_answers += 1

    def check_topic(self):
        """
        Checks if the topic got increased by the QuestionManager and calculates the new time per topic.
        Checks if the time for the current topic ran out and increases the topic.
        """
        # Check if topic got increased or time for topic ran out
        topic = self.topic_manager.get_topic()
        if topic != self.last_known_topic or (self.topic_time <= 0 and self.last_known_topic.value < len(KE)):
            self.feedback.add_feedback(self.correct_answers, self.last_known_topic, self.topic_manager.get_level())

            # Set new topic if time for topic ran out
            if self.topic_time <= 0 and self.last_known_topic.value < len(KE):
                self.topic_manager.increase_topic()
                topic = self.topic_manager.get_topic()

            # Set new time for topic
            remaining_topics = len(KE) - topic.value
            self.topic_time = self.remaining_time / remaining_topics
            logger.info(f"Next topic {topic.name} for {self.topic_time} seconds.")

            self.last_known_topic = topic
            self.correct_answers = 0
            return True
        return False

    def check_level(self):
        # Check the level TODO: Increase from level 2 to 3 by time?
        level = self.topic_manager.get_level()
        if level == Level.REMEMBER:
            if self.correct_answers >= 2:
                self.topic_manager.increase_level()
            else:
                return True
        return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.disabled = False

    dev_parameters = {"name": "Luna", "time": 10, "female": False, "male": False, "mute": True}
    exam = ExamManager(dev_parameters)
    exam.start_exam()
