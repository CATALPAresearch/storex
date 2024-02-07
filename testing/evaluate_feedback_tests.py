import os
import re

directory = os.path.dirname(os.path.dirname(__file__))
INPUT_FILE = os.path.join(directory, 'testing/prompt_feedback_01.txt')
words = [" du ", "inhaltlich", "relevant", "vollständig", "präzis", "Hilfe"]
occurrence = [0, 0, 0, 0, 0, 0, 0]

# Get text from txt files
with open(INPUT_FILE, 'r') as txt_file:
    lines = txt_file.readlines()
    # Remove the title and empty lines
    spaces = '                      '
    for i, line in reversed(list(enumerate(lines))):
        if line.startswith('                      '):
            lines[i-1] += line
            lines.pop(i)
    for line in lines:
        if line.startswith("Generiertes Feedback:"):
            for k in range(len(words)):
                if re.search(words[k], line):
                    occurrence[k] += 1
for word, number in zip(words, occurrence):
    print(f"{word}: {number}")
