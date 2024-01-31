import os

from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


class TextGenerator:
    def __init__(self):
        template = (""""[INST] Du bist ein Professor an einer deutschen Universität. Du hältst online mündliche Prüfungen ab.
                    {query}[/INST]""")

        prompt = PromptTemplate(template=template, input_variables=['query'])

        llm = HuggingFaceHub(repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
                             model_kwargs={'max_new_tokens': 512, 'raw_response': True})

        self.llm_chain = LLMChain(prompt=prompt,
                                  llm=llm)

    def get_text(self, query):
        return self.llm_chain.run(query)
