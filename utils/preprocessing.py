import os
import re

from nltk.probability import FreqDist


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


def preprocess_text(text):
    """
    Preprocess the answer by removing non-alphanumeric characters, extra whitespaces, german umlauts and stopwords and
    making all words lowercase.

    :param text: Unprocessed answer.
    :return: Preprocessed answer.
    """
    # Remove non-alphanumeric characters (except for whitespaces)
    text = re.sub(r'[^ \w+]', '', text)
    # Make all words lower case and strip extra whitespaces
    text = text.lower().strip()
    # Replace german umlauts
    umlauts = {ord('ä'): 'ae', ord('ü'): 'ue', ord('ö'): 'oe', ord('ß'): 'ss'}
    text = text.translate(umlauts)
    # Remove stopwords
    text = [word for word in text if word not in stop_words]
    # TODO: Stemming/ Lemmatization
    return text


def extract_keywords(text, n=5):
    """
    Extract the n most used words from a paragraph.
    """
    text = preprocess_text(text)
    # Calculate word frequencies
    freq_dist = FreqDist(text)

    # Get the n most common words
    common_words = freq_dist.most_common(n)

    return common_words
