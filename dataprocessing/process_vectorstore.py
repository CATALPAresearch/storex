"""
Script for creating a vector store from text files or pdf data.
"""
import os
import torch

from langchain.document_loaders import PyPDFLoader, DirectoryLoader, TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

directory = os.path.dirname(os.path.dirname(__file__))
PDF_PATH = os.path.join(directory, 'data/pdf')
TXT_PATH = os.path.join(directory, 'data/chapters_processed')
DB_FAISS_PATH = os.path.join(directory, 'data/vectorStore')


def get_doc_from_pdf():
    """
    Reads pdf files and return a list of documents.
    """
    loader = DirectoryLoader(PDF_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents


def get_doc_from_txt():
    """
    Reads textfiles and return a list of documents.
    """
    loader = DirectoryLoader(TXT_PATH, glob='*.txt', loader_cls=TextLoader)
    documents = loader.load()
    return documents


def process_doc(documents):
    """
    Removes headlines as well as questions and answers from the page contents of each document.
    """
    for document in documents:
        processed_text = " ".join(document.page_content.split("\n", 2)[2:]).split('\n')
        processed_text = [line for line in processed_text if line and not (line.startswith("Frage:") or
                                                                           line.startswith("Antwort:"))]

        document.page_content = '\n'.join(processed_text)
    return documents


def create_vector_db(documents):
    """
    Creates a FAISS vector database from text documents. First splits the text recursively and then creates embeddings.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150,
                                                   separators=['\n\n', '\n', '.', ',', ' ', ''])
    split_text = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name='paraphrase-multilingual-MiniLM-L12-v2',
                                       model_kwargs={'device': device})

    db = FAISS.from_documents(split_text, embeddings)
    db.save_local(DB_FAISS_PATH)
    print(f"Database saved to {DB_FAISS_PATH}")


# Create a FAISS vector database from processed text documents.
texts = get_doc_from_txt()  # To load directly from a pdf, call 'get_doc_from_pdf()' instead
process_doc(texts)
create_vector_db(texts)
