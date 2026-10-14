#!/usr/bin/python3
"""
Class for training exam conversation manager.
"""
import logging
import os
import random
import threading
import time

import models

from feedback_managing import FeedbackManager, check_feedback
from questions.paraphrasing import QuestionParaphraser
from questions.question_generation import QuestionGenerator
from questions.question_managing import NoQuestionsLeft, QuestionManager, TopicManager
from text_generation import TextGenerator
from utils import colours, preprocessing
from utils.helpers import EvaluationType, KE, Level, QuestionType

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

logger = logging.getLogger(__name__)

# How long a single answer may take before it counts as silence. The web app
# applies this while waiting for a browser upload; it also bounds what a single
# turn can subtract from the remaining exam time.
ANSWER_TIMEOUT = int(os.getenv("ANSWER_TIMEOUT", "120"))
TURN_CAP = ANSWER_TIMEOUT + 60


class ExamAborted(Exception):
    """Raised when an exam cannot be continued, for example because the client is gone."""


class MicrophoneUnavailable(ExamAborted):
    """Raised when no audio at all was received during the microphone check."""


class AudioUnavailable(ExamAborted):
    """
    Raised when the local audio stack is missing.

    pyaudio and simpleaudio are the optional 'cli' extra and are deliberately
    not installed in the container, where the browser handles the audio.
    """
    MESSAGE = ("Für Audio im Terminal fehlen pyaudio und simpleaudio. "
               "Installieren Sie sie mit 'poetry install --extras cli', nutzen Sie "
               "--mute und --ai ohne Audio, oder öffnen Sie die Web-App unter "
               "http://localhost:5000.")

    def __init__(self, message=None):
        super().__init__(message or self.MESSAGE)


