import csv
import glob
import os

from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate

directory = os.path.dirname(os.path.dirname(__file__))
CONTEXT_PATH = os.path.join(directory, 'data/chapters_raw')
OUTPUT_FILE = os.path.join(directory, 'data/processed/chapters_automated.csv')

repo_id = 'tiiuae/falcon-40b'
llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperatur": 0, "max_length": 1000})

template = """Proofread and edit this text for errors: {context}

Here's the corrected and edited text in German:"""

prompt = PromptTemplate(template=template, input_variables=["context"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

for file in glob.glob(CONTEXT_PATH + '/*.txt'):
    with open(file, 'r') as txt_file:
        input_context = ''.join(txt_file.readlines())
        edited_context = llm_chain.run(input_context)
        with open(OUTPUT_FILE, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(edited_context)

# Few-Shot Prompt
examples = [
    {
        "context": 'Während atomare Objekte grundsätzlich nicht veränderbar sind (welchen Sinn hätte es beispielsweise, aus einer "1" eine "2" zu machen oder aus einem "a" ein "b"?), gilt das zunächst nicht für zusammengesetzte Objekte. Es ist leicht vorstellbar (und auch grundsätzlich sinnvoll), in einem Array-Objekt eine Komponente durch eine andere zu ersetzen. Die Frage ist jedoch, ob dies auch für Array-Objekte gilt, die aus Literalen erzeugt wurden. Soll es erlaubt sein, dass das zusammengesetzte Objekt, das aus dem Array-Literal #(1 2 3) hervorgegangen ist, durch ein Programm so verändert wird, dass es nicht mehr seiner (ursprünglichen) literalen Repräsentation im Programm entspricht? Dies ist Ansichtssache und wird zumindest für String- und Array-Literale von verschiedenen SMALLTALK-Dialekten unterschiedlich gehandhabt. Objekte, die aus Symbolliteralen hervorgegangen sind, sollten dagegen nie veränderbar sein. Grundsätzlich sind zusammengesetzte Objekte in SMALLTALK jedoch veränderbar. Dies ist eine Voraussetzung dafür, dass Objekte einen Zustand haben können (siehe Kapitel 3), was wiederum die objektorientierte Programmierung zu einer Form der imperativen Programmierung macht. Aufgrund zunehmender funktionaler Einflüsse auf die objektorientierte Programmierung findet man jedoch auch immer mehr Sprachen, die unveränderliche Objekte anbieten, wie beispielsweise SCALA.',
        "question": "Warum sind atomare Objekte grundsätzlich nicht veränderbar?",
        "answer": 'Atomare Objekte sind grundsätzlich nicht veränderbar, da es keinen Sinn ergibt, sie zu verändern. Zum Beispiel macht es keinen Sinn, aus einer "1" eine "2" zu machen.'
    }
]
example_prompt = PromptTemplate(input_variables=["context", "question", "answer"], template="What are questions and answers for this paragraph: {context} \n {question} and {answer}")

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="What are questions and answers for this paragraph: {input}",
    input_variables=["input"]
)

prompt.format(input="")
