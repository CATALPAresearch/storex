"""
Step 1: split a course document into one text file per chapter.

    python content_pipeline/01_split_pdf.py --course oop

Be warned: this is a scraper written for one particular book. The German
markers it looks for ('Kurseinheit 1:', 'Verzeichnis der Weblinks'), the page
offsets and several hand patched special cases are specific to the OOP course
text. For another document it has to be adapted, not merely configured.

Its output still needs manual work before step 2: the raw chapters are cleaned
up, renamed to KE*.txt and complemented by the FragenKE*.txt files. See the
README in this directory.
"""
import argparse
import logging
import os
import re
import sys

import PyPDF2

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _course import source_path  # noqa: E402

_parser = argparse.ArgumentParser(description="Split a course document into chapters.")
_parser.add_argument("-c", "--course", required=True, help="Id of the course.")
_parser.add_argument("--document", help="Override the document from the manifest.")
_parser.add_argument("--output", help="Override the output directory.")
_args = _parser.parse_args()

INPUT_PATH = source_path(_args.course, "document", _args.document)
OUTPUT_PATH = (_args.output or source_path(_args.course, "chapters_raw")).rstrip("/") + "/"
if not os.path.isdir(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH, exist_ok=True)
print(f"{INPUT_PATH} -> {OUTPUT_PATH}", file=sys.stderr)

code_number = 1679
footnote_number = 95


def extract_text_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    text = []
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        page_text = page_obj.extract_text().splitlines()
        text.extend(page_text)
        # Prepare text
        text = [i.strip() for i in text]
        text = [i for i in text if i]
        text = [i.replace('  ', ' ') for i in text]
        # Remove side notations
        if page_num > 24:
            last_line = text[-1]
            while not last_line[0].isdigit() and len(last_line) < 22 and '!' not in last_line\
                    and not ('.' in last_line and 'vs.' not in last_line):
                text.pop()
                last_line = text[-1]
    pdf_file_obj.close()
    return text


def get_chapters(document):
    start_content = None
    end_content = None
    # Find start and end of the table of contents
    for line in document:
        if start_content is None and re.search('Kurseinheit 1:', line):
            start_content = document.index(line)
        if start_content and re.search('Verzeichnis der Weblinks', line):
            end_content = document.index(line)
            break

    if start_content is None or end_content is None:
        print("No start or end of the table of contents found! Check the search string")
        exit(1)

    # Create a list of contents
    content_table = document[start_content:(end_content + 2)]
    for i in reversed(range(len(content_table))):
        title, seperator, tail = content_table[i].partition(' ..')
        # Deal with long chapter names (29.2 and 52.6)
        if seperator != ' ..':
            if title[-1].isdigit():
                title = title.rsplit(' ', 1)[0]
            else:
                x = content_table.pop(i + 1)
                title += (' ' + x)
            logger.debug("Fixed long chapter name: " + title)
            # Mark long chapter name for writing
            title += '$'
        content_table[i] = title

    # Remove chapter 1.1 (its content will be appended to chapter 1.)
    logger.debug("Second chapter: " + str(content_table[2]))
    content_table.pop(2)
    logger.debug("Chapter 1.1 removed. New second chapter: " + str(content_table[2]))

    # Remove everything before first chapter
    for line in document[end_content:]:
        if re.search('Kurseinheit 1:', line):
            start_chapter = document.index(line)
            break
    del document[:start_chapter]

    return content_table


def format_paragraph(paragraph):
    global code_number
    global footnote_number
    for i in reversed(range(len(paragraph))):
        if i == 1:
            break
        if paragraph[i][0].isdigit():
            number = paragraph[i].split(' ', 1)[0]
            if any(punctuation in [',', '.', '!', ':', ')', '(', '>', '<'] for punctuation in number):
                pass
            # Remove lines with code
            else:
                paragraph.pop(i)

            # # Change code lines to markdown representation
            # elif int(number) == code_number:
            #     paragraph[i].replace(str(number), '   ')
            #     code_number -= 1
            #     # Code in removed chapters
            #     while code_number in [1252, 1251, 981, 980, 979, 978, 977, 976]:
            #         code_number -= 1
            #     if code_number == 832:
            #         code_number = 710
            #     if code_number == 278:
            #         code_number = 261
            # # Remove footnotes
            # elif int(number) == footnote_number:
            #     paragraph = paragraph[:i]
            #     footnote_number -= 1
            #     if footnote_number == 56:
            #         footnote_number -= 1

        elif re.search('Selbsttestaufgabe', paragraph[i]):
            pass

    return paragraph


def output_chapters(text, content_table):
    for i in reversed(range(len(text))):
        # Save Kurseinheit introduction chapters
        if content_table and re.search("Kurseinheit", content_table[-1]):
            if re.search(content_table[-1][:14], text[i]):
                chapter = content_table.pop()
                paragraph = text[i:]
                chapter_no = chapter.split(':', 1)[0]
                outpath = OUTPUT_PATH + chapter_no + '.txt'
                with open(outpath, 'w') as outfile:
                    for lines in paragraph:
                        outfile.write("%s\n" % lines)
                text = text[:i]

        elif content_table and re.search(content_table[-1][:5], text[i]):
            chapter = content_table.pop()

            # Save chapters as individual text files
            if chapter[0].isdigit() and not re.search('Lösungen zu den Selbsttestaufgaben', chapter) \
                    and not re.search('Fazit', chapter) and not re.search('Zusammenfassung', chapter):
                paragraph = text[i:]
                # Deal with long chapter names (29.2 and 52.6)
                if chapter[-1] == '$':
                    chapter = chapter[:-1]
                    paragraph[1] = chapter
                    paragraph = paragraph[1:]
                paragraph = format_paragraph(paragraph)
                chapter_no = chapter.split(' ', 1)[0]
                outpath = OUTPUT_PATH + chapter_no + '.txt'
                with open(outpath, 'w') as outfile:
                    for lines in paragraph:
                        outfile.write("%s\n" % lines)
            text = text[:i]

    logger.debug("Left lines of text (should be 0): " + str(len(text)))


text_lines = extract_text_from_pdf(INPUT_PATH)
chapters = get_chapters(text_lines)
logger.debug("Amount of chapters: " + str(len(chapters)))

output_chapters(text_lines, chapters)
