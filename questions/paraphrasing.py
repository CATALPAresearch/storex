"""
Class for paraphrasing questions.
"""
import hf_token

from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate


class QuestionParaphraser:
    def __init__(self):
        """
        Initializes the question paraphraser.
        """
        # Load prompt from template
        template = ("Du bist ein Professor an einer deutschen Universität. "
                    "Erstelle eine einfache Prüfungsfrage zu dieser Antwort: {context}")
        prompt = PromptTemplate(template=template, input_variables=["context"])
        # Load question generation model
        llm = HuggingFaceHub(repo_id='LunaticTanuki/oop-de-qg-flan-t5-base-v6', model_kwargs={'max_new_tokens': 250})
        # Create chain for question generation
        self.llm_chain = LLMChain(prompt=prompt, llm=llm)

    def paraphrase(self, answer):
        """
        Generates a new question for a given answer.
        """
        return self.llm_chain.run(answer)
