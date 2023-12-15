from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate


# Load a text-generation model on the hub
llm = HuggingFaceHub(repo_id='google/flan-t5-large',  # Text Generation, e.g. LlaMA
                     model_kwargs={'temperature': 0,
                                   'max_length': 1024})

template = """Du bist ein Professor an einer deutschen Universität.
Gib Feedback für deine Studentin nach einer mündlichen Prüfung, welches die folgenden Kernpunkte beinhaltet:

Kernpunkte: {feedback_points}

Gib nur das Feedback zurück:"""
# prompt_template = PromptTemplate.from_template(template)
# prompt = prompt_template.format(c_answer=correct_answer, s_answer=student_answer)
prompt = PromptTemplate(template=template, input_variables=['feedback_points'])
llm_chain = LLMChain(prompt=prompt, llm=llm)
feedback_points = "Test Feedback"
differences = llm_chain.run({'feedback_points': feedback_points})
