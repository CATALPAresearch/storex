import os
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


def evaluate_free_answer(answer):
    return True


def evaluate_answer(qa, answer):
    # Compare question-answer with given answer with t5 or 'tiiuae/falcon-40b'
    answers = {'qa_answer': qa['answer'], 'answer': answer}

    llm = HuggingFaceHub(repo_id='google/flan-t5-large',
                         model_kwargs={'temperature': 0,
                                       'max_length': 1024})
    template = """Compare the students answer to the corrected answer and highlight the differences.
    students answer: {answer}
    corrected answer: {qa_answer}

    Here are the differences:"""

    # prompt_template = PromptTemplate.from_template(template)
    # prompt_template.format(answer=answer, qa_answer=qa)

    prompt = PromptTemplate(template=template, input_variables=['answer', 'qa_answer'])
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    differences = llm_chain.run(answers)
    print(differences)

    # Identify the mistakes (factual inaccuracy, missing information, structural issues) out off the differences
    # Semantic textual similarity search (intfloat/multilingual-e5-small) or

    embeddings = HuggingFaceEmbeddings(model_name='LLukas22/all-MiniLM-L12-v2-embedding-all',
                                       model_kwargs={'device': 'cpu'})

    import requests

    API_URL = "https://api-inference.huggingface.co/models/LLukas22/all-MiniLM-L12-v2-embedding-all"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": {
            "source_sentence": "That is a happy person",
            "sentences": [
                "That is a happy dog",
                "That is a very happy person",
                "Today is a sunny day"
            ]
        },
    })

    return True
