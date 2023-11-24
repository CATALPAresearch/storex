import csv
import glob
import os
import re

directory = os.path.dirname(os.path.dirname(__file__))
INPUT_FILE = os.path.join(directory, 'data/chapters_processed')
OUTPUT_FILE = os.path.join(directory, 'data/processed/chapters.csv')

count = 0
# Get text from txt files
for file in glob.glob(INPUT_FILE + '/*.txt'):
    with open(file, 'r') as txt_file:
        lines = txt_file.readlines()
        lines = lines[lines.index('\n') + 1:]
        paragraph = ''.join(lines[:lines.index('\n')])

        for i, line in enumerate(lines):
            if re.search("Frage:", line):
                question = line.split(':', 1)[1].strip()  # TODO: Catch errors
                answer = lines[i + 1].split(':', 1)[1].strip()
                text_context = [paragraph.rstrip(), question, answer]

                with open(OUTPUT_FILE, 'a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    if count == 0:
                        csv_writer.writerow(['paragraph', 'question', 'answer'])
                        count += 1
                    csv_writer.writerow(text_context)
