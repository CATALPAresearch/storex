"""
Script for changing csv datasets from having separate answer and question columns ot having one answer-question column.
"""
import csv
import glob
import os

directory = os.path.dirname(os.path.dirname(__file__))
PATH = os.path.join(directory, 'data/processed')

# Get text from csv files
for in_file in glob.glob(PATH + '/*.csv'):
    if 'qag' not in str(in_file):
        out_file = os.path.join(PATH, in_file.split('.')[0] + '_qag.csv')
        count = 0
        with open(in_file, 'r') as file:
            csvreader = csv.DictReader(file)
            for row in csvreader:
                answer_question = "<answer> " + row['answer'] + " <answer> <question> " + row['question'] + " <question>"
                qag_rows = [row['paragraph'], answer_question]

                with open(out_file, 'a', newline='') as qag_file:
                    csv_writer = csv.writer(qag_file)
                    if count == 0:
                        csv_writer.writerow(['paragraph', 'answer-question'])
                        count += 1
                    csv_writer.writerow(qag_rows)
