import functools
import os
import re

# The stop word list and the matching rules below are German: the endings in
# extract_keywords and the umlaut transliteration in preprocess_text are German
# morphology, not course content. The technical terms, in contrast, belong to a
# course and are passed in by the caller, see courselib.
STOP_WORD_FILE = 'resources/stop_words_de.txt'


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


@functools.lru_cache(maxsize=1)
def stop_words():
    """
    The german stop word list. Shared, because it describes the language and
    not a course.
    """
    package = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(package, STOP_WORD_FILE), 'r', encoding='utf-8') as file:
        return tuple(word.strip() for word in file if word.strip())


def load_terms(path):
    """
    Reads a list of technical terms. Used by the course loader; the result
    belongs to one course and is handed to extract_keywords explicitly.
    """
    with open(path, 'r', encoding='utf-8') as file:
        return tuple(parse_term(line) for line in file if line.strip())


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
    text_words = [word for word in text_words if word not in stop_words()]
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


def extract_keywords(text, terms=()):
    """
    Extract the used technical terms.

    :param terms: the technical terms of a course, see courselib. Passing them
        in rather than reading a module global is what keeps two exams on
        different courses from scoring each other's vocabulary.
    :return: the terms found, preprocessed, see term_label.
    """
    words = preprocess_text(text)
    technical_words = []

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
