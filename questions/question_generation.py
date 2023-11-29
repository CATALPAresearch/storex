"""
Class for generating questions.
"""
import os
import torch

from langchain.chains import LLMChain, RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS

# TODO: Remove api token
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


class QuestionGenerator:
    def __init__(self):
        """
        Initializes
        """
        # Load vectorstore embeddings
        directory = os.path.dirname(os.path.dirname(__file__))
        self.vectorstore = (os.path.join(directory, 'data/vectorStore'))
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.embedding_model = HuggingFaceEmbeddings(model_name='paraphrase-multilingual-MiniLM-L12-v2',
                                                     model_kwargs={'device': self.device})
        # Load database
        self.db = FAISS.load_local(self.vectorstore, self.embedding_model)

        # Load language module for question generation
        question_llm = HuggingFaceHub(repo_id="dehio/german-qg-t5-drink600")  # "LunaticTanuki/german-qg-mT5-small-OOP"

        # For locally saved models:
        # llm = HuggingFacePipeline.from_model_id(
        #          model_id=LOCAL_MODEL_PATH,
        #          task="text2text-generation")

        # Load question generation prompt from template
        question_template = """Context: {context}

        Question:"""
        question_prompt = PromptTemplate(template=question_template, input_variables=["context"])
        # Create chain for question generation
        self.question_chain = LLMChain(prompt=question_prompt, llm=question_llm)

        # Load language model for answer retrieval
        self.answer_llm = HuggingFaceHub(repo_id="google/flan-t5-large")  # "deepset/gelectra-base-germanquad"
        # Load answer retrieval prompt from template
        answer_template = """Use the following pieces of context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        Context: {context}
        Question: {question}

        Only returns the helpful answer below and nothing else.
        Helpful answer in German:
        """
        self.answer_prompt = PromptTemplate(template=answer_template, input_variables=['context', 'question'])

    def answer_question(self, query, retriever):
        """
        Retrieve an answer to a given question from a FAISS database.

        :param query: Question to be answered.
        :param retriever:

        :return result: Answer to the question.
        :return source_documents: Source documents from the database.
        """
        # Create the chain for question answering
        answer_chain = RetrievalQA.from_chain_type(
            llm=self.answer_llm,
            chain_type="stuff",  # stuff, map_reduce or map_rerank with k=10
            retriever=retriever,  # context_docs = db.similarity_search(query, k=4)
            return_source_documents=True,
            chain_type_kwargs={'prompt': self.answer_prompt}
        )

        result = answer_chain({'query': query})
        source_documents = result["source_documents"]
        result = result["result"]

        if source_documents:
            result += f"\nQuelle: " + str(source_documents)
        else:
            result += f"\nKeine Quellen gefunden!"
        print(f"Antwort: {result}")

        return result, source_documents

    def generate_question(self, context):
        print(self.question_chain.run(context))  # {"answer": answer, "context": CONTEXT}))

        # Get predictions with pipeline:
        # model = "deepset/gelectra-large-germanquad"
        # electra = pipeline('question-answering', model=model, tokenizer=model)
        # question_context = {'question': query, 'context': context}
        # result = electra(question_context)

        # Load model & tokenizer
        # model = AutoModelForQuestionAnswering.from_pretrained(model)
        # tokenizer = AutoTokenizer.from_pretrained(model)

    def get_context(self, query, k):
        # TODO: Topic extraction (maybe different database splitting, e.g. not at \n?)
        # Get context for query
        context_docs = self.db.similarity_search(query, k=k)
        context = ' '.join([doc.page_content for doc in context_docs])
        print(context)

        # Set up as generic retriever
        retriever = self.db.as_retriever(search_type="similarity", search_kwargs={'k': k})

        return context, retriever


if __name__ == '__main__':
    test_context_1 = (
        "Ein Literal (von lat. littera, der Buchstabe ) ist eine in der Syntax der Programmiersprache ausgedrückte "
        "Repräsentation eines Objektes. Literale sind somit textuelle Spezifikationen von Objekten: Wenn der "
        "Compiler ein Literal übersetzt, erzeugt er daraus — bei der Übersetzung! — das entsprechende Objekt im "
        "Speicher. Dies steht im Gegensatz zu objekterzeugend en Anweisungen eines Programms, denn diese werden "
        "erst zur Laufzeit des Programms ausgeführt. Da wir uns mit der programmgesteuerten Erzeugung von Objekten "
        "aber erst in der nächsten Kurs einheit systematisch befassen, müssen wir hier zunächst mit Objekten mit "
        "literaler Repräsentation vorlieb nehmen. Wohlgemerkt: Literale repräsentieren Objekte, es sind nicht "
        "selbst welche.")
    test_context_2 = (
        "Literale sind in der Syntax der Programmiersprache ausgedrückte textuelle Spezifikationen von Objekten. Der "
        "Compiler erzeugt aus einem Literal bei der Übersetzung das entsprechende Objekt im Speicher.")
    test_query = "Was sind Literale?"

    generator = QuestionGenerator()
    # generator.generate_question(test_context_1)
    # generator.generate_question(test_context_2)

    db_context, db_retriever = generator.get_context("Literal", 5)
    generator.answer_question(test_query, db_retriever)
    generator.generate_question(db_context)
