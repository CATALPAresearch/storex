"""
Script for training a T5 model for question generation with the pytorch.
"""
import argparse
import copy
import pytorch_lightning
import time
import torch

from datasets import concatenate_datasets, load_dataset
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm
from transformers import AdamW, T5ForConditionalGeneration, T5Tokenizer


# Set model and database paths from the huggingface hub
pretrained_model = "t5-small"
finetuned_model = "LunaticTanuki/oop-de-qg-t5-small"
database = "LunaticTanuki/oop-de-qg"
data_files = {'train': "train.csv", 'validate': "validate.csv"}

# Set arguments
args = argparse.Namespace()
args.num_workers = 0
args.batch_size = 8
args.learning_rate = 3e-5
args.eps = 1e-8
args.weight_decay = 0.0


class QGDataset(Dataset):

    def __init__(self, tokenizer, data, max_len_input=512, max_len_output=128):
        self.tokenizer = tokenizer
        self.data = data.to_pandas()
        self.max_len_input = max_len_input
        self.max_len_output = max_len_output
        self.context_column = 'paragraph'
        self.answer_column = 'answer'
        self.question_column = 'question'
        self.inputs = []
        self.targets = []
        self._load_data()

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, index):
        source_ids = self.inputs[index]['input_ids'].squeeze()
        target_ids = self.targets[index]['input_ids'].squeeze()
        source_mask = self.inputs[index]['attention_mask'].squeeze()
        target_mask = self.targets[index]['attention_mask'].squeeze()
        labels = copy.deepcopy(target_ids)
        labels[labels == 0] = -100
        return {'source_ids': source_ids, 'source_mask': source_mask, 'target_ids': target_ids, 'target_mask': target_mask, 'labels': labels}

    def _load_data(self):
        for idx in tqdm(range(len(self.data))):

            context, answer, target = self.data.loc[idx, self.context_column], self.data.loc[idx, self.answer_column], self.data.loc[idx, self.question_column]
            # if len(str(answer).split()) >= 8:
            #     input_text = '<longanswer> %s <context> %s ' % (answer, context)
            # else:
            #     input_text = '<answer> %s <context> %s ' % (answer, context)
            input_text = '<answer> %s <context> %s ' % (answer, context)
            target = str(target)

            tokenized_inputs = self.tokenizer.batch_encode_plus(
                [input_text],
                max_length=self.max_len_input,
                padding='max_length',
                truncation=True,
                return_tensors='pt'
            )

            tokenized_targets = self.tokenizer.batch_encode_plus(
                [target],
                max_length=self.max_len_output,
                padding='max_length',
                truncation=True,
                return_tensors='pt'
            )

            self.inputs.append(tokenized_inputs)
            self.targets.append(tokenized_targets)


class T5FineTuner(pytorch_lightning.LightningModule):

    def __init__(self, model, tokenizer, args):
        super().__init__()
        self.model = model
        self.tokenizer = tokenizer
        self.args = args

    def forward(self, input_ids, attention_mask, labels=None):
        return self.model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels,  # decoder_input_ids included in lm_labels
        )

    def training_step(self, batch, batch_idx):
        outputs = self.forward(
            input_ids=batch['source_ids'],
            attention_mask=batch['source_mask'],
            # decoder_input_ids=batch['target_ids'],
            # decoder_attention_mask=batch['target_mask'],
            labels=batch['labels']
        )
        loss = outputs.loss
        # logits = outputs.logits
        self.log('train_loss', loss, on_step=True, on_epoch=True, prog_bar=True)
        return loss

    def validation_step(self, batch, batch_idx):
        outputs = self.forward(
            input_ids=batch['source_ids'],
            attention_mask=batch['source_mask'],
            # decoder_input_ids=batch['target_ids'],
            # decoder_attention_mask=batch['target_mask'],
            labels=batch['labels']
        )
        loss = outputs.loss
        # logits = outputs.logits
        self.log('val_loss', loss, on_step=True, on_epoch=True, prog_bar=True)
        return loss

    def train_dataloader(self):
        return DataLoader(train_dataset, batch_size=self.args.batch_size, num_workers=self.args.num_workers)

    def val_dataloader(self):
        return DataLoader(validation_dataset, batch_size=self.args.batch_size, num_workers=self.args.num_workers)

    def configure_optimizers(self):
        # no_decay = ["bias", "LayerNorm.weight"]
        # optimizer_grouped_parameters = [
        #     {
        #         "params": [p for n, p in self.model.named_parameters() if not any(nd in n for nd in no_decay)],
        #         "weight_decay": self.args.weight_decay,
        #     },
        #     {
        #         "params": [p for n, p in self.model.named_parameters() if any(nd in n for nd in no_decay)],
        #         "weight_decay": 0.0,
        #     },
        # ]
        # return AdamW(optimizer_grouped_parameters, lr=self.args.learning_rate, eps=args.eps)
        return AdamW(self.parameters(), lr=self.args.learning_rate, eps=args.eps)


