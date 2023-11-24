import json
import csv

INPUT_FILE = "/home/luna/workspace/Dialogsteuerung/data/processed/train.jsonl"
OUTPUT_FILE = "/home/luna/workspace/Dialogsteuerung/data/processed/train.csv"

count = 0
# Get JSON data from JSONL
with open(INPUT_FILE, 'r') as file:
    for line in file:
        json_data = json.loads(line)

        # Write JSON objects into a CSV file
        with open(OUTPUT_FILE, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            if count == 0:
                header = json_data.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(json_data.values())
