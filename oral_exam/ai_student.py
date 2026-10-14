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

from oral_exam import llm

from oral_exam.utils.paths import run_file

logger = logging.getLogger(__name__)

TEMPLATE = """Du bist eine durchschnittliche Studentin an einer deutschen Universität.
Du wirst in einer mündlichen Prüfung zum Thema {subject} abgefragt.
Antworte auf die Frage in einem Satz.
Die Frage lautet: {question}

Gib nur deine Antwort zurück:"""

class Student:
    """
    Answers exam questions in place of a person, for testing without a
    microphone. Everything it is asked and answers is written to a transcript
    in the run directory, named after the course.
    """
    def __init__(self, course):
        self.subject = course.title
        started = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        self.transcript = run_file(f"ai-student_{started}.txt", course.id)
        self.write(f"Trainingsprüfung von: {started}\n\n"
                   f"Kurs: {course.title}\n"
                   f"Modell: {llm.MODEL}\n"
                   f"Template: {TEMPLATE}\n")

    def write(self, text):
        with open(self.transcript, 'a', encoding='utf-8', newline='') as handle:
            handle.write(f"{text}\n")

    def log(self, output):
        """Records something the examiner said or decided."""
        self.write(f"[Exam:] {output}")

    def get_answer(self, question):
        answer = llm.chat(TEMPLATE.format(subject=self.subject, question=question))
        self.write(f"[Exam:] {question}")
        self.write(f"[AI:] {answer}")
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
            student.log(question)

            # Generate an answer
            if question.endswith('?'):
                answer = student.get_answer(question)
                print(f"AI: {answer}")

                process.stdin.write(f"{answer}\n")
                process.stdin.flush()

            if re.search("End!", question):
                break
    finally:
        process.terminate()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    import courselib
    repository = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    run_exam_realtime([sys.executable, os.path.join(repository, "start_exam"),
                       "-n", "Luna", "-f", "--mute"],
                      Student(courselib.get(courselib.default_course_id())))
