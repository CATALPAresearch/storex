import os
import re

from nltk.probability import FreqDist


stop_words = []
technical_terms = []


def setup_word_lists():
    """
    Set up the list of german stopwords and the list of technical terms from file.
    """
    directory = os.path.dirname(os.path.dirname(__file__))
    stop_word_file = (os.path.join(directory, 'data/german_stop_words.txt'))
    technical_term_file = (os.path.join(directory, 'data/technical_terms.txt'))

    with open(stop_word_file, 'r') as file:
        global stop_words
        stop_words = file.readlines()
        stop_words = [word.strip('\n') for word in stop_words]

    with open(technical_term_file, 'r') as file:
        global technical_terms
        technical_terms = file.readlines()
        technical_terms = [word.strip('\n') for word in technical_terms]


def preprocess_text(text):
    """
    Preprocess the answer by removing non-alphanumeric characters, extra whitespaces, german umlauts and stopwords and
    making all words lowercase.
    """
    # Remove non-alphanumeric characters (except for whitespaces and hyphen)
    text = re.sub(r'[^ \w+-]', '', text)
    # Make all words lower case and strip extra whitespaces
    text = text.lower().strip()
    # Replace german umlauts
    umlauts = {ord('ä'): 'ae', ord('ü'): 'ue', ord('ö'): 'oe', ord('ß'): 'ss'}
    text = text.translate(umlauts)
    return text


def remove_stopwords(text):
    # Remove stopwords
    text_words = text.split()
    text_words = [word for word in text_words if word not in stop_words]
    # result_text = ' '.join(text_words)
    # TODO: Stemming/ Lemmatization?
    return text_words


def extract_keywords(text, terms=None):
    """
    Extract the used technical terms.
    """
    words = preprocess_text(text)
    technical_words = []
    if terms is None:
        terms = technical_terms

    for term in terms:
        # Check synonym lists
        if isinstance(term, list):
            for word in term:
                pattern = re.compile(fr"\b{re.escape(word)}(?:\b|\w*en\b|\w*em\b|\w*es\b|\w*s\b|)?", re.IGNORECASE)
                matches = re.findall(pattern, words)
                if matches:
                    technical_words.append(term)
                    break
        # Create a regular expression pattern allowing for different grammatical endings
        else:
            pattern = re.compile(fr"\b{re.escape(term)}(?:\b|\w*en\b|\w*em\b|\w*es\b|\w*s\b|)?", re.IGNORECASE)
            matches = re.findall(pattern, words)
            if matches:
                technical_words.append(term)

    return technical_words


def extract_common_words(text, n=5):
    """
    Extract the n most common words from a paragraph. TODO: How many keywords?
    """
    words = preprocess_text(text)
    words = remove_stopwords(words)
    # Calculate word frequencies
    freq_dist = FreqDist(words)
    # Get the n most common words
    common_words = freq_dist.most_common(n)
    return [word[0] for word in common_words]
