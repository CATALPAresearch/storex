import os
import re


stop_words = []
technical_terms = []


def parse_term(line):
    """
    Parses one line of the technical term list.

    A line in the form '[alias, aliasing]' lists synonyms for the same term and
    becomes a list of spellings; every other line becomes a plain string.
    Without this the brackets and the comma survived into the search pattern,
    so a bracketed term could never match anything.
    """
    line = line.strip()
    if line.startswith('[') and line.endswith(']'):
        return [part.strip() for part in line[1:-1].split(',') if part.strip()]
    return line


def setup_word_lists():
    """
    Set up the list of german stopwords and the list of technical terms from file.
    """
    directory = os.path.dirname(os.path.dirname(__file__))
    stop_word_file = (os.path.join(directory, 'data/german_stop_words.txt'))
    technical_term_file = (os.path.join(directory, 'data/technical_terms.txt'))

    with open(stop_word_file, 'r', encoding='utf-8') as file:
        global stop_words
        stop_words = [word.strip() for word in file.readlines() if word.strip()]

    with open(technical_term_file, 'r', encoding='utf-8') as file:
        global technical_terms
        technical_terms = [parse_term(line) for line in file.readlines() if line.strip()]


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
    return text_words


def term_label(term):
    """
    Returns the preprocessed form a term is reported under.

    For a synonym list this is its first spelling, so that a term found through
    any of its synonyms is always reported the same way and can be compared
    against the keywords of a question.
    """
    spellings = term if isinstance(term, list) else [term]
    return preprocess_text(spellings[0])


def extract_keywords(text, terms=None):
    """
    Extract the used technical terms.
    Terms are returned preprocessed, see term_label.
    """
    words = preprocess_text(text)
    technical_words = []
    if terms is None:
        terms = technical_terms

    for term in terms:
        # A term is either a single spelling or a list of synonyms
        spellings = term if isinstance(term, list) else [term]
        label = term_label(term)

        for spelling in spellings:
            spelling = preprocess_text(spelling)
            if not spelling:
                continue
            # Create a regular expression pattern allowing for different grammatical endings
            pattern = re.compile(fr"\b{re.escape(spelling)}(?:\b|\w*en\b|\w*em\b|\w*es\b|\w*s\b|)?",
                                 re.IGNORECASE)
            if pattern.search(words):
                technical_words.append(label)
                break

    return technical_words


def extract_common_words(text, n=5):
    """
    Extract the n most common words from a paragraph.
    """
    # Imported here so that an exam run does not pull in nltk
    from nltk.probability import FreqDist

    words = preprocess_text(text)
    words = remove_stopwords(words)
    # Calculate word frequencies
    freq_dist = FreqDist(words)
    # Get the n most common words
    common_words = freq_dist.most_common(n)
    return [word[0] for word in common_words]
