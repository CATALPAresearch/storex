import os
from langchain import PromptTemplate, HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

DB_FAISS_PATH = '/home/luna/workspace/Dialogsteuerung/data/vectorStore/fromTxtGerman'
MODEL_PATH = '/home/luna/workspace/llama.cpp/models/OpenBuddy/openbuddy-13b-v7-q4_K.bin'
REPO = 'LunaticTanuki/german-qg-mT5-small-OOP'

custom_prompt_template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only returns the helpful answer below and nothing else.
Helpful answer in German:
"""


def retrieve_result(query):
    # Load embeddings
    embeddings = HuggingFaceEmbeddings(model_name='LLukas22/all-MiniLM-L12-v2-embedding-all',
                                       model_kwargs={'device': 'cpu'})
    # Load database
    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    # Load LLM (from Huggingface: llm = HuggingFaceHub(repo_id=REPO))
    llm = CTransformers(
        model=MODEL_PATH,
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5
    )
    # Load prompt
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])
    # Creat the chain to answer questions
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # map_reduce
        retriever=db.as_retriever(search_type="similarity", search_kwargs={'k': 2}),
        return_source_documents=True,
        chain_type_kwargs={'prompt': prompt}
    )
    result = qa_chain({'query': query})
    return result


if __name__ == '__main__':
    print('Hi, was willst du wissen?')
    question = input()
    res = retrieve_result(question)
    answer = res["result"]
    sources = res["source_documents"]

    if sources:
        answer += f"\nQuelle: " + str(sources)
    else:
        answer += f"\nKeine Quellen gefunden!"

    print("Antwort:", answer)
