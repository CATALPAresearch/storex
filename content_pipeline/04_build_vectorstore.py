"""
Step 4: build the FAISS index a course searches for context.

    python content_pipeline/04_build_vectorstore.py --course oop

Embeds the chapter prose - the generated Frage:/Antwort: lines are stripped
first - and writes the index into the course's materials directory. The exam
uses it to find context for generated questions; a course without one simply
asks predefined questions instead.

The embedding model must match what the application uses, otherwise the index
loads without complaint and returns unrelated context. It is therefore recorded
in the manifest and checked by courselib.validate.
"""
import argparse
import os
import sys

from langchain.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

REPOSITORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPOSITORY)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _course import materials_path, source_path  # noqa: E402
from oral_exam.models import EMBEDDING_MODEL  # noqa: E402

def get_doc_from_pdf(directory):
    """
    Reads pdf files and return a list of documents.
    """
    loader = DirectoryLoader(directory, glob='*.pdf', loader_cls=PyPDFLoader)
    return loader.load()


def get_doc_from_txt(directory):
    """
    Reads textfiles and return a list of documents.
    """
    loader = DirectoryLoader(directory, glob='*.txt', loader_cls=TextLoader)
    return loader.load()


def process_doc(documents):
    """
    Removes headlines as well as questions and answers from the page contents of each document.
    """
    for document in documents:
        processed_text = " ".join(document.page_content.split("\n", 2)[2:]).split('\n')
        processed_text = [line for line in processed_text if line and not (line.startswith("Frage:") or
                                                                           line.startswith("Antwort:"))]

        document.page_content = '\n'.join(processed_text)
    return documents


def create_vector_db(documents, target, model_name):
    """
    Creates a FAISS vector database from text documents. First splits the text recursively and then creates embeddings.
    """
    import torch
    device = "cuda" if torch.cuda.is_available() else "cpu"

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150,
                                                   separators=['\n\n', '\n', '.', ',', ' ', ''])
    split_text = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs={'device': device})

    db = FAISS.from_documents(split_text, embeddings)
    os.makedirs(target, exist_ok=True)
    db.save_local(target)
    print(f"{len(split_text)} chunks embedded with {model_name}")
    print(f"Index saved to {target}")


def main():
    parser = argparse.ArgumentParser(description="Build the vector store of a course.")
    parser.add_argument("-c", "--course", required=True, help="Id of the course.")
    parser.add_argument("--chapters", help="Override the chapter directory from the manifest.")
    parser.add_argument("--output", help="Override the target directory.")
    parser.add_argument("--model", default=EMBEDDING_MODEL,
                        help="Embedding model. Must match what the application uses.")
    args = parser.parse_args()

    chapters = source_path(args.course, "chapters", args.chapters)
    target = args.output or materials_path(args.course, "vector_store")
    if not target:
        sys.exit(f"The manifest of '{args.course}' declares no materials.vector_store.path; "
                 "add it, or pass --output.")

    print(f"{chapters} -> {target}")
    # To embed a pdf directly, call get_doc_from_pdf(directory) instead
    documents = get_doc_from_txt(chapters)
    process_doc(documents)
    create_vector_db(documents, target, args.model)

    if args.model != EMBEDDING_MODEL:
        print(f"\nNote: the application embeds with {EMBEDDING_MODEL}. Record {args.model} "
              "under materials.vector_store.embedding_model, or the index will return "
              "unrelated context.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
