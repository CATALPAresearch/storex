import os
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

REPO = 'LunaticTanuki/oop-de-qg-flan-t5-base'
CONTEXT = ('Bei größeren Programmen kann das Bedürfnis entstehen, ein Programm nach mehreren Kriterien gleichzeitig '
           'zu strukturieren, da verschiedene Vererbungshierarchien oder andere Strukturierungskriterien '
           'gleichzeitig relevant sein können. Die Trennung der Belange, auch als Separation of Concerns bekannt, '
           'wird in der objektorientierten Programmierung als unzureichend unterstützt angesehen, da es schwer ist, '
           'verschiedene Aspekte eines Systems sauber voneinander zu trennen.')

template_qg = """Write a question from this paragraph: {context}"""
template_ag = """Use the following pieces of information to answer the user's question in German.
If you don't know the answer, just say that you don't know the answer, don't try to make up an answer.

Context: {context}
Question: {question}

Only returns the helpful answer below and nothing else.
Helpful answer:"""

prompt = PromptTemplate(template=template_qg, input_variables=["context"])

# llm = HuggingFacePipeline.from_model_id(
#          model_id=MODEL_PATH,
#          task="text2text-generation")
llm = HuggingFaceHub(repo_id=REPO)

llm_chain = LLMChain(prompt=prompt,
                     llm=llm)

print(llm_chain.run(CONTEXT))
