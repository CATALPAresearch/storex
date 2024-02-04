import os
import re
import subprocess

from datetime import datetime
from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate


os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

date = datetime.now().strftime("%d-%m-%Y--%H-%M-%S")
directory = os.path.dirname(__file__)
OUTPUT_FILE = os.path.join(directory, f"test_results_AI_{date}")


def write_output(output):
    with open(OUTPUT_FILE, 'a', newline='') as test_file:
        test_file.write(f"[Exam:] {output}\n")


class Student:
    def __init__(self):
        template = (""""[INST] Du eine durchschnittliche Studentin an einer deutschen Universität.
        Du wirst in einer mündlichen Prüfungen zu objektorientierter Programmierung abgefragt.
        Antworte auf die Frage in einem Satz.
        Die Frage lautet: {question}

        Gib nur deine Antwort zurück:[/INST]""")

        prompt = PromptTemplate(template=template, input_variables=['question'])

        model = 'mistralai/Mixtral-8x7B-Instruct-v0.1'
        llm = HuggingFaceHub(repo_id=model,
                             model_kwargs={'max_new_tokens': 512, 'raw_response': True})

        self.llm_chain = LLMChain(prompt=prompt,
                                  llm=llm)

        with open(OUTPUT_FILE, 'a', newline='') as test_file:
            test_file.write(f"Trainingsprüfung von: {date}\n\n"
                            f"Modell: {model}\n"
                            f"Template: {template}\n\n")

    def get_answer(self, question):
        answer = self.llm_chain.run(question)
        with open(OUTPUT_FILE, 'a', newline='') as test_file:
            test_file.write(f"[Exam:] {question}\n")
            test_file.write(f"[AI:] {answer}\n")
        return answer


def run_exam_realtime(command, student):
    try:
        process = subprocess.Popen(command,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   text=True)

        while True:
            question = ''
            # Process each line of stdout in real-time
            for line in process.stdout:
                question = line.strip()
                print(f"Exam: {question}")
                with open(OUTPUT_FILE, 'a', newline='') as test_file:
                    test_file.writelines(f"[Exam:] {question}\n")

                # Generate an answer
                if question.endswith('?'):
                    answer = student.get_answer(question)
                    print(f"AI: {answer}")
                    with open(OUTPUT_FILE, 'a', newline='') as test_file:
                        test_file.write(f"[AI:] {answer}\n")

                    process.stdin.write(f"{answer}\n")
                    process.stdin.flush()

            if re.search("End!", question):
                break

        # Close the subprocess
        process.terminate()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    with open(OUTPUT_FILE, 'a', newline='') as file:
        file.write(f"Trainingsprüfung von: {date}\n\n")

    ai_student = Student()
    command_to_run = ["/home/luna/workspace/Dialogsteuerung/exam.py"]
    run_exam_realtime(command_to_run, ai_student)
