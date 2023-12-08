"""
File for answer evaluation.
"""
import re
import torch

from keybert import KeyBERT
from sentence_transformers import SentenceTransformer, util
from transformers import BertConfig, BertModel, BertTokenizer, pipeline
from utils.helpers import FeedbackType

import logging
logger = logging.getLogger()

# os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


def preprocess_text(text):  # TODO: Use preprocessing.preprocess_text()
    """
    Preprocesses text by removing non-alphanumeric characters, extra whitespaces, german umlauts and stopwords and
    making all words lowercase.

    :param text: Unprocessed text.
    :return text: Preprocessed text.
    """
    # Remove non-alphanumeric characters (except for whitespaces)
    text = re.sub(r'[^ \w+]', '', text)
    # Make all words lower case and strip extra whitespaces
    text = text.lower().strip()
    # Replace german umlauts
    umlauts = {ord('ä'): 'ae', ord('ü'): 'ue', ord('ö'): 'oe', ord('ß'): 'ss'}
    text = text.translate(umlauts)

    # TODO: Do I need stopword removal, Stemming, Lemmatization?

    return text


class Evaluator:
    """
    Class which evaluates given answers by finding contradictions, checking the similarity, and finding missing topics.
    """
    def __init__(self):
        """
        Initializes the similarity and classifier models used for answer evaluation.
        """
        # Load a sentence similarity model
        self.similarity_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")  # 'LLukas22/all-MiniLM-L12-v2-embedding-all'

        # Load a classifier model, try morit/xlm-t-roberta-base-mnli-xnli?
        classifier_model = "symanto/xlm-roberta-base-snli-mnli-anli-xnli"
        self.congruity_pipeline = pipeline("text-classification", model=classifier_model)
        self.accuracy_pipeline = pipeline("zero-shot-classification", model=classifier_model)

    def evaluate_keywords(self, keywords, student_answer):
        """
        Checks if the students answer contains the given keywords and returns the accuracy of the missing topics.

        :param keywords: Main keywords from the correct answer.
        :param student_answer: Answer given by the student.
        :return missing_topics:
        """
        processed_answer = preprocess_text(student_answer)
        missing_keys = []
        missing_topics = []

        # Check if keywords are directly mentioned in the students answer by searching in the preprocessed answer for
        # the preprocessed keywords
        for word in keywords:
            processed_word = preprocess_text(word)
            if not re.search(rf"{processed_word}", processed_answer):
                missing_keys.append(word)
            else:
                logger.info(f"Keyword '{word}' found!")

        # Check if keywords are indirectly mentioned in the students answer by checking the accuracy with which the
        # students answer hits the topics represented by the keywords
        if missing_keys:
            logger.info(f"Non-mentioned keywords: {missing_keys}")
            accuracy = self.check_accuracy(missing_keys, student_answer)
            # Add missing topics starting from a threshold of accuracy
            for topic in accuracy:
                if topic[1] < 0.2:  # TODO: What is a good threshold for accuracy?
                    missing_topics.append(topic[0])

        logger.info(f"Missing topics: {missing_topics}")
        return missing_topics

    def evaluate_answer(self, correct_answer, student_answer):
        """
        Compares the students answer with the correct answer.

        :param correct_answer: Question-answer pair.
        :param student_answer: Answer given by the student.
        :return feedback:
        """
        feedback = None
        # Check for silence, which is turned into a short sentence by speech recognition LLMs (TODO: Move to ASR)
        if len(student_answer) < 20:  # TODO: Understand sentences like "Ich weiß es nicht." oder "Sinnfreie Frage."
            feedback = FeedbackType.SILENCE
            return feedback

        # Check the congruity of the answer via text classification (MNLI)
        congruity = self.check_congruity(correct_answer, student_answer)
        if congruity[0]['label'] != 'ENTAILMENT':
            # Set OFF_TOPIC for neutral entailment
            if congruity[0]['label'] == 'NEUTRAL':
                feedback = FeedbackType.OFF_TOPIC
            # Set CONTRADICTS for contradicting entailment
            if congruity[0]['label'] == 'CONTRADICTION':
                feedback = FeedbackType.CONTRADICTS
            return feedback

        # Check the similarity with similarity search LLM
        similarity = self.check_similarity(correct_answer, student_answer)
        if similarity > 0.75:  # TODO: What similarity is similar??
            feedback = FeedbackType.CORRECT
        else:
            feedback = FeedbackType.MISSING_TOPIC
        return feedback

        # Identify the mistakes (factual inaccuracy, missing information, structural issues)

    def check_similarity(self, correct_answer, student_answer):
        """
        Finds the semantic similarity between two paragraphs.

        :param correct_answer: Correct answer.
        :param student_answer: Answer given by the student.
        :return: Similarity between both answers.
        """
        # Compute embeddings for both answers
        c_embedding = self.similarity_model.encode(correct_answer, convert_to_tensor=True)
        s_embedding = self.similarity_model.encode(student_answer, convert_to_tensor=True)
        # Calculate similarity
        similarity = util.pytorch_cos_sim(c_embedding, s_embedding)
        logger.info(f"Similarity: {similarity}")
        return similarity

    def check_congruity(self, correct_answer, student_answer):
        """
        Checks if the concatenated answers contain a contradiction or entail each other.

        :param correct_answer: Correct answer.
        :param student_answer: Answer given by the student.
        :return: Congruity
        """
        # Check entailment in concatenated answers
        congruity = self.congruity_pipeline(correct_answer + student_answer)
        logger.info(f"Congruity: {congruity}")
        return congruity

        # Check probs
        # model = AutoModelForSequenceClassification.from_pretrained("symanto/xlm-roberta-base-snli-mnli-anli-xnli")
        # tokenizer = AutoTokenizer.from_pretrained("symanto/xlm-roberta-base-snli-mnli-anli-xnli")
        # inputs = tokenizer([correct_answer, student_answer], return_tensors="pt", padding=True)  # truncate=True?
        # logits = model(**inputs).logits
        # probs = torch.softmax(logits, dim=1)
        # probs = probs[..., [0]].tolist()
        # logger.info(f"Probs: {probs}")

    def check_accuracy(self, keys, student_answer):
        """
        Checks if the missing keywords are accurately represented in the students answer.

        :param keys: Keywords from the correct answer which are not mentioned in the students answer directly.
        :param student_answer: Answer given by the student.
        :return accuracy:
        """
        # Check the accuracy of the keys for the student answer
        accuracy_scores = self.accuracy_pipeline(student_answer, keys)
        accuracy = list(zip(accuracy_scores.get('labels'), accuracy_scores.get('scores')))
        logger.info(f"Accuracy per keyword: {accuracy}")

        return accuracy

    def get_keywords(self, paragraph):
        """Gets the topic TODO: Get the keywords, maybe see preprocessing.extract_keywords"""
        key_model = KeyBERT(self.similarity_model)
        keyphrases = key_model.extract_keywords(paragraph, keyphrase_ngram_range=(1, 2))  #stop_words='german'
        return keyphrases


