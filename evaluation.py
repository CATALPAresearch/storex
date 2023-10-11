import os
from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


def evaluate_free_answer(answer):
    return True


def evaluate_answer(qa, answer):
    repo = 'TheBloke/Llama-2-13B-German-Assistant-v4-GPTQ'
    # Compare question-answer with given answer
    input_texts = {'qa_answer': qa['answer'], 'answer': answer}

    model = AutoModelForCausalLM.from_pretrained(repo,
                                                 device_map="cpu",
                                                 trust_remote_code=False)

    tokenizer = AutoTokenizer.from_pretrained(repo, use_fast=True)

    qa_answer = qa['answer']
    prompt_template = f'''### User: Compare {answer} to {qa_answer}. What are the differences?
    ### Assistant:

    '''

    print("\n\n*** Generate:")

    input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
    output = model.generate(inputs=input_ids, temperature=0.7, do_sample=True, top_p=0.95, top_k=40, max_new_tokens=512)
    print(tokenizer.decode(output[0]))

    # Inference can also be done using transformers' pipeline

    print("*** Pipeline:")
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.7,
        top_p=0.95,
        top_k=40,
        repetition_penalty=1.1
    )

    print(pipe(prompt_template)[0]['generated_text'])

    # Similarity search intfloat/multilingual-e5-small
    # Semantic textual similarity
    return True
