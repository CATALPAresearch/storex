import os
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from sentence_transformers import SentenceTransformer, util

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


def evaluate_free_answer(answer):
    return True


def evaluate_answer(question_answer, student_answer):
    """
    Compare the students answer with the correct answer (with t5 or 'tiiuae/falcon-40b'?)

    :param question_answer: Question-answer pair
    :param student_answer: Answer given by the student
    :return: Differences in the students answer
    """
    correct_answer = question_answer['answer']
    if (compare_similarity(correct_answer, student_answer)) > 0.75:  # TODO: What similarity is similar??
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
