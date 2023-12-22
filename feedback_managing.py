from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate

from utils.helpers import KE, Level


class FeedbackManager:
    def __init__(self):
        self.missed_term_counter = 0
        self.reiterated_counter = 0
        self.no_entailment_counter = 0
        self.correct_answers = []
        self.completed_level = []
        for unit in KE:
            self.correct_answers.append(0)
            self.completed_level.append(None)

    def add_missed(self, count):
        self.missed_term_counter += count

    def add_reiterated(self):
        self.reiterated_counter += 1

    def add_no_entailment(self):
        self.no_entailment_counter += 1

    def add_feedback(self, correct, ke, level):
        self.correct_answers[ke] += correct
        self.completed_level[ke] = level


# Load a text-generation model on the hub
# llm = HuggingFaceHub(repo_id='google/flan-t5-large',  # Text Generation, e.g. LlaMA
#                      model_kwargs={'temperature': 0,
#                                    'max_length': 1024})
# template = """Du bist ein Professor an einer deutschen Universität.
# Gib Feedback für deine Studentin nach einer mündlichen Prüfung, welches die folgenden Kernpunkte beinhaltet:
# Kernpunkte: {feedback_points}
# Gib nur das Feedback zurück:"""
# # prompt_template = PromptTemplate.from_template(template)
# # prompt = prompt_template.format(c_answer=correct_answer, s_answer=student_answer)
# prompt = PromptTemplate(template=template, input_variables=['feedback_points'])
# llm_chain = LLMChain(prompt=prompt, llm=llm)
# feedback_points = "Test Feedback"
# differences = llm_chain.run({'feedback_points': feedback_points})
