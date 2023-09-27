from pprint import pprint
from lmqg import TransformersQG

# initialize model
model = TransformersQG(language='de', model='lmqg/mt5-small-dequad-qg')
# paragraph to generate pairs of question and answer
context = "Wie bereits erwähnt sind Objekte im Speicher abgelegte Daten. Dabei ist jedes Objekt an " \
          "genau einer Stelle im Speicher abgelegt: Es wird damit durch seine Speicherstelle eindeutig " \
          "identifiziert. Aufgrund dieser eindeutigen Identifizierbarkeit spricht man auch von der Identität " \
          "eines Objekts; sie kann aus technischer Sicht mit der Speicherstelle, an der das Objekt " \
          "abgelegt ist, gleichgesetzt werden. Da keine zwei Objekte an derselben Stelle abgelegt werden " \
          "können, haben auch keine zwei Objekte dieselbe Identität."
# model prediction
question_answer = model.generate_qa(context)
# the output is a list of tuple (question, answer)
pprint(question_answer)
