import glob
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

PDF_PATH = '/home/luna/workspace/Dialogsteuerung/data/pdf'
TXT_PATH = '/home/luna/workspace/Dialogsteuerung/data/chapters/processed_chapters'
PDF_DB_FAISS_PATH = '/home/luna/workspace/Dialogsteuerung/data/vectorStore/fromPdf'
TXT_DB_FAISS_PATH = '/home/luna/workspace/Dialogsteuerung/data/vectorStore/fromTxtGerman'


# Create vector database
def create_vector_db_pdf():
    loader = DirectoryLoader(PDF_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name='LLukas22/all-MiniLM-L12-v2-embedding-all',  # German version of 'sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device': 'cpu'})

    db = FAISS.from_documents(texts, embeddings)
    db.save_local(PDF_DB_FAISS_PATH)


def create_vector_db_txt():
    texts = []
    for file in glob.glob(TXT_PATH + '/*.txt'):
        with open(file, 'r') as txt_file:
            text = ''.join(txt_file.readlines())
            texts.append(text)
    texts = ''.join(texts)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=256, chunk_overlap=20)
    texts = text_splitter.split_text(texts)

    embeddings = HuggingFaceEmbeddings(model_name='LLukas22/all-MiniLM-L12-v2-embedding-all',  # 'sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device': 'cpu'})

    db = FAISS.from_texts(texts, embeddings)
    db.save_local(TXT_DB_FAISS_PATH)


if __name__ == '__main__':
    # create_vector_db_pdf()
    create_vector_db_txt()
