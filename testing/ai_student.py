"""
Simulated student that answers exam questions, used to test the dialogue system
without a microphone and without a human.
"""
import logging
import os
import re
import subprocess
import sys

from datetime import datetime

import llm

from utils.paths import output_file

logger = logging.getLogger(__name__)

TEMPLATE = """Du bist eine durchschnittliche Studentin an einer deutschen Universität.
Du wirst in einer mündlichen Prüfung zu objektorientierter Programmierung abgefragt.
Antworte auf die Frage in einem Satz.
Die Frage lautet: {question}

Gib nur deine Antwort zurück:"""

date = datetime.now().strftime("%d-%m-%Y--%H-%M-%S")
OUTPUT_FILE = output_file(f"test_results_AI_{date}.txt")


def write_output(output):
    with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as test_file:
        test_file.write(f"[Exam:] {output}\n")


class Student:
    def __init__(self):
        with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as test_file:
            test_file.write(f"Trainingsprüfung von: {date}\n\n"
                            f"Modell: {llm.MODEL}\n"
                            f"Template: {TEMPLATE}\n\n")

    def get_answer(self, question):
        answer = llm.chat(TEMPLATE.format(question=question))
        with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as test_file:
            test_file.write(f"[Exam:] {question}\n")
            test_file.write(f"[AI:] {answer}\n")
        return answer


def run_exam_realtime(command, student):
    """
    Drives the command line exam as a subprocess and answers its questions.
    """
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    try:
        for line in process.stdout:
            question = line.strip()
            if not question:
                continue
            print(f"Exam: {question}")
            write_output(question)

            # Generate an answer
            if question.endswith('?'):
                answer = student.get_answer(question)
                print(f"AI: {answer}")
                with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as test_file:
                    test_file.write(f"[AI:] {answer}\n")

                process.stdin.write(f"{answer}\n")
                process.stdin.flush()

            if re.search("End!", question):
                break
    finally:
        process.terminate()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
        file.write(f"Trainingsprüfung von: {date}\n\n")

    exam_script = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "start_exam")
    run_exam_realtime([sys.executable, exam_script, "-n", "Luna", "-f", "--mute"], Student())