class ExamManager:
    """
    Training exam conversation manager.
    """
    def __init__(self, exam_parameters, channel=None):
        """
        Sets the students parameters, stopwords, vector database, and models for question, text and audio generation,
        and starts the timer for the exam.

        :param channel: if given, the examiner speaks and listens through this
            channel instead of through the terminal and a local microphone. This
            is what lets the web app drive the same conversation, see web/session.py.
        """
        self.channel = channel
        self.ai_student = False
        # Set student parameters like name and gender
        logger.info("Setting parameters: %s", exam_parameters)
        self.student = {
            'name': exam_parameters['name'],
            'nominative': "der*die Student*in",
            'accusative': "eine*n Studentin*en",
            'dative': "einem*r Studenten*in",
            'possessive': "seine*ihre"}
        if exam_parameters.get('female'):
            self.student['nominative'] = "die Studentin"
            self.student['accusative'] = "eine Studentin"
            self.student['dative'] = "einer Studentin"
            self.student['possessive'] = "ihre"
        elif exam_parameters.get('male'):
            self.student['nominative'] = "der Student"
            self.student['accusative'] = "einen Studenten"
            self.student['dative'] = "einem Studenten"
            self.student['possessive'] = "seine"

        # Setup stopwords for preprocessing
        preprocessing.setup_word_lists()

        # Set text generation model
        self.text_generator = TextGenerator()

        # Set question manager and question models
        topic_manager = TopicManager()
        self.manager = QuestionManager(topic_manager)
        self.last_question = None
        self.next_question = None
        self.repeating_reason = None
        self.prepend_question = "Dann lassen Sie uns beginnen."
        self.paraphraser = QuestionParaphraser()
        self.question_generator = QuestionGenerator(self.text_generator)

        # Set specific topics to be targeted for questions
        self.targets = []

        # Set audio models. The web app plays and records audio in the browser,
        # so neither is loaded when a channel is used.
        self.mute = bool(exam_parameters.get('mute'))
        self.audio = None
        self.transcription = None
        if self.channel is None and not self.mute:
            try:
                from audio.text_to_speech import TextToSpeech
            except ImportError as error:
                raise AudioUnavailable() from error
            self.audio = TextToSpeech()
        if exam_parameters.get('ai'):
            from testing.ai_student import Student
            self.ai_student = Student()
        elif self.channel is None:
            # Fail here rather than at the first question, when the microphone
            # module would be imported for the recording
            try:
                import audio.microphone  # noqa: F401
            except ImportError as error:
                raise AudioUnavailable() from error
            self.transcription = models.get_speech_recognition()

        # Set evaluator and feedback manager
        self.evaluation = models.get_evaluator()
        self.feedback = FeedbackManager()

        # Set time manager with the exam duration
        duration = (int(exam_parameters['time']) * 60)
        self.time_manager = TimeManager(duration, topic_manager, self.feedback)

    def speak(self, text):
        """Outputs the given text via the speakers and in the terminal."""
        if self.channel is not None:
            self.channel.say(text)
        elif self.ai_student:
            import testing.ai_student
            testing.ai_student.write_output(text)
        else:
            print_thread = threading.Thread(target=colours.print_blue, args=(text,))
            print_thread.start()
            if not self.mute:
                self.audio.get_audio(text)
            print_thread.join()

    def get_answer(self):
        """Gets the students answer."""
        if self.channel is not None:
            return self.channel.listen()

        answer = self.transcription.get_audio_to_text()
        if answer is not None:
            print("Ihre Antwort lautet (in etwa):")
            colours.print_yellow(answer)
        return answer

    def ask_question(self, question):
        """Outputs the given question, gets the students answer and evaluates the answer."""
        # The question text is not written back into the question, because the
        # predefined questions are shared data: prefixing in place would leak
        # into every later exam in the same process.
        spoken_question = question['question']
        if self.prepend_question:
            spoken_question = f"{self.prepend_question} {spoken_question}"
            self.prepend_question = ""

        if self.ai_student:
            with self.time_manager:
                answer = self.ai_student.get_answer(spoken_question)
                logger.info("AI answer: %s", answer)
        else:
            with self.time_manager:
                self.speak(spoken_question)
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
        # Only check keywords for topic questions
        else:
            result = EvaluationType.MISSING_TOPIC
        logger.info("Result: %s", result.name)

        questioning_sounds = ["Ah?", "Achso?", "Hmm.", "Hm?", '']
        accepting_sound = ["Ok.", '']

        # Set next question type
        match result.value:
            case 0:  # Correct answer
                self.prepend_question = random.choice(accepting_sound)
                self.next_question = QuestionType.PREDEFINE
                self.time_manager.increase_correct_answers()

            case 1:  # No answer given
                self.prepend_question = "Ich habe leider keine Antwort gehört."
                if 'answer' in question:
                    self.next_question = QuestionType.REPEAT
                    self.repeating_reason = EvaluationType.SILENCE
                else:
                    self.next_question = QuestionType.PREDEFINE

            case 2:  # Off-topic answer
                self.prepend_question = random.choice(questioning_sounds)

                # Get missed topics and add them as targets and save the data for feedback
                missed_topics, _ = self.evaluation.evaluate_keywords(question, student_answer)
                self.targets.extend(missed_topics)
                self.feedback.add_irrelevant()
                # Reiterate the question once, the same way a contradiction is
                # handled; the irrelevant answer is then no longer held against
                # the student, see start_exam.
                if 'answer' in question:
                    self.next_question = QuestionType.REPEAT
                    self.repeating_reason = EvaluationType.OFF_TOPIC
                elif self.targets:
                    self.next_question = QuestionType.SELECTED
                else:
                    self.next_question = QuestionType.PREDEFINE

            case 3:  # Contradicting answer
                self.prepend_question = random.choice(questioning_sounds)
                self.next_question = QuestionType.REPEAT
                self.repeating_reason = EvaluationType.CONTRADICTS
                self.feedback.add_contradiction()

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

        if self.ai_student:
            import testing.ai_student
            testing.ai_student.write_output(f"[Eval:] Result: {result.name}")
        logger.info("The next question should be: %s", self.next_question.name)

    def ask_predefined_question(self):
        """
        Gets, asks and returns a predefined question.
        """
        # Get predefined question
        predefined_question = self.manager.get_question()
        logger.info("Predefined question: %s", predefined_question)

        # Get the students answer to the question and get feedback on the answer
        self.ask_question(predefined_question)

        return predefined_question

    def take_target(self):
        """
        Takes a random target topic and removes all of its occurrences.
        A topic that was missed more often is more likely to be picked.
        """
        target = random.choice(self.targets)

        # Remove all occurrences of the selected target from the targets
        self.targets = [t for t in self.targets if t != target]
        logger.info("Target: %s", target)
        return target

    def ask_generated_question(self):
        """
        Gets, asks and returns a generated question.
        Falls back to a predefined question if none could be generated.
        """
        if not self.targets:
            return self.ask_predefined_question()

        # Get a generated question for a random target
        generated_question = self.question_generator.generate_question_answer(self.take_target())
        logger.info("Generated question: %s", generated_question)
        if generated_question is None:
            return self.ask_predefined_question()

        # Get the students answer to the question and get feedback on the answer
        self.ask_question(generated_question)

        return generated_question

    def ask_repeating_question(self):
        """
        Gets, asks and returns a reiterated question.
        """
        # Get a Reiteration of the last question
        repeating_question = dict(self.last_question)
        repeating_question['question'] = self.paraphraser.paraphrase(self.last_question['answer'])
        logger.info("Generated reiteration: %s", repeating_question)

        # Get the students answer to the question and get feedback on the answer
        self.ask_question(repeating_question)

        return repeating_question

    def ask_selected_question(self):
        """
        Gets, asks and returns a question selected for a missed topic.
        """
        if not self.targets:
            return self.ask_predefined_question()

        # Get selected question for a random target
        selected_question = self.manager.select_question(self.take_target())
        logger.info("Selected question: %s", selected_question)

        # Get the students answer to the question and get feedback on the answer
        self.ask_question(selected_question)

        return selected_question

    def mic_test(self):
        """
        Checks the microphone and greets the students.

        :raises MicrophoneUnavailable: if no audio was received at all.
        """
        # Greet the student and check the microphone
        mic_query = (
            f"""Begrüße {self.student['accusative']} namens {self.student['name']} in 2 Sätzen zu einer mündlichen Prüfung.
            Sage in der Begrüßung, dass ihr als Erstes das Mikrofon testen müsst und {self.student['name']} dafür gleich hineinsprechen soll.
            Gib nur die Begrüßung zurück:""")
        greeting = self.text_generator.get_text(mic_query)
        self.speak(greeting)

        if not self.ai_student:
            mic_check = self.get_answer()
            # Stop the exam if no sound was detected
            if mic_check is None:
                raise MicrophoneUnavailable(
                    "Leider ist kein Audio über Ihr Mikrofon zu vernehmen. Bitte überprüfen Sie Ihr "
                    "Mikrophon und starten die Trainingsprüfung dann erneut.")

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

            # If a new topic started, clear the targets and set the question type to predefined
            if self.time_manager.check_topic():
                self.targets = []
                self.next_question = QuestionType.PREDEFINE
            # Set the question type to selected if there should be no generated questions at the current level or the
            # maximum of hints is reached
            if ((self.time_manager.check_level() and self.next_question == QuestionType.GENERATE)
                    or (self.next_question == QuestionType.REPEAT and repeated is True)):
                if self.targets:
                    self.next_question = QuestionType.SELECTED
                else:
                    self.next_question = QuestionType.PREDEFINE
            # A reiteration needs a previous question that has a sample answer
            if self.next_question == QuestionType.REPEAT and not isinstance(self.last_question, dict):
                self.next_question = QuestionType.PREDEFINE

            logger.info("The next question is: %s", self.next_question.name)
            if self.ai_student:
                import testing.ai_student
                testing.ai_student.write_output(f"[Eval:] Question: {self.next_question.name}")

            # Match the question type for the next question
            try:
                match self.next_question.value:

                    case 0:  # Ask a predefined question
                        repeated = False
                        current_question = self.ask_predefined_question()

                    case 1:  # Generate a specific question
                        repeated = False
                        current_question = self.ask_generated_question()

                    case 2:  # Generate a reiteration of the question (once per question)
                        current_question = self.ask_repeating_question()
                        self.feedback.add_reiteration()
                        if self.repeating_reason == EvaluationType.OFF_TOPIC:
                            self.feedback.remove_irrelevant()
                        elif self.repeating_reason == EvaluationType.CONTRADICTS:
                            self.feedback.remove_contradiction()
                        self.repeating_reason = None
                        repeated = True

                    case 3:  # Select a question from the predefined questions
                        repeated = False
                        current_question = self.ask_selected_question()

                    case _:
                        raise ValueError(f"Cannot assign {self.next_question}.")
            except NoQuestionsLeft:
                logger.info("No questions left, ending the exam early.")
                break

        # Give a feedback to the students
        self.time_manager.append_feedback()
        feedback_rules = self.feedback.construct_feedback(self.student['nominative'])
        logger.info(feedback_rules)
        if self.ai_student:
            import testing.ai_student
            testing.ai_student.write_output(f"[Eval:] {feedback_rules}")

        feedback_query = (
            f"""Gib {self.student['dative']} namens {self.student['name']} mündlich ein konstruktives Feedback in 3 Sätzen für {self.student['possessive']} Leistungen im Anschluss an eine mündliche Prüfung.
            Nutze folgende Informationen zu {self.student['possessive']}n Leistungen:
            {feedback_rules}
            Gib nur das Feedback zurück:"""
        )
        feedback = self.text_generator.get_text(feedback_query)
        feedback = check_feedback(feedback)
        self.speak(feedback)

        # See the student off
        goodbye_query = (
            f"""Verabschiede {self.student['accusative']} namens {self.student['name']} in 1 Satz nach einer mündlichen Prüfung.
            Gib nur die Verabschiedung zurück:"""
        )
        goodbye = self.text_generator.get_text(goodbye_query)
        self.speak(goodbye)

        if self.channel is None:
            delimiter = "-" * 50
            print(f"{delimiter}End!{delimiter}")


