import os
import re

from nltk.probability import FreqDist


stop_words = []


def setup_stopwords():
    """
    Set up the list of german stopwords from file.
    """
    directory = os.path.dirname(os.path.dirname(__file__))
    stop_word_file = (os.path.join(directory, 'data/german_stop_words.txt'))
    print(stop_word_file)
    with open(stop_word_file, 'r') as file:
        global stop_words
        stop_words = file.readlines()
        stop_words = [word.strip('\n') for word in stop_words]


def preprocess_text(text):
    """
    Preprocess the answer by removing non-alphanumeric characters, extra whitespaces, german umlauts and stopwords and
    making all words lowercase.

    :param text: Unprocessed answer.
    :return: Preprocessed answer.
    """
    # Remove non-alphanumeric characters (except for whitespaces and hyphen)
    text = re.sub(r'[^ \w+-]', '', text)
    # Remove numbers
    text = re.sub(r'[0-9]', '', text)
    # Make all words lower case and strip extra whitespaces
    text = text.lower().strip()
    # Replace german umlauts
    umlauts = {ord('ä'): 'ae', ord('ü'): 'ue', ord('ö'): 'oe', ord('ß'): 'ss'}
    text = text.translate(umlauts)
    # Remove stopwords
    text_words = text.split()
    text_words = [word for word in text_words if word not in stop_words]
    # result_text = ' '.join(text_words)
    # TODO: Stemming/ Lemmatization?
    return text_words


def extract_keywords(text, n=5):
    """
    Extract the n most used words from a paragraph.
    """
    words = preprocess_text(text)
    # Calculate word frequencies
    freq_dist = FreqDist(words)
    # Get the n most common words
    common_words = freq_dist.most_common(n)
    return common_words
