"""
Optional: export the chapters of a course as a fine-tuning data set.

    python content_pipeline/export_training_data.py --course oop

Writes paragraph, question and answer of every annotated chapter into a CSV.
This is not part of the exam pipeline; it only feeds the scripts under
finetuning/, which train a question generation model. Those load their data
from the Hugging Face Hub, so the CSV written here is the source that was
uploaded, not something read at training time.
"""
import argparse
import csv
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _course import source_path  # noqa: E402

_parser = argparse.ArgumentParser(description="Export a course as fine-tuning data.")
_parser.add_argument("-c", "--course", required=True, help="Id of the course.")
_parser.add_argument("--chapters", help="Override the chapter directory from the manifest.")
_parser.add_argument("--output", help="Override the CSV to write.")
_args = _parser.parse_args()

INPUT_PATH = source_path(_args.course, "chapters", _args.chapters)
OUTPUT_FILE = _args.output or os.path.join(
    source_path(_args.course, "dataset"), "train.csv")
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
print(f"{INPUT_PATH} -> {OUTPUT_FILE}")


count = 0
# Get text from txt files
for file in glob.glob(INPUT_PATH + '/*.txt'):
    with open(file, 'r') as txt_file:
        lines = txt_file.readlines()
        # Remove the title and empty lines
        lines = lines[lines.index('\n') + 1:]
        lines = [line for line in lines if line.strip()]

        while lines:
            # Get the next paragraph and remove it from the lines
            paragraph = ""
            while lines and not lines[0].startswith("Frage:") and not lines[0].startswith("Antwort:"):
                paragraph += lines.pop(0).rstrip()

            # Get the next question and its answer and remove them from the lines
            while lines and lines[0].startswith("Frage:"):
                question = lines.pop(0).split(':', 1)[1].strip()
                answer = lines.pop(0).split(':', 1)[1].strip()

                # Create a row with the paragraph, the question and the answer and write it to the CSV file
                text_context = [paragraph, question, answer]
                with open(OUTPUT_FILE, 'a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    if count == 0:
                        csv_writer.writerow(['paragraph', 'question', 'answer'])
                        count += 1
                    csv_writer.writerow(text_context)
