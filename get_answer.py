import os
import torch
from langchain.prompts import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain import HuggingFaceHub

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'
DB_FAISS_PATH = '/home/luna/workspace/Dialogsteuerung/data/vectorStore'

prompt_template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only returns the helpful answer below and nothing else.
Helpful answer in German:
"""


def retrieve_result(query):
    # Load embeddings
    device = "cuda" if torch.cuda.is_available() else "cpu"
    embeddings = HuggingFaceEmbeddings(model_name='LLukas22/all-MiniLM-L12-v2-embedding-all',
                                       model_kwargs={'device': device})

    # Load database and set up as generic retriever
    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={'k': 4})

    # Load LLM
    # TODO: Question-Answering: llm = HuggingFaceHub(repo_id="deepset/gelectra-base-germanquad")
    llm = HuggingFaceHub(repo_id="google/flan-t5-large")

    # Load prompt
    prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

    # Creat the chain to answer questions
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # stuff, map_reduce or map_rerank with k=10
        retriever=retriever,  # context_docs = db.similarity_search(query, k=4)
        return_source_documents=True,
        chain_type_kwargs={'prompt': prompt}
    )
    result = qa_chain({'query': query})
    return result


if __name__ == '__main__':
    question = "Was ist das Problem der eindimensionalen Strukturierung?"
    res = retrieve_result(question)
    answer = res["result"]
    sources = res["source_documents"]

    if sources:
        answer += f"\nQuelle: " + str(sources)
    else:
        answer += f"\nKeine Quellen gefunden!"

    print("Antwort:", answer)
