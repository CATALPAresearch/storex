import os
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


class AnswerGenerator:
    def __init__(self):
        model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

        answer_template = ("Du erstellst Musterantworten für eine Prüfung an einer deutschen Universität."
                           "[INST] Schreibe eine Antwort für die Frage: '{question}'."
                           "Nutze dafür nur Informationen aus dem folgenden Text: "
                           "{context} [/INST]")

        summary_template = """[INST] Du erstellst Prüfungsfragen und Musterantworten an einer deutsche Universität.
        Schreibe eine Frage und dazugehörige Antwort zu dem folgenden Text:
        {context} [/INST]"""

        answer_prompt = PromptTemplate(template=answer_template, input_variables=['context', 'question'])
        summary_prompt = PromptTemplate(template=summary_template, input_variables=['context'])

        llm = HuggingFaceHub(repo_id=model_id, model_kwargs={'max_new_tokens': 512, 'raw_response': True})
        self.answer_chain = LLMChain(prompt=answer_prompt,
                                     llm=llm)
        self.summary_chain = LLMChain(prompt=summary_prompt,
                                      llm=llm)

    def get_answer(self, context, question):
        query = {'context': context, 'question': question}
        return self.answer_chain.run(query)

    def get_summary(self, context):
        query = {'context': context}
        return self.summary_chain.run(query)


test_context = "Die in anderen Programmiersprachen vorhandenen Literale (oder Schlüsselwörter), wie true, false und nil (oder null), die ebenfalls atomare Objekte repräsentieren, sind in SMALLTALK nicht vorhanden. Damit sind sie nicht Literale, sondern sogenannte Pseudo-Variablen. Der Grund dafür scheint pragmatischer Natur zu sein: SMALLTALK hat keine Schlüsselwörter, und indem true, false und nil als Pseudo-Variablen betrachtet werden, müssen sie vom Compiler nicht syntaktisch von Variablen unterschieden werden. Sie repräsentieren jeweils ein entsprechendes Objekt, das in anderen Sprachen wiederum Werte sind."
test_question = "Was sind Pseudo-Variablen in SMALLTALK?"

answer_generator = AnswerGenerator()
print(answer_generator.get_answer(test_context, test_question))
print(answer_generator.get_summary(test_context))
