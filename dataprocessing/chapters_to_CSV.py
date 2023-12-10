"""
Script to write the paragraph, questions and answers from the processed chapters into a CSV file.
"""
import csv
import glob
import os

directory = os.path.dirname(os.path.dirname(__file__))
INPUT_PATH = os.path.join(directory, 'data/chapters_processed')
OUTPUT_FILE = os.path.join(directory, 'data/processed/chapters.csv')

count = 0
# Get text from txt files
for file in glob.glob(INPUT_PATH + '/*.txt'):
    with open(file, 'r') as txt_file:
        lines = txt_file.readlines()
        # Remove the title from the lines
        lines = lines[lines.index('\n') + 1:]

        # Get the next paragraph and remove it from the lines
        while lines and '\n' in lines:
            paragraph = ''.join(lines[:lines.index('\n')]).rstrip()
            lines = lines[lines.index('\n') + 1:]

            # Get the next question and its answer and remove them from the lines
            while lines[0][:5] == "Frage":
                question = lines[0].split(':', 1)[1].strip()  # TODO: Catch errors?
                answer = lines[1].split(':', 1)[1].strip()
                lines = lines[3:]

                # Create a row with the paragraph, the question and the answer and write it to the CSV file
                text_context = [paragraph, question, answer]
                with open(OUTPUT_FILE, 'a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    if count == 0:
                        csv_writer.writerow(['paragraph', 'question', 'answer'])
                        count += 1
                    csv_writer.writerow(text_context)
