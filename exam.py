import evaluation
import time

# import nltk
# nltk.download('stopwords')


def start_exam(exam_parameters):
    student_name = exam_parameters["name"]
    address_form = ''
    if exam_parameters["female"]:
        address_form = "Frau"
    elif exam_parameters["male"]:
        address_form = "Herr"
    duration = exam_parameters["time"] * 60

    start_time = time.time()
    end_time = start_time + duration

    print("Guten Tag", address_form, student_name + "! Erzählen Sie mir etwas zu objektorientierter Programmierung.")

    # TODO: Time answer
    answer = input()

    correct = evaluation.evaluate_free_answer(answer)
    if correct:
        print("Correct! Next question:")
    else:
        print("Wrong! Next question:")

    # while time.time() < end_time:
    # TODO: While time not up
    # TODO: Question-Answer-Generation
    qa_pair = {
        'question': 'Was ist der Unterschied zwischen Gleichheit und Identität von Objekten?',
        'answer': """Gleichheit: Erscheinungsbild oder Bedeutung von Objekten
                     Identität: Speicher Repräsentation."""
    }

    print(qa_pair['question'])
    # answer = input()
    answer = """Gleichheit bezieht sich in der Regel auf das Erscheinungsbild oder die Bedeutung von Objekten und Identität
                bezieht sich darauf, ob zwei Objekte dasselbe Objekt im Speicher repräsentieren."""
    evaluation.evaluate_answer(qa_pair, answer)
    print("Your answer is acceptable. A good answer would be:", qa_pair['answer'])


if __name__ == "__main__":
    start_exam({"name": "Luna", "time": 10, "female": True, "male": False})
