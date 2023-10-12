from langchain.prompts import StringPromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA

from langchain.agents import AgentExecutor, LLMSingleActionAgent, AgentOutputParser

from langchain import LLMChain

from typing import Union
from langchain.schema import AgentAction, AgentFinish
import re
import langchain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.docstore.document import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


DATA_PATH = '/home/luna/workspace/Dialogsteuerung/data/pdf'
VECTOR_STORE = '/home/luna/workspace/Dialogsteuerung/data/vectorStore'
MODEL_PATH = '/home/luna/workspace/llama.cpp/models/OpenBuddy/openbuddy-13b-v7-q4_K.bin'
MODEL_TYPE = 'llama'

template = """Come up with Question-Answer pairs for the following paragraph in German as best you can,
speaking as a teacher in computer science. Use the following information:

{context}

Use the following format:
Context: the paragraph containing the answer
Question: the input question you must answer
Answer: the final answer to the question

Question: {question}
Context: {context}
"""


def split_text():
    """
    Split up a text document.
    """
    loader = DirectoryLoader(DATA_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)  # 2230 parts
    docs = [Document(page_content=t) for t in texts[:len(texts)]]
    return docs


# Set up a prompt template
class CustomPromptTemplate(StringPromptTemplate):
    template: str


def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vector stores
    """
    prompt = CustomPromptTemplate(
        template=template,
        input_variables=['context', 'question'])
    return prompt


class CustomOutputParser(AgentOutputParser):
    """

    """
    def parse(self, llm_output: str) -> Union[AgentAction, AgentFinish]:
        # Check if agent should finish
        if "Answer:" in llm_output:
            return AgentFinish(
                # Return values is generally always a dictionary with a single `output` key
                # It is not recommended to try anything else at the moment :)
                return_values={"output": llm_output.split("Answer:")[-1].strip()},
                log=llm_output,
            )


def load_output_parser():
    output_parser = CustomOutputParser()
    return output_parser


def load_llm():
    llm = CTransformers(
        model=MODEL_PATH,
        model_type=MODEL_TYPE,
        max_new_tokens=512,
        temperature=0.5
    )
    return llm


def retrival_qa_chain(llm, prompt, db):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={'k': 2}),
        return_source_documents=True,
        chain_type_kwargs={'prompt': prompt}
    )

    return qa_chain


def qa_bot():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(VECTOR_STORE, embeddings)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrival_qa_chain(llm, qa_prompt, db)

    return qa


def final_result(query):
    qa_result = qa_bot()
    response = qa_result({'query': query})
    return response


if __name__ == '__main__':
    pass
