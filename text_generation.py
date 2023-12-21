import os

from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '***REMOVED***'


class TextGenerator:
    def __init__(self):
        repo = "mistralai/Mixtral-8x7B-Instruct-v0.1"

        template = ("Du bist ein Professor an einer deutschen Universität."
                    "{query}")

        prompt = PromptTemplate(template=template, input_variables=['query'])
        llm = HuggingFaceHub(repo_id=repo)

        self.llm_chain = LLMChain(prompt=prompt,
                                  llm=llm)

    def get_text(self, query):
        return self.llm_chain.run(query)
