"""
Script to write the questions and answers from the processed chapters into the questions.py file.
"""
import glob
import os
import re

from pathlib import Path

directory = os.path.dirname(os.path.dirname(__file__))
INPUT_PATH = os.path.join(directory, 'data/chapters_processed')
OUTPUT_FILE = os.path.join(directory, 'questions/questions.py')

KE1_questions = []
KE2_questions = []
KE3_questions = []
KE4_questions = []
KE5_questions = []
KE6_questions = []
KE7_questions = []

# Get text from txt files
for file in glob.glob(INPUT_PATH + '/*.txt'):
    filename = Path(file).stem
    filename = ".".join(filename.split(".", 2)[:2])

    with (open(file, 'r') as txt_file):
        lines = txt_file.readlines()
        question_lines = [line for line in lines if line.startswith("Frage:")]
        for question in question_lines:
            answer = lines[lines.index(question) + 1]
            answer = answer.split(':', 1)[1].strip()
            question = question.split(':', 1)[1].strip()
            question_dict = {'question': question, 'answer': answer}

            if re.match("KE", filename):
                if filename == "KE1":
                    KE1_questions.append(question_dict)
                if filename == "KE2":
                    KE2_questions.append(question_dict)
                if filename == "KE3":
                    KE3_questions.append(question_dict)
                if filename == "KE4":
                    KE4_questions.append(question_dict)
                if filename == "KE5":
                    KE5_questions.append(question_dict)
                if filename == "KE7":
                    KE7_questions.append(question_dict)
            elif float(filename) < 6:
                KE1_questions.append(question_dict)
            elif float(filename) < 17:
                KE2_questions.append(question_dict)
            elif float(filename) < 33:
                KE3_questions.append(question_dict)
            elif float(filename) < 49:
                KE4_questions.append(question_dict)
            elif float(filename) < 53:
                KE5_questions.append(question_dict)
            elif float(filename) < 61:
                KE6_questions.append(question_dict)
            else:
                KE7_questions.append(question_dict)

with open(OUTPUT_FILE, 'a') as py_file:
    py_file.write(f"KE1_questions = {KE1_questions}\n")
