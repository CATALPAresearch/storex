import time
import evaluation
from questions import get_questions
from utils import colours
from utils.helpers import QuestionType
from audio import text_to_speech, speech_recognition


def ask_question(question):
    text_to_speech.get_audio(question)
    colours.print_blue(question)


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
    ask_question(greeting)

    # Set duration of the exam
    duration = exam_parameters["time"] * 60
    start_time = time.time()
    end_time = start_time + duration
    return end_time


def predef_question():
    # Get predefined question TODO: Probabilities
    question_keywords = get_questions.question_ke6()
    ask_question(question_keywords["question"])
    correct_answer = "Das Fragile-Base-Class-Problem bezieht sich auf eine Gruppe von Problemen in der Vererbung von Klassen. Wenn zwischen einer Klasse und ihren Subklassen aufgrund der Vererbung von Eigenschaften starke Abhängigkeiten bestehen, können Änderungen an der Basisklasse zu unerwarteten und unerwünschten Auswirkungen in der abgeleiteten Klasse führen."

    answer = get_answer()
    evaluation.evaluate_predefined_question(question_keywords, answer)
    evaluation.evaluate_answer(correct_answer, answer)

    missing_keywords = []

    next_question = QuestionType.GENERATED if missing_keywords else QuestionType.PREDEFINED

    return next_question, missing_keywords


def specific_question(answer):
    # Get specific question TODO: Generate question for targeted answer
    question = "Was ist das Fragile-Base-Class-Problem?"
    print(question)
    # TODO: Find answer in database without LLM
    # result = getAnswerFromDB.retrieve_result(question)
    # answer = result["result"]
    correct_answer = "Das Fragile-Base-Class-Problem bezieht sich auf eine Gruppe von Problemen in der Vererbung von Klassen. Wenn zwischen einer Klasse und ihren Subklassen aufgrund der Vererbung von Eigenschaften starke Abhängigkeiten bestehen, können Änderungen an der Basisklasse zu unerwarteten und unerwünschten Auswirkungen in der abgeleiteten Klasse führen."

    qa_pair = {
        'question': question,
        'answer': correct_answer
    }

    print(qa_pair['answer'])
    answer = input()
    evaluation.evaluate_answer(qa_pair, answer)

    print("Your answer is acceptable. A good answer would be:", qa_pair['answer'])
    next_question = QuestionType.PREDEFINED

    return next_question


def start_exam(exam_parameters):
    # Set up the exam
    # end_time = setup(exam_parameters)

    # TODO: Ask first question
    # first_question = "Erzählen Sie mir etwas zu objektorientierter Programmierung."
    # ask_question(first_question)
    # answer = get_answer()

    next_question = QuestionType.PREDEFINED
    targets = []

    # TODO: Time answer
    # TODO: Add calculation time to end_time
    # answer = input()
    # correct = evaluation.evaluate_free_answer(answer)
    # if correct:
    #     print("Nächste Frage:")

    # while time.time() < end_time:
    # TODO: While time not up
    # TODO: Question-Answer-Generation

    match next_question.value:
        case 0:  # Ask predefined question
            next_question, targets = predef_question()
        case 1:  # Generate specific question
            next_question = specific_question(targets)
        case 2:  # Check due to silence
            ask_question("Ich habe Sie nicht verstanden. Bitte wiederholen Sie Ihre Antwort.")
            # TODO: Repeat evaluation. Silence counter for feedback?
        case _:
            pass


if __name__ == "__main__":
    start_exam({"name": "Luna", "time": 10, "female": False, "male": False, "logging": True})
