import os


directory = os.path.dirname(os.path.dirname(__file__))
index = os.path.join(directory, 'data/technical_terms.txt')


def custom_sort_key(element):
    # Extract the first letter for sorting
    first_letter = element[0] if element[0] != '[' else element[1]
    return first_letter


with (open(index, 'r') as txt_file):
    new_lines = []
    lines = txt_file.readlines()

for line in lines:
    # Make all words lower case and strip extra whitespaces
    line = line.lower().strip()
    # Replace german umlauts
    umlauts = {ord('ä'): 'ae', ord('ü'): 'ue', ord('ö'): 'oe', ord('ß'): 'ss'}
    line = line.translate(umlauts)

    line = line + '\n'
    new_lines.append(line)

# Sort terms alphabetically
new_lines = sorted(new_lines, key=custom_sort_key)

# Remove doubles
i = 0
while i < len(new_lines):
    if new_lines[i] == new_lines[i-1]:
        new_lines.pop(i)
    else:
        i += 1

with open(index, 'w') as txt_file:
    txt_file.writelines(new_lines)
