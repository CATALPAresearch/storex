"""
Class for generating questions.
"""
import os
import torch

from langchain.chains import LLMChain
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

        # Load question model and create a question chain
        question_template = """Du erstellst Prüfungsfragen an einer deutsche Universität.
        Schreibe eine Frage zu dem folgenden Text:
        {context}"""
        question_prompt = PromptTemplate(template=question_template, input_variables=["context"])
        question_llm = HuggingFaceHub(repo_id='LunaticTanuki/oop-de-qg-flan-t5-base',
                                      model_kwargs={'max_new_tokens': 250})  # TODO: Why is 250 max?
        self.question_chain = LLMChain(prompt=question_prompt, llm=question_llm)

        self.answer_generator = AnswerGenerator()

        # Load question-answer model and create a question-answer chain
        question_answer_template = """[INST] Du erstellst Prüfungsfragen und Musterantworten für mündliche Prüfungen
        an einer deutsche Universität.
        Schreibe eine Frage und dazugehörige Antwort zu dem folgenden Text:
        {context} [/INST]"""
        question_answer_prompt = PromptTemplate(template=question_answer_template, input_variables=['context'])
        question_answer_llm = HuggingFaceHub(repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
                                             model_kwargs={'max_new_tokens': 512, 'raw_response': True})
        self.question_answer_chain = LLMChain(prompt=question_answer_prompt, llm=question_answer_llm)

    def generate_question_answer(self, keyword, k=2):
        """
        Generates a question-answer pair for the context from the given keyword.
        """
        # Get a context for the keyword
        context = self.get_context(keyword, k)
        logger.debug(f"Context: {context}")

        # Generate a question and answer from the context
        question_answer = self.question_answer_chain.run(context)
        logger.debug(f"Question and answer: {question_answer}")

        # Find the question and the answer in the model output
        question_line = question_answer.split('\n', 1)[0]
        question = question_line.split(': ')[1].strip()
        answer_lines = question_answer.split('\n', 1)[1]
        answer = answer_lines.split(': ')[1].strip()

        question_dict = {'question': question, 'answer': answer}
        return question_dict

    def generate_question(self, keyword, k=2):
        """
        Generates a question for the context from the given keyword.
        """
        # Get a context for the keyword
        context = self.get_context(keyword, k)
        logger.debug(f"Context: {context}")

        # Generate a question from the context
        question = self.question_chain.run(context)

        # Get the answer TODO: Extract from context or summarize for End2end, pipeline or multitask
        answer = self.answer_generator.get_answer(context, question)
        logger.debug(f"Question: {question}\n Answer: {answer}")

        question_dict = {'question': question, 'answer': answer}
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


class AnswerGenerator:
    def __init__(self):
        model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

        template = ("Du erstellst Musterantworten für eine Prüfung an einer deutschen Universität."
                    "[INST] Schreibe eine Antwort für die Frage: '{question}'."
                    "Nutze dafür nur Informationen aus dem folgenden Text: "
                    "{context} [/INST]")

        prompt = PromptTemplate(template=template, input_variables=['context', 'question'])
        llm = HuggingFaceHub(repo_id=model_id, model_kwargs={'max_new_tokens': 512, 'raw_response': True})
        self.llm_chain = LLMChain(prompt=prompt,
                                  llm=llm)

    def get_answer(self, context, question):
        query = {'context': context, 'question': question}
        return self.llm_chain.run(query)
