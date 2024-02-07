import os
import torch

from langchain.chains import LLMChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS

import logging
logger = logging.getLogger()

# TODO: Remove Token
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


class QuestionParaphraser:
    def __init__(self):
        """
        Initializes
        """
        # Load prompt from template
        template = ("Du bist ein Professor an einer deutschen Universität. "
                    "Erstelle eine einfache Prüfungsfrage zu dieser Antwort: {context}")
        prompt = PromptTemplate(template=template, input_variables=["context"])
        # Load question generation model
        llm = HuggingFaceHub(repo_id='LunaticTanuki/oop-de-qg-flan-t5-base-v6', model_kwargs={'max_new_tokens': 250})
        # Create chain for question generation
        self.llm_chain = LLMChain(prompt=prompt, llm=llm)

        # Load vectorstore embeddings
        directory = os.path.dirname(os.path.dirname(__file__))
        vectorstore = (os.path.join(directory, 'data/vectorStore'))
        device = "cuda" if torch.cuda.is_available() else "cpu"
        embedding_model = HuggingFaceEmbeddings(model_name='paraphrase-multilingual-MiniLM-L12-v2',
                                                model_kwargs={'device': device})
        # Load database
        self.db = FAISS.load_local(vectorstore, embedding_model)

    def paraphrase(self, answer):
        """
        Generates a new question for the context of a given answer.
        """
        context = self.get_context(answer, 1)
        return self.llm_chain.run(context)

    def get_context(self, answer, k):
        """
        Retrieves the k most fitting context documents for the given query.
        Returns the concatenated context.
        """
        # Get context for query
        context_docs = self.db.similarity_search(answer, k=k)
        context_docs = [docs for docs in context_docs if not docs.page_content[0].isdigit()]

        context = ' '.join([doc.page_content for doc in context_docs])
        logger.debug(f"Context: {context}\n"
                     f"For answer: {answer}")
        return context
