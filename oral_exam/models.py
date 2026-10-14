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
# The question generation model used for hints is course specific and is named
# in the course manifest, see courselib.

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


def get_embeddings(model_name=EMBEDDING_MODEL):
    """Langchain embedding wrapper used for the FAISS context search."""
    def build():
        import torch
        from langchain.embeddings import HuggingFaceEmbeddings
        device = "cuda" if torch.cuda.is_available() else "cpu"
        return HuggingFaceEmbeddings(model_name=model_name, model_kwargs={"device": device})

    return _singleton(f"embeddings:{model_name}", build)


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


def get_vectorstore(course):
    """
    FAISS index over the teaching material of one course, read-only.

    Returns None when the course declares no vector store or the index cannot
    be read. None is cached like any other value, so a course without one does
    not retry on every generated question; the exam falls back to predefined
    questions.
    """
    def build():
        path = course.materials.vector_store_path
        if not path:
            logger.info("Course %s has no vector store; questions are not generated from "
                        "the teaching material.", course.id)
            return None
        from langchain.vectorstores import FAISS
        try:
            return FAISS.load_local(path, get_embeddings(course.materials.embedding_model
                                                         or EMBEDDING_MODEL))
        except Exception as error:  # noqa: BLE001 - a broken index must not end the exam
            logger.error("Course %s: the vector store cannot be read (%s).", course.id, error)
            return None

    return _singleton(f"vectorstore:{course.id}", build)


def get_evaluator():
    """Answer evaluator, see evaluation.Evaluator."""
    def build():
        from oral_exam.evaluation import Evaluator
        return Evaluator()

    return _singleton("evaluator", build)


def get_speech_recognition():
    """Whisper based transcription, see audio.speech_recognition.SpeechRecognition."""
    def build():
        from oral_exam.audio.transcription import SpeechRecognition
        return SpeechRecognition()

    return _singleton("speech_recognition", build)


def get_paraphraser_pipeline(model_name):
    """A fine-tuned question generation model, run locally to phrase hints."""
    def build():
        from transformers import pipeline
        return pipeline("text2text-generation", model=model_name)

    return _singleton(f"paraphraser:{model_name}", build)


def warmup(speech=True, paraphrase=True, course_list=None):
    """
    Load the models needed to run an exam.

    The shared models are loaded first, then whatever each course brings. A
    course whose material cannot be loaded is logged and skipped: one broken
    course must not keep the others from being examined.

    :param speech: also load transcription, needed by the web app and the CLI.
    :param paraphrase: also load the local paraphrasing models, see PARAPHRASE_ENGINE.
    """
    get_embeddings()
    get_similarity_model()
    get_congruity_pipeline()
    get_evaluator()
    if speech:
        get_speech_recognition()

    # Imported here, not at module level, to keep models free of a course import
    import courselib

    local_hints = os.getenv("PARAPHRASE_ENGINE", "local").lower() == "local"
    for course in (courselib.all_courses() if course_list is None else course_list):
        get_vectorstore(course)
        if paraphrase and local_hints and course.materials.paraphrase_model:
            try:
                get_paraphraser_pipeline(course.materials.paraphrase_model)
            except Exception as error:  # noqa: BLE001 - hints fall back to the backend
                logger.error("Course %s: the paraphrase model %s is unavailable (%s); "
                             "hints will come from the text generation backend.",
                             course.id, course.materials.paraphrase_model, error)
    logger.info("Model warmup complete.")
