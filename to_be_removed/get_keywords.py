import torch
from keybert import KeyBERT
from transformers import BertConfig, BertModel, BertTokenizer


#########################################
def get_keywords(similarity_model, paragraph):
    """Gets the topic TODO: Get the keywords, maybe see preprocessing.extract_keywords"""
    key_model = KeyBERT(similarity_model)
    keyphrases = key_model.extract_keywords(paragraph, keyphrase_ngram_range=(1, 2))  #stop_words='german'
    return keyphrases
#########################################


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
