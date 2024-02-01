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

KE1_questions = [[], [], []]
KE2_questions = [[], [], []]
KE3_questions = [[], [], []]
KE4_questions = [[], [], []]
KE6_questions = [[], [], []]

KE_questions = [KE1_questions, KE2_questions, KE3_questions, KE4_questions, KE6_questions]


def sort_in_ke(question_answer, ke_index):
    if question_answer['question'].startswith(("Was ist", "Was sind", "Welche")):
        KE_questions[ke_index][0].append(question_answer)
    elif question_answer['question'].startswith(("Wie", "Wann")):
        KE_questions[ke_index][1].append(question_answer)
    else:  # ("Was unterscheidet", "Warum")
        KE_questions[ke_index][2].append(question_answer)


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
                    ke = 0
                if filename == "KE2":
                    ke = 1
                if filename == "KE3":
                    ke = 2
                if filename == "KE4":
                    ke = 3
                if filename == "KE5":
                    ke = 3
                if filename == "KE6":
                    ke = 5
            elif float(filename) < 6:
                ke = 0
            elif float(filename) < 17:
                ke = 1
            elif float(filename) < 33:
                ke = 2
            elif float(filename) < 53:
                ke = 3  # KE 4 until 49, then KE 5
            else:
                ke = 4  # KE 6 until 61, then KE 7
            sort_in_ke(question_dict, ke)

with open(OUTPUT_FILE, 'a') as py_file:
    for ke in range(len(KE_questions)):
        py_file.write(f"KE{ke+1}_questions = [\n") if ke <= 3 else py_file.write(f"KE{ke+2}_questions = [\n")
        for question_list in KE_questions[ke]:
            for question_dictionary in question_list:
                if question_dictionary == question_list[0]:
                    py_file.write(f"    [{question_dictionary},\n")
                elif question_dictionary == question_list[-1]:
                    py_file.write(f"     {question_dictionary}],\n")
                else:
                    py_file.write(f"     {question_dictionary},\n")
        py_file.write("]\n")