def get_key_phrases(paragraph):
    """
    Get the attention of each word in a paragraph.
    """
    # Load a pre-trained BERT model and tokenizer with multi-head attention layer
    model_name = 'dbmdz/bert-base-german-uncased'  # 'bert-base-multilingual-uncased'

    config = BertConfig.from_pretrained(model_name, output_hidden_states=True, output_attentions=True)
    model = BertModel.from_pretrained(model_name, config=config)
    tokenizer = BertTokenizer.from_pretrained(model_name, language="german")
    # model = BertForMaskedLM.from_pretrained(model_name)

    # Tokenize the correct answer text
    tokens = tokenizer.tokenize(paragraph)  # (tokenizer.cls_token + answer_paragraph + tokenizer.sep_token)
    input_ids = tokenizer.convert_tokens_to_ids(tokens)

    # indexed_tokens = tokenizer.encode(tokens, return_tensors='pt')

    # Convert input to tensor
    input_tensor = torch.tensor(input_ids).unsqueeze(0)  # Add batch dimension

    # Perform forward pass to get the attention weights
    with torch.no_grad():
        outputs = model(input_tensor, output_attentions=True)
############################################
    # Extract the attention weights
    attention_weights = outputs.attentions

    # Print the attention weights for the first layer of the model
    layer = 0  # Choose the layer you want to analyze
    attention_layer = attention_weights[layer][0]  # [0] since we have a single input

    # Find words with the highest attention scores
    top_k = 5
    top_indices = attention_layer.mean(dim=0).argsort(descending=True)[:top_k]

    for k in top_indices:
        top_words = [tokens[i] for i in k]

    print(f"Top attended words in the input: {top_words}")

############################################
    # Extract the attention weights for all heads in a multi-head attention layer
    attention_weights = (torch.stack(outputs.attentions, dim=0))

    # Average attention scores across all heads
    average_attention = attention_weights.mean(dim=0)

    # Calculate mean attention scores for each word
    mean_attention_scores = average_attention.mean(dim=0)

    # Get the indices of words with the highest mean attention scores
    top_k = 5
    top_indices = mean_attention_scores.argsort(descending=True)[:top_k]

    # Find the top-k words with the highest mean attention scores
    top_words = [tokens[i] for i in top_indices]
    print(f"Top {top_k} attended words in the input: {top_words}")
