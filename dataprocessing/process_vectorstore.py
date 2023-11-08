import torch
from langchain.document_loaders import PyPDFLoader, DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS  # Try CHROMA?

PDF_PATH = '/home/luna/workspace/Dialogsteuerung/data/pdf'
TXT_PATH = '/home/luna/workspace/Dialogsteuerung/data/chapters/processed_chapters'
PDF_DB_FAISS_PATH = '/home/luna/workspace/Dialogsteuerung/data/vectorStore/fromPdf'
TXT_DB_FAISS_PATH = '/home/luna/workspace/Dialogsteuerung/data/vectorStore/fromTxtGerman'
DB_FAISS_PATH = '/home/luna/workspace/Dialogsteuerung/data/vectorStore'


def get_doc_pdf():
    """
    Read pdf documents.

    :return documents: Read pdf documents.
    """
    loader = DirectoryLoader(PDF_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents


def get_doc_txt():
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

    embeddings = HuggingFaceEmbeddings(model_name='LLukas22/all-MiniLM-L12-v2-embedding-all',
                                       model_kwargs={'device': device})

    db = FAISS.from_documents(split_text, embeddings)
    db.save_local(DB_FAISS_PATH)


if __name__ == '__main__':
    # texts = get_doc_pdf()
    texts = get_doc_txt()
    create_vector_db(texts)
