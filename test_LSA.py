import os
import re
import numpy
import torch
import glob
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import AutoModelForSequenceClassification, AutoModelForCausalLM, AutoTokenizer, pipeline
from sentence_transformers import SentenceTransformer, util
from gensim import corpora, models, similarities
from gensim.parsing.preprocessing import preprocess_string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD


import logging
logger = logging.getLogger()

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'
stop_words = []


def setup_stopwords():
    """
    Set up the list of german stopwords from file.
    """
    directory = os.path.dirname(__file__)
    file_sw = (os.path.join(directory, 'data/german_stop_words.txt'))
    with open(file_sw, 'r') as sw:
        global stop_words
        stop_words = sw.readlines()
        stop_words = [word.strip('\n') for word in stop_words]


def preprocess_answer(text):
    """
    Preprocess the answer by removing non-alphanumeric characters, extra whitespaces, german umlauts and stopwords and
    making all words lowercase.

    :param text: Unprocessed answer.
    :return: Preprocessed answer.
    """
    # Remove non-alphanumeric characters (except for whitespaces)
    text = re.sub(r'[^ \w+]', '', text)
    custom_filters = [lambda x: x.lower(),             # Make all words lowercase
                      lambda x: x.strip(),             # Strip extra whitespace
                      lambda x: x.replace("ä", "ae"),  # Replace german umlauts
                      lambda x: x.replace("ö", "oe"),
                      lambda x: x.replace("ü", "ue"),
                      lambda x: x.replace("ß", "ss")]
    text = preprocess_string(text, custom_filters)
    # Remove stopwords
    text = [word for word in text if word not in stop_words]
    # TODO: Stemming/ Lemmatization
    return text


def setup_semantic_room():
    directory = os.path.dirname(__file__)
    # Load course material
    course_material = []
    directory_cm = (os.path.join(directory, 'data/chapters/processed_chapters'))
    for file_cm in glob.glob(directory_cm + '/*.txt'):
        with open(file_cm, 'r') as cm:
            lines = cm.readlines()
            lines = lines[lines.index('\n') + 1:]
            paragraph = ''.join(lines[:lines.index('\n')])
            paragraph = ' '.join(preprocess_answer(paragraph))
            course_material.append(paragraph)
    # Create a document-term matrix
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(course_material)
    terms = tfidf_vectorizer.get_feature_names_out()

    # Apply Latent Semantic Analysis (LSA) using TruncatedSVD
    num_topics = 2  # Number of topics for LSA
    lsa_model = TruncatedSVD(n_components=num_topics)
    lsa_topic_matrix = lsa_model.fit_transform(tfidf_matrix)

    return lsa_model, tfidf_vectorizer


def answers_in_semantic_room(student_answer, correct_answer):
    lsa_model, tfidf_vectorizer = setup_semantic_room()

    # Fold student and correct answers into the semantic room
    student_vector = tfidf_vectorizer.transform([student_answer])
    correct_vector = tfidf_vectorizer.transform([correct_answer])

    student_lsa = lsa_model.transform(student_vector)
    correct_lsa = lsa_model.transform(correct_vector)

    # Calculate cosine similarity between student and correct answers
    cosine_sim = cosine_similarity(student_lsa, correct_lsa)
    similarity = cosine_sim[0][0]

    print(f"Cosine Similarity: {similarity:.4f}", cosine_sim)


def similarity_lsa(correct_tokens, student_tokens):
    # Create a term dictionary of the corpus, where every unique term is assigned an index
    dictionary = corpora.Dictionary([student_tokens, correct_tokens])
    # Converting corpus into Document Term Matrix
    corpus = [dictionary.doc2bow(tokens) for tokens in [student_tokens, correct_tokens]]

    # coherence_values = []
    # model_list = []
    # for num_topics in range(2, 12):
    #     # generate LSA model
    #     model = LsiModel(corpus, num_topics=num_topics, id2word=dictionary)  # train model
    #     model_list.append(model)
    #     coherence_model = CoherenceModel(model=model, texts=[student_tokens, correct_tokens], dictionary=dictionary, coherence='c_v')
    #     coherence_values.append(coherence_model.get_coherence())
    # num_topics = coherence_values.index(max(coherence_values))
    # if num_topics == 0:
    #     num_topics = 2

    num_topics = 5  # TODO: What is a good number of topics?

    # Create an LSA model
    lsa = models.LsiModel(corpus, id2word=dictionary, num_topics=num_topics)  # train model
    print(lsa.print_topics(num_topics=num_topics, num_words=3))

    # Transform the student and correct answer into the LSA space
    student_lsa = lsa[corpus[0]]
    correct_lsa = lsa[corpus[1]]

    # Convert LSA representations to NumPy arrays
    student_lsa_array = numpy.array(student_lsa)
    correct_lsa_array = numpy.array(correct_lsa)
    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(student_lsa_array, correct_lsa_array)
    # Set a threshold to identify low similarity tokens
    threshold = 0.2  # Adjust the threshold as needed
    # Identify tokens with low similarity to any tokens from the other answer
    low_similarity_tokens_student = [token for token, similarity in zip(student_tokens, similarity_matrix[0]) if
                                     similarity < threshold]
    low_similarity_tokens_correct = [token for token, similarity in zip(correct_tokens, similarity_matrix[0]) if
                                     similarity < threshold]

    # Calculate the cosine similarity
    similarity = numpy.dot(student_lsa, correct_lsa) / (numpy.linalg.norm(student_lsa) * numpy.linalg.norm(correct_lsa))
    # Print the similarity score
    print(f"Similarity Score (LSA): {similarity}")

    term_loading = lsa.projection.u
    threshold = 0.5
    # differing_tokens = [term for i, term in enumerate(dictionary.values()) if abs(term_loading[i, 0]) < threshold]

    # Identify dimensions with low similarity
    #low_similarity_dimensions = [i for i, sim in enumerate(similarity) if sim < threshold]
#
    ## Examine term loadings in low similarity dimensions
    #term_loadings = lsa.projection.u
#
    ## Identify differing tokens with high absolute term loadings
    #differing_tokens = set()
    #for dim in low_similarity_dimensions:
    #    for term, loading in enumerate(term_loadings):
    #        if abs(loading[dim]) > 0.2:  # Adjust the threshold as needed
    #            differing_tokens.add(dictionary[term])
#
    #print("Differing tokens:", differing_tokens)


def similarity(student_answer, correct_answer):
    # Preprocess answers for similarity search
    c_processed = preprocess_answer(correct_answer)
    s_processed = preprocess_answer(student_answer)

    # Similarity with LSA
    similarity = similarity_lsa(c_processed, s_processed)
    print(similarity)


if __name__ == '__main__':
    # Sample student answer and correct answer
    student_answer = "Das Problem der schlechten Tracebarkeit entsteht durch den dynamischen Programmablauf. Das Lokalitätsprinzip wird gebrochen und dies für zur Unerbersichtlichkeit."
    correct_answer = "Das Problem der schlechten Tracebarkeit entsteht durch den dynamischen Programmablauf. Die Goto-Anweisung erlaubt Sprünge von beliebigen Stellen eines Programms zu anderen Stellen und bricht dabei das Lokalitätsprinzip von Programmen, bei dem zusammengehörende Anweisungen im Programmtext nahe beieinander stehen. Dies führte zu einer Unübersichtlichkeit im Programmtext und erschwerte das Verstehen und Debuggen von Programmen."

    similarity(student_answer, correct_answer)

    # Or with sematic room over pdf:
    answers_in_semantic_room(student_answer, correct_answer)