class TimeManager:
    """
    Training exam time manager.
    """
    def __init__(self, duration, topic_manager, feedback, turn_cap=TURN_CAP):
        self.remaining_time = duration
        self.topic_manager = topic_manager
        self.last_known_topic = topic_manager.get_topic()
        self.topic_time = duration / len(KE)
        self.correct_answers = 0
        self.feedback = feedback
        self.turn_cap = turn_cap

        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Capped, so that a student who walks away from the microphone or a
        # browser tab that was closed cannot drive the remaining time far into
        # the negative and skew the topic schedule on the way out.
        elapsed_time = min(time.time() - self.start_time, self.turn_cap)
        logger.info("Answer took %.6f seconds.", elapsed_time)
        self.remaining_time = self.remaining_time - elapsed_time
        self.topic_time = self.topic_time - elapsed_time
        logger.info("Remaining time: %.6f seconds (%.6f seconds in this topic).",
                    self.remaining_time, self.topic_time)

    def get_remaining_time(self):
        return self.remaining_time

    def increase_correct_answers(self):
        self.correct_answers += 1

    def append_feedback(self):
        self.feedback.add_feedback(self.correct_answers, self.last_known_topic, self.topic_manager.get_level())

    def check_topic(self):
        """
        Checks if the topic got increased by the QuestionManager and calculates the new time per topic.
        Checks if the time for the current topic ran out and increases the topic.
        """
        # Check if topic got increased or time for topic ran out. The last course
        # unit has no successor, so it never triggers a topic change.
        topic = self.topic_manager.get_topic()
        is_last_topic = self.last_known_topic.value >= len(KE) - 1
        if topic != self.last_known_topic or (self.topic_time <= 0 and not is_last_topic):
            self.append_feedback()

            # Set new topic if time for topic ran out
            if self.topic_time <= 0 and not is_last_topic:
                self.topic_manager.increase_topic()
                topic = self.topic_manager.get_topic()

            # Set new time for topic
            remaining_topics = len(KE) - topic.value
            self.topic_time = self.remaining_time / remaining_topics
            logger.info("Next topic %s for %s seconds.", topic.name, self.topic_time)

            self.last_known_topic = topic
            self.correct_answers = 0
            return True
        return False

    def check_level(self):
        # Check the level
        level = self.topic_manager.get_level()
        if ((level == Level.REMEMBER and self.correct_answers >= 2) or
                (level == Level.APPLY and self.correct_answers >= 1)):
            self.topic_manager.increase_level()
        elif level == Level.REMEMBER:
            return True
        return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    dev_parameters = {"name": "Luna", "time": 10, "female": True, "male": False, "mute": True, "ai": False}
    exam = ExamManager(dev_parameters)
    exam.start_exam()
