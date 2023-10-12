import os
import re
import numpy
from nltk.corpus import stopwords
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from sentence_transformers import SentenceTransformer, util
from gensim import corpora, models, similarities
from gensim.parsing.preprocessing import preprocess_string
from sklearn.metrics.pairwise import cosine_similarity


os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'
stop_words = stopwords.words('german')


def setup():
    with open('/home/luna/workspace/Dialogsteuerung/data/german_stop_words.txt', 'r') as sw:
        global stop_words
        stop_words = sw.readlines()


def evaluate_free_answer(answer):
    return True


def preprocess_answer(text):
    # Remove non-alphanumeric characters (except for whitespaces)
    text = re.sub(r'[^ \w+]', '', text)
    custom_filters = [lambda x: x.lower(),                         # Make all words lowercase
                      lambda x: x.strip(),                         # Strip extra whitespace
                      lambda x: x.replace("ä", "ae"),              # Replace german umlauts
                      lambda x: x.replace("ö", "oe"),
                      lambda x: x.replace("ü", "ue"),
                      lambda x: x.replace("ß", "ss")]
    text = preprocess_string(text, custom_filters)
    # Remove stopwords
    text = [word for word in text if word not in stop_words]
    print(text)
    return text


def evaluate_answer(question_answer, student_answer):
    """
    Compare the students answer with the correct answer (with t5 or 'tiiuae/falcon-40b'?)

    :param question_answer: Question-answer pair
    :param student_answer: Answer given by the student
    :return: Differences in the students answer
    """
    correct_answer = question_answer['answer']
    c_processed = preprocess_answer(correct_answer)
    s_processed = preprocess_answer(student_answer)

    similarity_lsa(c_processed, s_processed)
    similarity = compare_similarity(' '.join(c_processed), ' '.join(s_processed))
    print(similarity)
    if similarity > 0.5:  # TODO: What similarity is similar??
        print("Similar answers. Check if the facts are correct.")
    else:
        print("Something missing in the answer or the answer is not regarding the right topic.")

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
    # Create a dictionary and a corpus
    dictionary = corpora.Dictionary([student_tokens, correct_tokens])
    corpus = [dictionary.doc2bow(tokens) for tokens in [student_tokens, correct_tokens]]

    # Create an LSA model
    num_topics = 2  # You can adjust the number of topics based on your needs
    lsa = models.LsiModel(corpus, id2word=dictionary, num_topics=num_topics)

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
