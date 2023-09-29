from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain

MODEL_PATH = '/home/luna/workspace/Dialogsteuerung/models/trainedT5'
CONTEXT = """Ein Literal (von lat. littera, der Buchstabe ) ist eine in der Syntax der Programmiersprache
ausgedrückte Repräsentation eines Objektes. Literale sind somit textuelle Spezifikationen
von Objekten: Wenn der Compiler ein Literal übersetzt, erzeugt er daraus — bei der Über-
setzung! — das entsprechende Objekt im Speicher . Dies steht im Gegensatz zu objekter-
zeugend en Anweisungen eines Programms, denn diese werden erst zur Laufzeit des Pro-
gramms ausgeführt. Da wir uns mit der programmgesteuerten Erzeugung von Objekten
aber erst in der nächsten Kurs einheit systematisch befassen, müssen wir hier zunächst mit
Objekten mit literaler Repräsentation vorlieb nehmen. Wohlgemerkt: Literale repräsentieren
Objekte, es sind nicht selbst welche."""


template = """Question: {context}
Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["context"])

llm = HuggingFacePipeline.from_model_id(
         model_id=MODEL_PATH,
         task="text2text-generation")

llm_chain = LLMChain(prompt=prompt,
                      llm=llm)

question = """Ein Literal (von lat. littera, der Buchstabe ) ist eine in der Syntax der Programmiersprache
ausgedrückte Repräsentation eines Objektes."""
print(llm_chain.run(question))
