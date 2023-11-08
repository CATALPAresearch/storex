import os
import re
import numpy
import torch
import glob
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
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


def evaluate_free_answer(answer):
    return True


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


def evaluate_answer(correct_answer, student_answer):
    """
    Compare the students answer with the correct answer (with t5 or 'tiiuae/falcon-40b'?)

    :param correct_answer: Question-answer pair.
    :param student_answer: Answer given by the student.
    :return: Differences in the students answer.
    """
    # Text classification with MNLI to check the congruity of the answer
    congruity = check_congruity(correct_answer, student_answer)
    logger.info("The answers contain: " + str(congruity[0]['label']))
    if congruity[0]['label'] == 'ENTAILMENT':
        pass

    # Similarity with similarity search LLM
    similarity = compare_similarity(correct_answer, student_answer)
    print(similarity)
    if similarity > 0.75:  # TODO: What similarity is similar??
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

    :param correct_answer: Correct answer.
    :param student_answer: Answer given by the student.
    :return: Similarity between both answers.
    """
    # Load a sentence similarity model
    model = SentenceTransformer('LLukas22/all-MiniLM-L12-v2-embedding-all')
    # Compute embeddings for both answers
    c_embedding = model.encode(correct_answer, convert_to_tensor=True)
    s_embedding = model.encode(student_answer, convert_to_tensor=True)
    # Calculate similarity
    similarity = util.pytorch_cos_sim(c_embedding, s_embedding)
    return similarity


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
    logger.info(f"Accuracy: {accuracy}")

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
