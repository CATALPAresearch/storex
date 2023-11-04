import print_colors as pc
import text_to_speech
import evaluation
import getQuestions
import getAnswerFromDB

import time


def start_exam(exam_parameters):
    evaluation.setup_stopwords()
    student_name = exam_parameters["name"]
    address_form = ''
    if exam_parameters["female"]:
        address_form = "Frau"
    elif exam_parameters["male"]:
        address_form = "Herr"
    duration = exam_parameters["time"] * 60

    start_time = time.time()
    end_time = start_time + duration

    greeting = (f"Guten Tag {address_form} {student_name}! Erzählen Sie mir etwas zu objektorientierter Programmierung."
                .replace('  ', ' '))
    text_to_speech.get_audio(greeting)
    pc.print_blue(greeting)

    # TODO: Time answer
    # answer = input()
    # correct = evaluation.evaluate_free_answer(answer)
    # if correct:
    #     print("Nächste Frage:")

    # while time.time() < end_time:
    # TODO: While time not up
    # TODO: Question-Answer-Generation

    # Get predefined question
    question_keyword = getQuestions.question_ke6()
    print(question_keyword['question'])

    answer = input()
    evaluation.evaluate_predefined_question(question_keyword, answer)

    # Get specific question
    question = "Was ist das Fragile-Base-Class-Problem?"  # questions.question_ke6()
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


if __name__ == "__main__":
    start_exam({"name": "Luna", "time": 10, "female": False, "male": False, "logging": True})
