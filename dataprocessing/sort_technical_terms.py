import os
import re


directory = os.path.dirname(os.path.dirname(__file__))
index = os.path.join(directory, 'data/technical_terms.txt')

with (open(index, 'r') as txt_file):
    new_lines = []
    lines = txt_file.readlines()
    for line in lines:
        # TODO: Use utils/preprocessing function
        # Remove non-alphanumeric characters (except for whitespaces and hyphen)
        line = re.sub(r'[^ \w+-]', '', line)
        # Make all words lower case and strip extra whitespaces
        line = line.lower().strip()
        # Replace german umlauts
        umlauts = {ord('ä'): 'ae', ord('ü'): 'ue', ord('ö'): 'oe', ord('ß'): 'ss'}
        line = line.translate(umlauts)

        line = line + '\n'
        new_lines.append(line)
    new_lines = sorted(new_lines)
with open(index, 'w') as txt_file:
    txt_file.writelines(new_lines)
