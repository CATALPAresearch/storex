from langchain import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA

DB_FAISS_PATH = '/home/luna/workspace/Dialogsteuerung/data/vectorStore/fromTxt'
MODEL_PATH = '/home/luna/workspace/llama.cpp/models/OpenBuddy/openbuddy-13b-v7-q4_K.bin'
REPO = 'TheBloke/Llama-2-13B-German-Assistant-v4-GPTQ'

custom_prompt_template = """Use the following pieces of information to answer the user's question in German.
If you don't know the answer, just say that you don't know the answer, don't try to make up an answer.

Context: {context}
Question: {question}

Only returns the helpful answer below and nothing else.
Helpful answer:
"""


def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vector stores
    """
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])
    return prompt


def load_llm():
    llm = CTransformers(
        model=MODEL_PATH,
        model_type="llama",
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
    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrival_qa_chain(llm, qa_prompt, db)

    return qa


def final_result(query):
    qa_result = qa_bot()
    response = qa_result({'query': query})
    return response


if __name__ == '__main__':
    print('Hi, was willst du wissen?')
    question = input()
    res = final_result(question)
    answer = res["result"]
    sources = res["source_documents"]

    if sources:
        answer += f"\nQuelle: " + str(sources)
    else:
        answer += f"\nKeine Quellen gefunden!"

    print("Antwort:", answer)
