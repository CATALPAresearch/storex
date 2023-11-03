import os
from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

REPO = 'LunaticTanuki/german-qg-mT5-small-OOP'
MODEL_PATH = '/home/luna/workspace/german-qg-mT5-small-OOP/trained_model'
CONTEXT = """Ein Literal (von lat. littera, der Buchstabe ) ist eine in der Syntax der Programmiersprache
ausgedrückte Repräsentation eines Objektes. Literale sind somit textuelle Spezifikationen
von Objekten: Wenn der Compiler ein Literal übersetzt, erzeugt er daraus — bei der Über-
setzung! — das entsprechende Objekt im Speicher . Dies steht im Gegensatz zu objekter-
zeugend en Anweisungen eines Programms, denn diese werden erst zur Laufzeit des Pro-
gramms ausgeführt. Da wir uns mit der programmgesteuerten Erzeugung von Objekten
aber erst in der nächsten Kurs einheit systematisch befassen, müssen wir hier zunächst mit
Objekten mit literaler Repräsentation vorlieb nehmen. Wohlgemerkt: Literale repräsentieren
Objekte, es sind nicht selbst welche."""
question = "Was ist ein Literal?"

template = """Use the following pieces of information to answer the user's question in German.
If you don't know the answer, just say that you don't know the answer, don't try to make up an answer.

Context: {context}
Question: {question}

Only returns the helpful answer below and nothing else.
Helpful answer:"""
prompt = PromptTemplate(template=template, input_variables=["context", "question"])

# llm = HuggingFacePipeline.from_model_id(
#          model_id=MODEL_PATH,
#          task="text2text-generation")
llm = HuggingFaceHub(repo_id=REPO)

llm_chain = LLMChain(prompt=prompt,
                     llm=llm)

print(llm_chain.run(CONTEXT))
