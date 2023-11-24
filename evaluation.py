"""
File for answer evaluation.
"""
import torch

from sentence_transformers import SentenceTransformer, util
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline, BertForMaskedLM, BertTokenizer, \
    BertConfig, BertModel
from utils.helpers import FeedbackType

import logging
logger = logging.getLogger()

# os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


class Evaluator:
    def __init__(self):
        # Load a sentence similarity model, try: "paraphrase-multilingual-MiniLM-L12-v2"
        self.similarity_model = SentenceTransformer('LLukas22/all-MiniLM-L12-v2-embedding-all')

        # Load a classifier model, try morit/xlm-t-roberta-base-mnli-xnli?
        classifier_model = "symanto/xlm-roberta-base-snli-mnli-anli-xnli"
        self.congruity_pipeline = pipeline("text-classification", model=classifier_model)
        self.accuracy_pipeline = pipeline("zero-shot-classification", model=classifier_model)

    def evaluate_predefined_question(self, question_keyword, student_answer):
        keywords = question_keyword['keywords']
        missing_keys = []
        for word in keywords:
            if word not in student_answer:
                missing_keys.append(word)

        if missing_keys:
            print(missing_keys)
            logger.info("Non-mentioned keywords: " + str(missing_keys))
            accuracy = self.check_accuracy(missing_keys, student_answer)

    def evaluate_answer(self, correct_answer, student_answer):
        """
        Compare the students answer with the correct answer.

        :param correct_answer: Question-answer pair.
        :param student_answer: Answer given by the student.
        :return feedback:
        """
        feedback = None
        # Silence is turned into a short sentence by speech recognition LLMs
        if len(student_answer) < 30:  # TODO: What is the minimum amount of words counting as an answer?
            feedback = FeedbackType.SILENCE
            return feedback

        # Text classification with MNLI to check the congruity of the answer
        congruity = self.check_congruity(correct_answer, student_answer)
        if congruity[0]['label'] != 'ENTAILMENT':
            # OFF_TOPIC for neutral entailment
            if congruity[0]['label'] == 'NEUTRAL':
                feedback = FeedbackType.OFF_TOPIC
            # CONTRADICTS for contradicting entailment
            if congruity[0]['label'] == 'CONTRADICTION':
                feedback = FeedbackType.CONTRADICTS
            return feedback

        # Similarity with similarity search LLM
        similarity = self.check_similarity(correct_answer, student_answer)
        if similarity > 0.75:  # TODO: What similarity is similar??
            feedback = FeedbackType.CORRECT
        else:
            feedback = FeedbackType.MISSING_TOPIC
        return feedback

        # TODO: Topic extraction and comparison or LDA
        # Load a text-generation model on the hub
        # llm = HuggingFaceHub(repo_id='google/flan-t5-large',
        #                      model_kwargs={'temperature': 0,
        #                                    'max_length': 1024})
        # # TODO: Antworten aufbereiten, damit sie vergleichbar sind, z.B. keywords suchen? Summary?
        # template = """Compare the following texts:
        # "{c_answer}"
        # and
        # "{s_answer}"
        # Here are the differences:"""
        # # prompt_template = PromptTemplate.from_template(template)
        # # prompt = prompt_template.format(c_answer=correct_answer, s_answer=student_answer)
        # prompt = PromptTemplate(template=template, input_variables=['c_answer', 's_answer'])
        # llm_chain = LLMChain(prompt=prompt, llm=llm)
        # differences = llm_chain.run({'c_answer': correct_answer, 's_answer': student_answer})

        # Identify the mistakes (factual inaccuracy, missing information, structural issues) out off the differences

    def check_similarity(self, correct_answer, student_answer):
        """
        Find the semantic similarity between two paragraphs.

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
        Check if the concatenated answers contain a contradiction or entail each other.

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
        # print("probs", probs)

    def check_accuracy(self, keys, student_answer):
        """
        Check if the keywords are accurately represented in the students answer.

        :param keys:
        :param student_answer:
        :return: Congruity
        """
        # Check accuracy
        accuracy = self.accuracy_pipeline(student_answer, keys)
        logger.info(f"Accuracy: {accuracy}")
        return accuracy

    def get_keys(self, paragraph):
        from keybert import KeyBERT

        sentence_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
        key_model = KeyBERT(sentence_model)
        keyphrases = key_model.extract_keywords(paragraph, keyphrase_ngram_range=(1, 2))  #stop_words='german'
        print(keyphrases)

    def get_missing_keys(self, correct_answer, student_answer):
        self.get_keys(student_answer)
        self.get_keys(correct_answer)
        # TODO: Compare


def get_key_phrases(paragraph):
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


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger.disabled = False

    # Sample student answer and correct answer
    # paragraph = """Klassen sind die Module der objektorientierten Programmierung. Die Menge der Module und damit das Programm werden durch die Vererbungshierarchie weiter strukturiert. Parallel dazu (und weitgehend, bis auf die Vererbung von Beziehungen unabhängig) gibt es noch eine Struktur, die durch das Bestehen von Beziehungen zwischen Klassen (genauer: das Bestehen der Möglichkeit von Beziehungen zwischen Objekten der Klassen; s. Kapitel 2 in Kurseinheit 1) geprägt ist. Diese ist jedoch nicht hierarchisch und insgesamt eher unorganisiert, weshalb sie sich nicht zur systematischen Programmorganisation eignet. Außerdem besteht ein gewisser Konflikt zwischen der Hierarchie der Subklassenbeziehung und den Beziehungen zwischen Objekten: Wenn man einen Teilbaum der Vererbungshierarchie herauslöst, trennt man damit praktisch immer Beziehungen zwischen Mitgliedern des Teilbaums und anderen. Die Klassenhierarchie stellt also insbesondere keine Form der hierarchischen Modularisierung dar."""

    # Sample student answer and correct answer
    student = ("Das Problem der schlechten Tracebarkeit entsteht durch den dynamischen Programmablauf. Das"
               "Lokalitätsprinzip wird gebrochen und dies für zur Unübersichtlichkeit.")
    correct = ("Das Problem der schlechten Tracebarkeit entsteht durch den dynamischen Programmablauf. Die"
               "Goto-Anweisung erlaubt Sprünge von beliebigen Stellen eines Programms zu anderen Stellen und bricht"
               "dabei das Lokalitätsprinzip von Programmen, bei dem zusammengehörende Anweisungen im Programmtext nahe"
               "beieinander stehen. Dies führte zu einer Unübersichtlichkeit im Programmtext und erschwerte das"
               "Verstehen und Debuggen von Programmen.")

    evaluator = Evaluator()
    evaluator.evaluate_answer(correct, student)
    # get_key_phrases(correct)