def max_length(column):
    """
    Gets the maximum total sequence length for input or target text after tokenization
    Longer sequences will be truncated and shorter sequences will be padded
    """
    datasets = [dataset['train'], dataset['validate']]
    columns = ['context', 'question_answer']
    # Get the maximum total sequence length after tokenization
    tokenized = concatenate_datasets(datasets).map(
        lambda x: tokenizer(x[column], truncation=True), batched=True, remove_columns=columns)
    maximum = max([len(x) for x in tokenized['input_ids']])
    print(f"Max length of {column}: {maximum}")
    return maximum


if __name__ == "__main__":
    start_time = time.time()
    pytorch_lightning.seed_everything(99)

    print("Loading dataset...")
    dataset = load_dataset(database, data_files=data_files)
    print(f"Train dataset size: {len(dataset['train'])}")
    print(f"Validation dataset size: {len(dataset['validate'])}")

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Loading pre-trained model to {device}...")
    print('Loading pre-trained model...')
    model = T5ForConditionalGeneration.from_pretrained(pretrained_model).to(device)
    tokenizer = T5Tokenizer.from_pretrained(pretrained_model)
    tokenizer.add_special_tokens(
        {'additional_special_tokens': ['<answer>', '<context>']}
    )

    print("Preparing dataset...")
    max_length_input = max_length('context')
    max_length_output = max_length('question_answer')
    train_dataset = QGDataset(tokenizer, dataset['train'], max_length_input, max_length_output)
    validation_dataset = QGDataset(tokenizer, dataset['validate'], max_length_input, max_length_output)

    print('Initializing model...')
    model = T5FineTuner(model, tokenizer, args)
    trainer = pytorch_lightning.Trainer(
        max_epochs=10,
        devices=1,
        accelerator='gpu',
        # gradient_clip_val=1.0,
        # auto_lr_find=True,
        callbacks=[EarlyStopping(monitor="val_loss")]
    )
    print('Run learning rate finder...')
    tuner = pytorch_lightning.pytorch.tuner.Tuner(trainer)  # TODO: With tuner possible?
    lr_finder = tuner.lr_find(model)
    args.learning_rate = lr_finder.suggestion()
    print('Suggested lr: ', lr_finder.suggestion())

    # # Plot with lr
    # import matplotlib
    # matplotlib.use("Agg")
    # fig = lr_finder.plot(suggest=True)
    # fig.savefig('lr.png')mv ~/Dow
    # # fig.show()

    print('Fine tuning...')
    trainer.fit(model)
    # trainer.test()

    end_time = time.time() - start_time
    print('Total time: %s hours' % (end_time / 60 / 60))

    print("Save finetuned model to the hub...")
    # Save tokenizer and create model card
    tokenizer.save_pretrained(finetuned_model)
    trainer.create_model_card()
    # Push the results to the hub
    trainer.push_to_hub()

    # Save model locally
    # if not os.path.exists(finetuned_model):
    #     os.makedirs(finetuned_model)
    # model.model.save_pretrained(finetuned_model)
    # tokenizer.save_pretrained(finetuned_model)

    print('All done.')
