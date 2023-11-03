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


def setup():
    # Set up the list of german stopwords from file.
    directory = os.path.dirname(__file__)
    file_sw = (os.path.join(directory, 'data/german_stop_words.txt'))
    with open(file_sw, 'r') as sw:
        global stop_words
        stop_words = sw.readlines()
        stop_words = [word.strip('\n') for word in stop_words]

    # Load course material
    course_material = []
    directory_cm = (os.path.join(directory, 'data/chapters/processed_chapters'))
    for file_cm in glob.glob(directory_cm + '/*.txt'):
        with open(file_cm, 'r') as cm:
            lines = cm.readlines()
            lines = lines[lines.index('\n') + 1:]
            paragraph = ''.join(lines[:lines.index('\n')])
            paragraph = ' '.join(preprocess_text(paragraph))
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


def preprocess_text(text):
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


lsa_model, tfidf_vectorizer = setup()

# Sample student answer and correct answer
student_answer = "Das Problem der schlechten Tracebarkeit ist eine neue Automarke"
correct_answer = "Das Problem der schlechten Tracebarkeit entsteht durch den dynamischen Programmablauf. Die Goto-Anweisung erlaubt Sprünge von beliebigen Stellen eines Programms zu anderen Stellen und bricht dabei das Lokalitätsprinzip von Programmen, bei dem zusammengehörende Anweisungen im Programmtext nahe beieinander stehen. Dies führte zu einer Unübersichtlichkeit im Programmtext und erschwerte das Verstehen und Debuggen von Programmen."

# Fold student and correct answers into the semantic room
student_vector = tfidf_vectorizer.transform([student_answer])
correct_vector = tfidf_vectorizer.transform([correct_answer])

student_lsa = lsa_model.transform(student_vector)
correct_lsa = lsa_model.transform(correct_vector)

# Calculate cosine similarity between student and correct answers
cosine_sim = cosine_similarity(student_lsa, correct_lsa)
similarity = cosine_sim[0][0]

print(f"Cosine Similarity: {similarity:.4f}", cosine_sim)
