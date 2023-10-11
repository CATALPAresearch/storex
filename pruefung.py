import evaluation

print("Guten Tag! Erzählen Sie mir etwas zu objektorientierter Programmierung.")

# TODO: Time answer
answer = input()

correct = evaluation.evaluate_free_answer(answer)
if correct:
    print("Correct! Next question:")
else:
    print("Wrong! Next question:")

# TODO: While time not up
# TODO: Question-Answer-Generation
qa_pair = {
    'question': 'Was ist der Unterschied zwischen Gleichheit und Identität von Objekten?',
    'answer': 'Gleichheit bezieht sich in der Regel auf das Erscheinungsbild oder die Bedeutung von Objekten und wird'
              'in SMALLTALK durch den Gleichheitsoperator = getestet. Identität wird in SMALLTALK durch == getestet und'
              'bezieht sich darauf, ob zwei Objekte dasselbe Objekt im Speicher repräsentieren.'
}

print(qa_pair['question'])
answer = input()
evaluation.evaluate_answer(qa_pair, answer)
