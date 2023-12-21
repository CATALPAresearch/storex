from pprint import pprint

from langchain.chains import RetrievalQA
from lmqg import TransformersQG

# initialize model
model = TransformersQG(language='de', model='lmqg/mt5-small-dequad-qg')
# paragraph to generate pairs of question and answer
context = "Wie bereits erwähnt sind Objekte im Speicher abgelegte Daten. Dabei ist jedes Objekt an " \
          "genau einer Stelle im Speicher abgelegt: Es wird damit durch seine Speicherstelle eindeutig " \
          "identifiziert. Aufgrund dieser eindeutigen Identifizierbarkeit spricht man auch von der Identität " \
          "eines Objekts; sie kann aus technischer Sicht mit der Speicherstelle, an der das Objekt " \
          "abgelegt ist, gleichgesetzt werden. Da keine zwei Objekte an derselben Stelle abgelegt werden " \
          "können, haben auch keine zwei Objekte dieselbe Identität."
# model prediction
question_answer = model.generate_qa(context)
# the output is a list of tuple (question, answer)
pprint(question_answer)


def get_question_from_retriever(self, query, k=4):
    """
    TODO: remove this function?
    Retrieve context for a given topic from a FAISS database.

    :param query:
    :param k:

    :return result: Answer to the question.
    :return source_documents: Source documents from the database.
    """
    # Set up as generic retriever
    retriever = self.db.as_retriever(search_type="similarity", search_kwargs={'k': k})

    # Create the chain for question answering
    answer_chain = RetrievalQA.from_chain_type(
        llm=self.llm,
        chain_type="stuff",  # stuff, map_reduce or map_rerank with k=10
        retriever=retriever,  # context_docs = db.similarity_search(query, k=4)
        return_source_documents=True,
        chain_type_kwargs={'prompt': self.prompt}
    )

    result = answer_chain({'query': query})
    result = result["result"]  # Sources at: result["source_documents"]
    return result
