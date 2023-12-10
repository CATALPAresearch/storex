"""
Script to write the questions and answers from the processed chapters into the questions.py file.
"""
import glob
import os

from pathlib import Path

directory = os.path.dirname(os.path.dirname(__file__))
INPUT_PATH = os.path.join(directory, 'data/chapters_processed')
OUTPUT_FILE = os.path.join(directory, 'questions/questions.py')

KE1_questions = []
KE2_questions = []
KE3_questions = []
KE4_questions = []
KE5_questions = []
KE7_questions = []

# Get text from txt files
for file in glob.glob(INPUT_PATH + '/*.txt'):
    filename = Path(file).stem
    filename = ".".join(filename.split(".", 2)[:2])

    with open(file, 'r') as txt_file:
        lines = txt_file.readlines()
        question_lines = [line for line in lines if line.startswith("Frage:")]
        for question in question_lines:
            answer = lines[lines.index(question) + 1]
            answer = answer.split(':', 1)[1].strip()
            question = question.split(':', 1)[1].strip()
            question_dict = {'question': question, 'answer': answer}

            try:
                # Get files from KE1
                if float(filename) < 4.3:
                    KE1_questions.append(question_dict)
                # Get files from KE2 - 7
                else:
                    KE2_questions.append(question_dict)
            # KE files: Check number
            except:
                ke_number = int(filename[-1])
                ke_list = f"KE{ke_number}_questions"
                # ke_list.append(question_dict)

with open(OUTPUT_FILE, 'a') as py_file:
    py_file.write(f"KE1_questions = {KE1_questions}")
