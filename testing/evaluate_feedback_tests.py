"""
Counts how often the generated feedback mentions each performance criterion.
"""
import os
import re

CONTINUATION_INDENT = '                      '

directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE = os.path.join(directory, 'testing/prompt_feedback_01.txt')
words = [" du ", "inhaltlich", "relevant", "vollständig", "präzis", "Hilfe"]
occurrence = [0] * len(words)

# Get text from txt files
with open(INPUT_FILE, 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()

# Join wrapped lines onto the line they belong to
for i, line in reversed(list(enumerate(lines))):
    # A continuation of the first line has nothing to be joined to
    if i > 0 and line.startswith(CONTINUATION_INDENT):
        lines[i - 1] = lines[i - 1].rstrip('\n') + line
        lines.pop(i)

for line in lines:
    if line.startswith("Generiertes Feedback:"):
        for k, word in enumerate(words):
            if re.search(word, line):
                occurrence[k] += 1

for word, number in zip(words, occurrence):
    print(f"{word}: {number}")
