import PyPDF2
import re

import logging
logger = logging.getLogger()
logger.disabled = False

INPUT_PATH = '/home/luna/workspace/Dialogsteuerung/data/pdf/Kurstext_OOP.pdf'


def extract_text_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        text += page_obj.extract_text()
    pdf_file_obj.close()
    # Prepare text
    text = text.splitlines()
    text = [i.strip() for i in text]
    text = [i for i in text if i]
    text = [i.replace('  ', ' ') for i in text]
    return text


def get_chapters(document):
    # Find start and end of the table of contents
    for line in document:
        if re.search('1 Objekte', line):
            start_content = document.index(line)
            break

    for line in document[start_content:]:
        if re.search('Verzeichnis der Weblinks', line):
            end_content = document.index(line)
            break

    # Create a list of contents
    content_table = document[(start_content):(end_content + 2)]
    for i in range(len(content_table)):
        title, seperator, tail = content_table[i].partition(' ..')
        content_table[i] = title

    # Remove everything before first chapter
    for line in document[end_content:]:
        if re.search('1 Objekte', line):
            start_chapter = document.index(line)
            break
    del document[:start_chapter]
    return content_table


text_lines = extract_text_from_pdf(INPUT_PATH)
chapters = get_chapters(text_lines)
logger.info("Amount of chapters:" + str(len(chapters)))

num = 0
for lines in text_lines:
    if re.search(chapters[0][:6], lines):
    # if lines == chapters[0]:
        print(chapters[0])
        chapters.pop(0)
        num += 1


print(num)
print(chapters[0])

# for line in text:
    # if re.search(chapter[0], line):

