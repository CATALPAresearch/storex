import os
from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

# TODO: Remove Token
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


class QuestionParaphraser:
    def __init__(self):
        """
        Initializes
        """
        # Load prompt from template
        template = """Write a question from this paragraph: {context}"""
        prompt = PromptTemplate(template=template, input_variables=["context"])
        # Load question generation model
        llm = HuggingFaceHub(repo_id='LunaticTanuki/oop-de-qg-flan-t5-base')  # TODO: Try other models
        # Create chain for question generation
        self.llm_chain = LLMChain(prompt=prompt, llm=llm)

    def paraphrase(self, answer):
        """
        Generates a new question for a given answer.
        """
        return self.llm_chain.run(answer)
