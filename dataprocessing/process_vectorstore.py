import os
import re

import torch

from langchain.document_loaders import PyPDFLoader, DirectoryLoader, TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

directory = os.path.dirname(os.path.dirname(__file__))
PDF_PATH = os.path.join(directory, 'data/pdf')
TXT_PATH = os.path.join(directory, 'data/chapters_processed')
DB_FAISS_PATH = os.path.join(directory, 'data/vectorStore')

# PDF_DB_FAISS_PATH = os.path.join(DB_FAISS_PATH, 'from_pdf')
# TXT_DB_FAISS_PATH = os.path.join(DB_FAISS_PATH, 'from_txt')


def get_doc_from_pdf():
    """
    Read pdf documents.

    :return documents: Read pdf documents.
    """
    loader = DirectoryLoader(PDF_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents


def get_doc_from_txt():
    """
    Read textfiles.

    :return documents: Read textfiles.
    """
    loader = DirectoryLoader(TXT_PATH, glob='*.txt', loader_cls=TextLoader)
    documents = loader.load()
    return documents


def create_vector_db(documents):
    """
    Create vector database from text documents.

    :param documents: Text documents to create the vector store from.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
    split_text = text_splitter.split_documents(documents)
    # docs = [langchain.docstore.document.Document(page_content=t) for t in split_text[:len(split_text)]]

    embeddings = HuggingFaceEmbeddings(model_name='paraphrase-multilingual-MiniLM-L12-v2',
                                       # Or: model_name='LLukas22/all-MiniLM-L12-v2-embedding-all',
                                       model_kwargs={'device': device})

    db = FAISS.from_documents(split_text, embeddings)
    db.save_local(DB_FAISS_PATH)
    print(f"Database saved to {DB_FAISS_PATH}")


def process_doc(documents):
    """
    Remove headlines and questions from page content.

    :param documents: Text documents to create the vector store from.
    """
    for document in documents:
        processed_text = " ".join(document.page_content.split("\n", 2)[2:]).split('\n')
        processed_text = [line for line in processed_text if line and not (line.startswith("Frage:") or
                                                                           line.startswith("Antwort:"))]

        document.page_content = '\n'.join(processed_text)
    return documents


if __name__ == '__main__':
    # texts = get_doc_from_pdf()
    texts = get_doc_from_txt()
    process_doc(texts)
    create_vector_db(texts)
