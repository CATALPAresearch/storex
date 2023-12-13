import os

directory = os.path.dirname(os.path.dirname(__file__))
index = os.path.join(directory, 'data/technical_terms')

with (open(index, 'r') as txt_file):
    new_lines = []
    lines = txt_file.readlines()
    for line in lines:
        line = line.lower().strip()
        line = line + '\n'
        new_lines.append(line)
    new_lines = sorted(new_lines)
with open(index, 'w') as txt_file:
    txt_file.writelines(new_lines)
