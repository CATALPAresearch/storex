import time
import evaluation
from questions import get_questions
from utils import colours
from utils.helpers import QuestionType, FeedbackType
from audio import text_to_speech, speech_recognition

import logging
logger = logging.getLogger()

# Global variables
last_question = None
next_question = None


def talk(text):
    # Output teacher text via speaker and terminal
    text_to_speech.get_audio(text)
    colours.print_blue(text)


def ask_question(question):
    # Output question via speaker and terminal
    talk(question)
    # Set global last question
    global last_question
    last_question = question


def get_answer():
    answer = speech_recognition.get_audio_to_text()
    print(f"Deine Antwort lautet: {answer}")
    return answer


def setup(exam_parameters):
    """
    Set the students parameters, greet the student and start the timer.

    :param exam_parameters: Dictionary with parameters for the exam.

    :return end_time: Calculated time to end the exam.
    """
    # Set student parameters
    student_name = exam_parameters["name"]
    address_form = ''
    if exam_parameters["female"]:
        address_form = "Frau"
    elif exam_parameters["male"]:
        address_form = "Herr"

    # Greet the student
    greeting = (f"Guten Tag {address_form} {student_name}!".replace('  ', ' '))
    talk(greeting)

    # Set duration of the exam
    duration = int(exam_parameters["time"]) * 60
    start_time = time.time()
    end_time = start_time + duration
    return end_time


def predef_question():
    # Get predefined question TODO: Probabilities, not same question twice
    predefined = get_questions.question_ke6()
    ask_question(predefined["question"])

    answer = get_answer()
    get_feedback(predefined["answer"], answer)


def specific_question(target):
    predef_question()
    # TODO: Find answer for target keyword in database
    # TODO: Generate question for target keyword
    # specific = generate_questions
    # ask_question(specific["question"])
    # answer = get_answer()
    # get_feedback(specific["answer"], answer)


def get_feedback(correct_answer, student_answer):
    result = evaluation.evaluate_answer(correct_answer, student_answer)
    logger.info(f"Result: {result.name}")

    # Give feedback and set next question type
    global next_question
    match result.value:
        case 0:  # Correct answer
            next_question = QuestionType.PREDEFINED
        case 1:  # No or too short answer
            talk("Ich habe Sie nicht verstanden. Bitte wiederholen Sie Ihre Antwort.")
            next_question = QuestionType.REPEAT
        case 2:  # Off-topic answer
            talk('Sie haben das Thema leider verfehlt.')
            next_question = QuestionType.REPEAT
        case 3:  # Contradicting answer
            talk('Mit dieser Antwort wiedersprechen Sie dem Kurstext.')
            next_question = QuestionType.REPEAT
        case 4:  # The answer is missing topics
            # TODO: Get missing topics and give feedback
            next_question = QuestionType.GENERATED
        case _:
            raise ValueError(f"Cannot assign {result}.")


def start_exam(exam_parameters):
    # Set up the exam
    end_time = setup(exam_parameters)
    global next_question

    # TODO: Ask first question
    # first_question = "Erzählen Sie mir etwas zu objektorientierter Programmierung."
    # first_correct_answer = "..."
    # ask_question(first_question)
    # first_student_answer = get_answer()
    # get_feedback(first_correct_answer, first_student_answer)

    next_question = QuestionType.PREDEFINED
    targets = []
    repeated = False

    # TODO: Time answer
    # TODO: Add calculation time to end_time

    # Match next question type while the exam time is not up
    while time.time() < end_time:
        logger.info(f"The next question should be: {next_question.name}")
        match next_question.value:
            case 0:  # Ask predefined question
                predef_question()
            case 1:  # Generate specific question
                specific_question(targets)
            case 2:  # Repeat question once due to silence or no entailment
                if repeated is False:
                    talk(last_question)
                    repeated = True
                else:
                    next_question = QuestionType.GENERATED
                    repeated = False
            case _:
                raise ValueError(f"Cannot assign {next_question}.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.disabled = False

    start_exam({"name": "Luna", "time": 10, "female": False, "male": False, "logging": True})
