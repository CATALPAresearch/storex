"""
Class for generating questions.
"""
import os
import torch

from langchain.chains import LLMChain, RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from utils import preprocessing

import logging
logger = logging.getLogger()


# TODO: Remove api token
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


class QuestionGenerator:
    def __init__(self):
        """
        Initializes
        """
        # Load vectorstore embeddings
        directory = os.path.dirname(os.path.dirname(__file__))
        vectorstore = (os.path.join(directory, 'data/vectorStore'))
        device = "cuda" if torch.cuda.is_available() else "cpu"
        embedding_model = HuggingFaceEmbeddings(model_name='paraphrase-multilingual-MiniLM-L12-v2',
                                                model_kwargs={'device': device})
        # Load database
        self.db = FAISS.load_local(vectorstore, embedding_model)

        # Load prompt from template
        template = """Write a question from this paragraph: {context}"""
        self.prompt = PromptTemplate(template=template, input_variables=["context"])
        # Load question generation model
        self.llm = HuggingFaceHub(repo_id='LunaticTanuki/oop-de-qg-flan-t5-base')  # TODO: Try other models
        # Create chain for question generation
        self.question_chain = LLMChain(prompt=self.prompt, llm=self.llm)

    def get_question_from_retriever(self, query, k=4):
        """
        TODO: remove this function?
        Retrieve context for a given topic from a FAISS database.

        :param query:
        :param k:

        :return result: Answer to the question.
        :return source_documents: Source documents from the database.
        """
        # Set up as generic retriever
        retriever = self.db.as_retriever(search_type="similarity", search_kwargs={'k': k})

        # Create the chain for question answering
        answer_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",  # stuff, map_reduce or map_rerank with k=10
            retriever=retriever,  # context_docs = db.similarity_search(query, k=4)
            return_source_documents=True,
            chain_type_kwargs={'prompt': self.prompt}
        )

        result = answer_chain({'query': query})
        result = result["result"]  # Sources at: result["source_documents"]
        logger.debug(f"Question: {result}")
        return result

    def generate_question(self, keyword, k=2):
        """
        Generates a question for the context from the given keyword.
        """
        # Get a context for the keyword
        context = self.get_context(keyword, k)
        logger.debug(f"Context: {context}")

        # Set the answer TODO: Extract from context or summarize for End2end, pipeline or multitask
        answer = context
        # Generate a question from the context
        question = self.question_chain.run(context)
        logger.debug(f"Question: {question}")

        # Get technical terms and common words from the paragraph
        keywords = preprocessing.extract_keywords(self.get_context(keyword, k))  # TODO: How many keywords?
        logger.info(f"Keywords from context: {keywords}")
        if keyword not in keywords['terms']:
            keywords['terms'].append(keyword)

        question_dict = {'question': question, 'answer': answer, 'keywords': keywords}
        return question_dict

    def get_context(self, query, k):
        """
        Retrieves the k most fitting context documents for the given query.
        Returns the concatenated context.
        """
        # TODO: Topic extraction (maybe different database splitting, e.g. not at \n?)
        # Get context for query
        context_docs = self.db.similarity_search(query, k=k)
        context_docs = [docs for docs in context_docs if not docs.page_content[0].isdigit()]
        # TODO: Process context?

        context = ' '.join([doc.page_content for doc in context_docs])
        return context
