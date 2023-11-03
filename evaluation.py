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


def evaluate_free_answer(answer):
    return True


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


def evaluate_predefined_question(question_keyword, student_answer):
    keywords = question_keyword['keywords']
    missing_keys = []
    for word in keywords:
        if word not in student_answer:
            missing_keys.append(word)

    if missing_keys:
        print(missing_keys)
        logger.info("Non-mentioned keywords: " + str(missing_keys))
        accuracy = check_accuracy(missing_keys, student_answer)


def evaluate_answer(question_answer, student_answer):
    """
    Compare the students answer with the correct answer (with t5 or 'tiiuae/falcon-40b'?)

    :param question_answer: Question-answer pair
    :param student_answer: Answer given by the student
    :return: Differences in the students answer
    """
    correct_answer = question_answer['answer']

    # Text classification with MNLI to check the congruity of the answer
    congruity = check_congruity(correct_answer, student_answer)
    logger.debug("The answers contain: " + str(congruity[0]['label']))
    if congruity[0]['label'] == 'ENTAILMENT':
        pass

    # Preprocess answers for similarity search
    c_processed = preprocess_answer(correct_answer)
    s_processed = preprocess_answer(student_answer)

    # Similarity with similarity search LLM
    similarity = compare_similarity(' '.join(c_processed), ' '.join(s_processed))
    print(similarity)
    if similarity > 0.75:  # TODO: What similarity is similar??
        print("Similar answers. Check if the facts are correct.")
    else:
        print("Something missing in the answer or the answer is not regarding the right topic.")

    # Similarity with LSA
    similarity_lsa(c_processed, s_processed)

    # Load a text-generation model on the hub
    llm = HuggingFaceHub(repo_id='google/flan-t5-large',
                         model_kwargs={'temperature': 0,
                                       'max_length': 1024})
    # TODO: Antworten aufbereiten, damit sie vergleichbar sind, z.B. keywords suchen? Summary?
    template = """Compare the following texts:
    "{c_answer}"
    and
    "{s_answer}"

    Here are the differences:"""
    # prompt_template = PromptTemplate.from_template(template)
    # prompt = prompt_template.format(c_answer=correct_answer, s_answer=student_answer)

    prompt = PromptTemplate(template=template, input_variables=['c_answer', 's_answer'])

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    differences = llm_chain.run({'c_answer': correct_answer, 's_answer': student_answer})
    print(differences)

    # Identify the mistakes (factual inaccuracy, missing information, structural issues) out off the differences
    return True


def compare_similarity(correct_answer, student_answer):
    """
    Semantic textual similarity search (also try: intfloat/multilingual-e5-small)

    :param correct_answer: Correct answer
    :param student_answer: Answer given by the student
    :return: Similarity between both answers
    """
    # Load a sentence similarity model
    model = SentenceTransformer('LLukas22/all-MiniLM-L12-v2-embedding-all')
    # Compute embeddings for both answers
    c_embedding = model.encode(correct_answer, convert_to_tensor=True)
    s_embedding = model.encode(student_answer, convert_to_tensor=True)
    # Calculate similarity
    similarity = util.pytorch_cos_sim(c_embedding, s_embedding)
    return similarity


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
    print("Similarity Score (LSA):\n", similarity)

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


def check_accuracy(keys, student_answer):
    """
    Check if the keywords are accurately represented in the students answer.

    Try morit/xlm-t-roberta-base-mnli-xnli?

    :param keys:
    :param student_answer:
    :return: Congruity
    """
    # Check entailment in concatenated answers
    classifier = pipeline("zero-shot-classification", model="symanto/xlm-roberta-base-snli-mnli-anli-xnli")
    accuracy = classifier(student_answer, keys)
    print(accuracy)
    exit(0)

    return accuracy


def check_congruity(correct_answer, student_answer):
    """
    Check if the concatenated answers contain a contradiction or entail each other.

    Try morit/xlm-t-roberta-base-mnli-xnli?

    :param correct_answer:
    :param student_answer:
    :return: Congruity
    """
    # Check entailment in concatenated answers
    classifier = pipeline("text-classification", model="symanto/xlm-roberta-base-snli-mnli-anli-xnli")
    congruity = classifier(correct_answer + student_answer)

    return congruity

    # Check probs
    model = AutoModelForSequenceClassification.from_pretrained("symanto/xlm-roberta-base-snli-mnli-anli-xnli")
    tokenizer = AutoTokenizer.from_pretrained("symanto/xlm-roberta-base-snli-mnli-anli-xnli")
    inputs = tokenizer([correct_answer, student_answer], return_tensors="pt", padding=True)  # truncate=True?
    logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=1)
    probs = probs[..., [0]].tolist()
    print("probs", probs)
