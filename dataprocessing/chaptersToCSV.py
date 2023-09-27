import glob
import csv

INPUT_FILE = "/home/luna/workspace/Dialogsteuerung/data/chapters"
OUTPUT_FILE = "/home/luna/workspace/Dialogsteuerung/data/processed/chapters.csv"

count = 0
# Get text from txt files
for file in glob.glob(INPUT_FILE + '/*.txt'):
    with open(file, 'r') as txt_file:
        text_content = ''.join(line for line in txt_file)

    with open(OUTPUT_FILE, 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        if count == 0:
            csv_writer.writerow(['paragraph'])
            count += 1
        csv_writer.writerow([text_content])
