import os
import torch
from langchain.prompts import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


def text_generation(query, vectorstore):
    """
    Retrieve an answer to a given question from a FAISS database.

    :param query: Question to be answered.
    :param vectorstore: FAISS vectorstore database.

    :return result: Answer to the question.
    :return source_documents: Source documents from the database.
    """
    # Load prompt from template
    prompt_template = """Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    Context: {context}
    Question: {question}

    Only returns the helpful answer below and nothing else.
    Helpful answer in German:
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

    # Load embeddings
    device = "cuda" if torch.cuda.is_available() else "cpu"
    embeddings = HuggingFaceEmbeddings(model_name='paraphrase-multilingual-MiniLM-L12-v2',
                                       model_kwargs={'device': device})

    # Load vectorstore database and set up as generic retriever
    db = FAISS.load_local(vectorstore, embeddings)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={'k': 4})

    # Load LLM
    # TODO: Question-Answering: llm = HuggingFaceHub(repo_id="deepset/gelectra-base-germanquad")
    llm = HuggingFaceHub(repo_id="google/flan-t5-large")

    # Create the chain for question answering
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # stuff, map_reduce or map_rerank with k=10
        retriever=retriever,  # context_docs = db.similarity_search(query, k=4)
        return_source_documents=True,
        chain_type_kwargs={'prompt': prompt}
    )
    result = qa_chain({'query': query})
    source_documents = result["source_documents"]
    result = result["result"]
    return result, source_documents


def question_answering(query, vectorstore):
    # Load embeddings
    device = "cuda" if torch.cuda.is_available() else "cpu"
    embeddings = HuggingFaceEmbeddings(model_name='paraphrase-multilingual-MiniLM-L12-v2',
                                       model_kwargs={'device': device})

    # Load database and get context for query
    db = FAISS.load_local(vectorstore, embeddings)
    context_docs = db.similarity_search(query, k=4)
    context = ' '.join([doc.page_content for doc in context_docs])

    # Get predictions
    model = "deepset/gelectra-large-germanquad"
    electra = pipeline('question-answering', model=model, tokenizer=model)
    question_context = {'question': query, 'context': context}
    res = electra(question_context)

    # Load model & tokenizer
    # model = AutoModelForQuestionAnswering.from_pretrained(model)
    # tokenizer = AutoTokenizer.from_pretrained(model)
    print(res)


def get_answer_from_db(query):
    directory = os.path.dirname(__file__)
    vectorstore_path = (os.path.join(directory, 'data/vectorStore'))

    # TODO: Topic extraction (maybe different database splitting, e.g. not at \n?)

    question_answering(query, vectorstore_path)

    answer, sources = text_generation(question, vectorstore_path)
    if sources:
        answer += f"\nQuelle: " + str(sources)
    else:
        answer += f"\nKeine Quellen gefunden!"

    print(f"Antwort: {answer}")


if __name__ == '__main__':
    question = "Was ist das Problem der eindimensionalen Strukturierung?"
    get_answer_from_db(question)