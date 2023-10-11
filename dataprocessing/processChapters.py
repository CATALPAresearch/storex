import glob
import csv

from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

CONTEXT_PATH = '/home/luna/workspace/Dialogsteuerung/data/chapters'
OUTPUT_FILE = '/home/luna/workspace/Dialogsteuerung/data/chapters/processed_chapters/chapters.csv'

repo_id = 'tiiuae/falcon-40b'

llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperatur": 0, "max_length": 1000})

template = """Proofread and edit this text for errors: {context}

Here's the corrected and edited text:"""
prompt = PromptTemplate(template=template, input_variables=["context"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

for file in glob.glob(CONTEXT_PATH + '/*.txt'):
    with open(file, 'r') as txt_file:
        input_context = ''.join(txt_file.readlines())
        edited_context = llm_chain.run(input_context)
        with open(OUTPUT_FILE, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(edited_context)

question_template = """What are questions and answers for this paragraph: {context}

Here's are some questions and answers based on the provided paragraph:"""
