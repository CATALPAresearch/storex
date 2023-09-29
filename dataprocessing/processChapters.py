import glob
import csv

from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

CONTEXT_PATH = '/home/luna/workspace/Dialogsteuerung/data/chapters'
OUTPUT_FILE = '/home/luna/workspace/Dialogsteuerung/data/chapters/processed_chapters/chapters.csv'
TEST_CONTEXT = """1.6 Zuweisung
Damit eine Variable ein Objekt bezeichnet, muss ihr dieses durch eine sog. Zuweisung , in
anderen Kontexten auch Wertzuweisung genannt, zugeordnet werden. Ursprünglich
wurde als Zuweisungsoperator das Symb ol „“ gewählt; wegen der mangelnden Verfüg-
barkeit auf Tastaturen wurde es jedoch in den meisten SMALLTALK -Implementierungen durch
das aus ALGOL und PASCAL bekannte := ( englisch als „ becomes “ gelesen) ersetzt.7 Die
Variable lieblingszahl bezeichnet also i n Folge der Zuweisung
ein Objekt „2“ (in der Zuweisung repräsentiert durch das Literal 2). Nach einer Zuweisung
= für die Zuweisung steht, darf als eine der Tragödien in der Geschichte der Programmiersprachen
angesehen werden. Ich möchte nicht wissen, wie viele fatale Fehler auf die dadurch provozierte Ver-
wechselung von Test auf Gleichheit und Zuweisung zurückzuführen sind. lokale und globale
bezeichnen x und y das gleiche Objekt (genau welches ist hier nicht er-
sichtlich); ob sie auch dasselbe bezeichnen, hängt von der Semantik der
Variablen ab. Man beachte, dass in SMALLTALK (anders als in typisierten
Sprachen) aus Sicht des Compilers nichts dagegen spricht, der Variable x erst eine Zahl und
dann einen String zuzuweis en. Auch Array -Literale können jeder beliebigen Variable zuge-
wiesen werden.
"""
repo_id = 'tiiuae/falcon-40b'

# llm = OpenAI(temperature=.7)
llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperatur": 0, "max_length": 1000})

template = """Proofread and edit this text for errors: {context}

Here's the corrected and edited text:"""

prompt = PromptTemplate(template=template, input_variables=["context"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

edited_text = llm_chain.run(TEST_CONTEXT)
print(edited_text)
exit(0)

for file in glob.glob(CONTEXT_PATH + '/*.txt'):
    with open(file, 'r') as txt_file:
        input_context = ''.join(txt_file.readlines())
        edited_context = llm_chain.run(input_context)
        with open(OUTPUT_FILE, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(edited_context)
