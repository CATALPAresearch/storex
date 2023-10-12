import evaluation
import time

# TODO: Input name, gender and time for exam (default: 25 min) in the console as flags
print("Bitte geben Sie Ihren Namen an:")
student_name = input()
gender = 'Frau'
duration = 25  # Duration in minutes
duration *= 60  # Duration in seconds

start_time = time.time()
end_time = start_time + duration

print("Guten Tag", gender, student_name + "! Erzählen Sie mir etwas zu objektorientierter Programmierung.")

# TODO: Time answer
answer = input()

correct = evaluation.evaluate_free_answer(answer)
if correct:
    print("Correct! Next question:")
else:
    print("Wrong! Next question:")

while time.time() < end_time:
    pass
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
