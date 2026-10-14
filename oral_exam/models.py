"""
Process-wide registry for the machine learning models.

A command line exam loaded every model into a fresh process. The web app serves
several exams from one long-lived process, so the models are loaded once and
shared. They are used for inference only and hold no per-exam state, so sharing
them is safe; PyTorch releases the GIL inside its kernels, which lets concurrent
sessions overlap.

Everything is loaded lazily behind a lock. Call warmup() at start-up, otherwise
the first exam request pays the full load time.
"""
import logging
import os
import threading

logger = logging.getLogger(__name__)

# Both the answer evaluation and the question generation context search embed
# German text with this model. It used to be loaded twice.
EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"
CLASSIFIER_MODEL = "symanto/xlm-roberta-base-snli-mnli-anli-xnli"
PARAPHRASE_MODEL = "LunaticTanuki/oop-de-qg-flan-t5-base-v6"

# Reentrant on purpose: building one model may ask for another, for example the
# similarity model and the vector store both reuse the embedding model.
_lock = threading.RLock()
_cache = {}


def _singleton(key, factory):
    """Return the cached object for key, building it under the lock on first use."""
    if key in _cache:
        return _cache[key]
    with _lock:
        # Another thread may have built it while we waited for the lock.
        if key not in _cache:
            logger.info("Loading %s ...", key)
            _cache[key] = factory()
            logger.info("Loaded %s.", key)
    return _cache[key]


def get_embeddings():
    """Langchain embedding wrapper used for the FAISS context search."""
    def build():
        import torch
        from langchain.embeddings import HuggingFaceEmbeddings
        device = "cuda" if torch.cuda.is_available() else "cpu"
        return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL, model_kwargs={"device": device})

    return _singleton("embeddings", build)


def get_similarity_model():
    """
    Sentence transformer for answer similarity.

    This reuses the sentence transformer inside the langchain embedding wrapper
    so the weights are held once instead of twice.
    """
    def build():
        client = getattr(get_embeddings(), "client", None)
        if client is not None:
            return client
        from sentence_transformers import SentenceTransformer
        return SentenceTransformer(EMBEDDING_MODEL)

    return _singleton("similarity_model", build)


def get_congruity_pipeline():
    """Text classification pipeline that detects entailment and contradiction."""
    def build():
        from transformers import pipeline
        return pipeline("text-classification", model=CLASSIFIER_MODEL, truncation=True)

    return _singleton("congruity_pipeline", build)


def get_vectorstore():
    """FAISS index over the teaching material, read-only."""
    def build():
        from langchain.vectorstores import FAISS
        directory = os.path.dirname(__file__)
        return FAISS.load_local(os.path.join(directory, "data/vectorStore"), get_embeddings())

    return _singleton("vectorstore", build)


def get_evaluator():
    """Answer evaluator, see evaluation.Evaluator."""
    def build():
        from evaluation import Evaluator
        return Evaluator()

    return _singleton("evaluator", build)


def get_speech_recognition():
    """Whisper based transcription, see audio.speech_recognition.SpeechRecognition."""
    def build():
        from audio.speech_recognition import SpeechRecognition
        return SpeechRecognition()

    return _singleton("speech_recognition", build)


def get_paraphraser_pipeline():
    """The fine-tuned question generation model from the paper, run locally."""
    def build():
        from transformers import pipeline
        return pipeline("text2text-generation", model=PARAPHRASE_MODEL)

    return _singleton("paraphraser", build)


def warmup(speech=True, paraphrase=True):
    """
    Load the models needed to run an exam.

    :param speech: also load transcription, needed by the web app and the CLI.
    :param paraphrase: also load the local paraphrasing model, see PARAPHRASE_ENGINE.
    """
    get_embeddings()
    get_similarity_model()
    get_congruity_pipeline()
    get_vectorstore()
    get_evaluator()
    if speech:
        get_speech_recognition()
    if paraphrase and os.getenv("PARAPHRASE_ENGINE", "local").lower() == "local":
        get_paraphraser_pipeline()
    logger.info("Model warmup complete.")
