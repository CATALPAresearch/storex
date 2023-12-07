#!/usr/bin/env python
# coding: utf-8

import evaluate
import nltk
import numpy
import os
import time
import torch

from datasets import concatenate_datasets, load_dataset
from huggingface_hub.hf_api import HfFolder
from transformers import (AutoModelForSeq2SeqLM, AutoTokenizer, DataCollatorForSeq2Seq, Seq2SeqTrainer,
                          Seq2SeqTrainingArguments)

nltk.download("punkt")
HfFolder.save_token("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")

# Log into huggingface account on notebooks like Colab
# from huggingface_hub import notebook_login
# notebook_login()
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Set model and database paths from the huggingface hub
pretrained_model = "google/flan-t5-base"  # TODO: Try "google/flan-t5-large"
finetuned_model = "LunaticTanuki/oop-de-qag-flan-t5-base"
database = "LunaticTanuki/qg_OOP"
data_files = {'train': "train.csv", 'validate': "validate.csv"}


def max_length(column):
    """
    Gets the maximum total sequence length for input or target text after tokenization
    Longer sequences will be truncated and shorter sequences will be padded
    """
    datasets = [dataset['train'], dataset['validate']]
    columns = ['paragraph', 'question']
    # Get the maximum total sequence length after tokenization
    tokenized = concatenate_datasets(datasets).map(
        lambda x: tokenizer(x[column], truncation=True), batched=True, remove_columns=columns)
    maximum = max([len(x) for x in tokenized['input_ids']])
    print(f"Max length of {column}: {maximum}")
    return maximum


def preprocess_function(sample, padding='max_length'):
    """
    Preprocesses the dataset.
    """
    # Add a prefix to the input
    inputs = ["Write a question from this paragraph: " + item for item in sample['paragraph']]
    # Tokenize inputs
    model_inputs = tokenizer(inputs, max_length=max_length_input, padding=padding, truncation=True)
    # Tokenize targets with the `text_target` keyword argument
    labels = tokenizer(text_target=sample['question'], max_length=max_length_output, padding=padding, truncation=True)

    # Pad and replace all tokenizer.pad_token_id in the labels with -100 to ignore padding in the loss
    if padding == 'max_length':
        labels['input_ids'] = [
            [(l if l != tokenizer.pad_token_id else -100) for l in label] for label in labels['input_ids']
        ]

    model_inputs['labels'] = labels['input_ids']
    return model_inputs


def postprocess_text(preds, labels):
    """
    Postprocesses the text.
    """
    preds = [pred.strip() for pred in preds]
    labels = [label.strip() for label in labels]

    # Add newline after each sentence for rougeLSum
    preds = ["\n".join(nltk.tokenize.sent_tokenize(pred)) for pred in preds]
    labels = ["\n".join(nltk.tokenize.sent_tokenize(label)) for label in labels]

    return preds, labels


def compute_metrics(eval_preds):
    preds, labels = eval_preds
    if isinstance(preds, tuple):
        preds = preds[0]
    decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)
    # Replace -100 in the labels as we can't decode them.
    labels = numpy.where(labels != -100, labels, tokenizer.pad_token_id)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

    # Some simple post-processing
    decoded_preds, decoded_labels = postprocess_text(decoded_preds, decoded_labels)

    result = metric.compute(predictions=decoded_preds, references=decoded_labels, use_stemmer=True)
    result = {k: round(v * 100, 4) for k, v in result.items()}
    prediction_lens = [numpy.count_nonzero(pred != tokenizer.pad_token_id) for pred in preds]
    result['gen_len'] = numpy.mean(prediction_lens)
    return result


if __name__ == '__main__':
    start_time = time.time()

    print("Loading dataset...")
    dataset = load_dataset(database, data_files=data_files)
    print(f"Train dataset size: {len(dataset['train'])}")
    print(f"Validation dataset size: {len(dataset['validate'])}")

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Loading pre-trained model to {device}...")
    model = AutoModelForSeq2SeqLM.from_pretrained(pretrained_model).to(device)  # Same as T5ForConditionalGeneration
    tokenizer = AutoTokenizer.from_pretrained(pretrained_model)                 # and T5Tokenizer
    # tokenizer.add_special_tokens(  TODO: Can I add ['<answer>', '<question>'] in as special tokens in the target?
    #     {'additional_special_tokens': ['<answer>', '<context>']}
    # )

    print("Preparing dataset...")
    max_length_input = max_length('paragraph')
    max_length_output = max_length('question')

    tokenized_dataset = dataset.map(preprocess_function, batched=True, remove_columns=['paragraph', 'question', 'answer'])
    print(f"Keys of tokenized dataset: {list(tokenized_dataset['train'].features)}")

    print("Initializing evaluation metric...")
    metric = evaluate.load("rouge")

    print("Initializing data collector...")
    # Ignore tokenizer pad token in the loss
    label_pad_token_id = -100
    # Create data collector for padding the inputs and labels
    data_collator = DataCollatorForSeq2Seq(
        tokenizer,
        model=model,
        label_pad_token_id=label_pad_token_id,
        pad_to_multiple_of=8
    )

    print("Initializing trainer...")
    # Define training arguments
    training_args = Seq2SeqTrainingArguments(
        output_dir=finetuned_model,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        predict_with_generate=True,
        fp16=False,  # True: Half-precision on colab, False: Overflows with fp16
        learning_rate=5e-5,
        num_train_epochs=8,
        # logging_dir=f"{finetuned_model}/logs",
        # logging_strategy="steps",
        # logging_steps=500,
        evaluation_strategy='epoch',
        save_strategy='epoch',
        save_total_limit=2,
        load_best_model_at_end=True,
        # metric_for_best_model='overall_f1',  # Leads to key error
        push_to_hub=False,
        hub_strategy='every_save',
        hub_model_id=finetuned_model,
        hub_token=HfFolder.get_token()
    )

    # Create Trainer instance
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=tokenized_dataset['train'],
        eval_dataset=tokenized_dataset['validate'],
        compute_metrics=compute_metrics,
    )

    print("Start training...")
    trainer.train()

    print("Start evaluation...")
    trainer.evaluate()

    end_time = time.time() - start_time
    print("Total time: %s hours" % (end_time / 60 / 60))

    print("Save finetuned model to the hub...")
    # Save our tokenizer and create model card
    tokenizer.save_pretrained(finetuned_model)
    trainer.create_model_card()
    # Push the results to the hub
    trainer.push_to_hub()

    print("All done.")
