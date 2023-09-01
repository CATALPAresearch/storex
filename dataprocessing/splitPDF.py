import PyPDF2
import re

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.disabled = False

INPUT_PATH = '/home/luna/workspace/Dialogsteuerung/data/pdf/Kurstext_OOP.pdf'
OUTPUT_PATH = '/home/luna/workspace/Dialogsteuerung/data/chapters/'


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

    # Remove second element from too long chapter name
    content_table.remove('Klasseninvarianten')

    # Remove everything before first chapter
    for line in document[end_content:]:
        if re.search('1 Objekte', line):
            start_chapter = document.index(line)
            break
    del document[:start_chapter]
    return content_table


text_lines = extract_text_from_pdf(INPUT_PATH)
chapters = get_chapters(text_lines)
logger.debug("Amount of chapters:" + str(len(chapters)))

num = 0
for i in reversed(range(len(text_lines))):
    if chapters and re.search(chapters[-1][:5], text_lines[i]):
        chapter = chapters.pop()
        # Save chapters as individual text files
        if chapter[0].isdigit() and not re.search('Lösungen zu den Selbsttestaufgaben', chapter):
            paragraph = text_lines[i:]
            chapter_no = chapter.split(' ', 1)[0]
            outpath = OUTPUT_PATH + chapter_no + '.txt'
            with open(outpath, 'w') as outfile:
                for lines in paragraph:
                    outfile.write("%s\n" % lines)
            num += 1
        text_lines = text_lines[:i]

logger.debug("Left lines of text:" + str(len(text_lines)))
logger.debug("Amount of paragraphs:" + str(num))
