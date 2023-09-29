import glob
import csv
import re

INPUT_FILE = "/home/luna/workspace/Dialogsteuerung/data/chapters/processed_chapters"
OUTPUT_FILE = "/home/luna/workspace/Dialogsteuerung/data/processed/chapters.csv"

count = 0
# Get text from txt files
for file in glob.glob(INPUT_FILE + '/*.txt'):
    with open(file, 'r') as txt_file:
        lines = txt_file.readlines()
        lines = lines[lines.index('\n') + 1:]
        paragraph = ''.join(lines[:lines.index('\n')])

        # paragraph = ''.join(line for line in txt_file if line.strip() and not (re.search("Frage", line)
        #                                                                        or re.search("Antwort", line)
        #                                                                        or line[0].isdigit()))

        for i, line in enumerate(lines):
            if re.search("Frage", line):
                text_context = [paragraph.rstrip(), line.rstrip(), lines[i + 1].rstrip()]

                with open(OUTPUT_FILE, 'a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    if count == 0:
                        csv_writer.writerow(['paragraph', 'question', 'answer'])
                        count += 1
                    csv_writer.writerow(text_context)
