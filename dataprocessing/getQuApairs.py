import glob
import re

INPUT_PATH = '/home/luna/workspace/Dialogsteuerung/data/chapters/'


def read_txt(chapter_file):
    with open(chapter_file, 'r') as f:
        content = f.readlines()
    return content


def get_questions(topic):
    questions = []
    # Simple "what" question
    if topic.split(' ', 1)[0] in ['Der', 'Die', 'Das']:
        question = 'Was ist d' + topic[1:] + '?'
    elif topic[-1] in ['n', 'e']:
        question = 'Was sind ' + topic + '?'
    else:
        question = 'Was ist ' + topic + '?'
    questions.append(question)

    # Question for solution to a problem
    if re.search('Problem', topic):
        questions.append('Was kann man gegen d' + topic[1:] + ' tun?')
        return questions

    if re.search(' und ', topic):
        questions.append('Was unterscheidet ' + topic + '?')
        print(questions)

    return questions


files = glob.glob(INPUT_PATH + '*.txt')
for file in files:
    chapter = read_txt(file)
    chapter_title = chapter[0].split(' ', 1)[1]
    question_list = get_questions(chapter_title[0:-1])
