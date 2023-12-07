"""
Script to process raw QuAD file for Question Generation format.

Run the following command beforehand, for downloading the german splitter:
    python -m spacy download de_core_news_sm

Split when uploading to dataset hub by:
    gsplit -l 1500 -d --additional-suffix=.jsonl train.jsonl train
"""
import json
import os
import re
import spacy

from glob import glob
from tqdm import tqdm
from typing import Dict

SPLITTER = spacy.load('de_core_news_sm')
HIGHLIGHT_TOKEN = '<hl>'

directory = os.path.dirname(os.path.dirname(__file__))
INPUT_FILE = os.path.join(directory, 'data/raw/QuA_Einsendeaufgaben.jsonl')
OUTPUT_PATH = os.path.join(directory, 'data/processed/')
OUTPUT_FILE = 'train'


def get_sentence(document: str):
    return [str(sent) for sent in SPLITTER(document).sents]


def jsonline_reader(filename: str):
    with open(filename, 'r') as f_reader:
        examples = [json.loads(i) for i in f_reader.read().split('\n') if len(i) > 0]
    return examples


def process_single_data(data: Dict):
    """ Convert single raw json data into QG format """
    if data["sentence"]:
        example = {'question': data["question"], 'paragraph': data["paragraph"], 'answer': data["answer"],
                   'sentence': data["sentence"]}
    else:
        example = {'question': data["question"], 'paragraph': data["context"], 'answer': data["answer"]}

        # get sentence
        position = example['paragraph'].find(example['answer'])
        assert position != -1
        before_tmp = get_sentence(example['paragraph'][:position])
        if len(before_tmp) == 0:
            before_sentence = ''
        else:
            if before_tmp[-1].endswith('.'):
                before_sentence = ''
            else:
                before_sentence = before_tmp[-1]
                before_sentence = before_sentence if before_sentence.endswith(' ') else '{} '.format(before_sentence)
        after_tmp = get_sentence(example['paragraph'][position + len(example['answer']):])
        if len(after_tmp) == 0:
            after_sentence = ''
        else:
            after_sentence = after_tmp[0]
            after_sentence = after_sentence if after_sentence.startswith(' ') else ' {}'.format(after_sentence)
        example['sentence'] = '{}{}{}'.format(before_sentence, example['answer'], after_sentence)

    # get paragraph_sentence
    position_sentence = example['paragraph'].find(example['sentence'])
    assert position_sentence != -1
    source_text = '{0}{1} {2} {1}{3}'.format(
        example['paragraph'][:position_sentence], HIGHLIGHT_TOKEN, example['sentence'],
        example['paragraph'][position_sentence + len(example['sentence']):])
    example['paragraph_sentence'] = re.sub(r'\s+', ' ', source_text)

    # get paragraph_answer
    position = example['paragraph'].find(example['answer'])
    assert position != -1
    source_text = '{0}{1} {2} {1}{3}'.format(
        example['paragraph'][:position], HIGHLIGHT_TOKEN, example['answer'],
        example['paragraph'][position + len(example['answer']):])
    example['paragraph_answer'] = re.sub(r'\s+', ' ', source_text)

    # get sentence_answer
    position_answer = example['sentence'].find(example['answer'])
    assert position != -1
    source_text = '{0}{1} {2} {1}{3}'.format(
        example['sentence'][:position_answer], HIGHLIGHT_TOKEN, example['answer'],
        example['sentence'][position_answer + len(example['answer']):])
    example['sentence_answer'] = re.sub(r'\s+', ' ', source_text)

    return example


if __name__ == '__main__':
    output = OUTPUT_PATH
    os.makedirs(output, exist_ok=True)
    path = {OUTPUT_FILE: INPUT_FILE}
    for k, v in path.items():
        json_data = []
        for _file in sorted(glob(v)):
            json_data += jsonline_reader(_file)
        with open('{}/{}.jsonl'.format(output, k), 'w') as f:
            for single_data in tqdm(json_data):
                single_data = process_single_data(single_data)
                f.write(json.dumps(single_data) + '\n')
