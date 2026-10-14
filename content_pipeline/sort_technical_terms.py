"""
Helper: normalise the technical term list of a course.

    python content_pipeline/sort_technical_terms.py --course oop

Lower cases, transliterates umlauts, sorts and removes duplicates, writing the
file back in place. The list itself is written by hand - this only tidies it.
Synonyms are written as '[alias, aliasing]' on one line.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _course import materials_path  # noqa: E402

_parser = argparse.ArgumentParser(description="Normalise a course's technical term list.")
_parser.add_argument("-c", "--course", required=True, help="Id of the course.")
_parser.add_argument("--file", help="Override the term list from the manifest.")
_args = _parser.parse_args()

index = _args.file or materials_path(_args.course, "technical_terms")
if not index:
    sys.exit(f"The course '{_args.course}' declares no materials.technical_terms.")
print(f"Normalising {index}")


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
