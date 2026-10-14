"""
Client for the KI:connect text generation backend.

KI:connect exposes an OpenAI-compatible API, so a chat completion is a plain
POST to ``{BASE_URL}/chat/completions`` with a bearer token. This replaces the
former langchain/HuggingFaceHub path: the legacy inference host
``api-inference.huggingface.co`` has been shut down and no longer resolves.

Configuration comes from the environment (see example.env):
    BASE_URL    e.g. https://chat.kiconnect.nrw/api/v1
    API_KEY     bearer token
    MODEL       e.g. Mistral-small-4-119b-2603
    DISABLE_LLM set to 'true' to answer from a canned string (UI development)
"""
import logging
import os
import time

import requests

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

BASE_URL = os.getenv("BASE_URL", "").rstrip("/")
API_KEY = os.getenv("API_KEY", "")
MODEL = os.getenv("MODEL", "")
LLM_TIMEOUT = int(os.getenv("LLM_TIMEOUT", "120"))
LLM_RETRIES = int(os.getenv("LLM_RETRIES", "3"))

# Resolved once per process, see _resolve_model().
_model_cache = None


class LLMError(RuntimeError):
    """Raised when the text generation backend cannot be reached or returns nothing."""


def is_disabled():
    """True if LLM calls are stubbed out via DISABLE_LLM (development guard)."""
    return os.getenv("DISABLE_LLM", "false").lower() == "true"


def _headers():
    return {"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}


def _extract_content(data):
    """Pull the assistant text out of an OpenAI-compatible chat completion."""
    try:
        message = data.get("choices", [{}])[0].get("message", {})
        content = message.get("content", "")
        if isinstance(content, str):
            return content
        # Some providers answer with structured content blocks instead of a string.
        if isinstance(content, list):
            parts = []
            for block in content:
                if isinstance(block, dict):
                    if isinstance(block.get("text"), str):
                        parts.append(block["text"])
                    elif block.get("type") == "text" and isinstance(block.get("content"), str):
                        parts.append(block["content"])
            return "\n".join(part for part in parts if part)
    except (AttributeError, IndexError, TypeError) as error:
        logger.warning("Could not parse the response content: %s", error)
    return ""


def _resolve_model():
    """
    Return a usable chat model id.

    If MODEL is not offered by the endpoint, fall back to the first
    non-embedding model it lists. The decision is cached for the process.
    """
    global _model_cache
    if _model_cache:
        return _model_cache

    try:
        response = requests.get(f"{BASE_URL}/models", headers=_headers(), timeout=30)
        response.raise_for_status()
        ids = [model.get("id") for model in response.json().get("data", []) if model.get("id")]
    except (requests.RequestException, ValueError) as error:
        logger.warning("Could not list models (%s). Using the configured model '%s'.", error, MODEL)
        _model_cache = MODEL
        return MODEL

    if not ids or (MODEL in ids and "embedding" not in MODEL.lower()):
        _model_cache = MODEL
        return MODEL

    for model_id in ids:
        if "embedding" not in model_id.lower():
            logger.warning("Model '%s' is not available. Falling back to '%s'.", MODEL, model_id)
            _model_cache = model_id
            return model_id

    _model_cache = ids[0]
    return ids[0]


def chat(instruction, user_prompt=None, temperature=0.0, max_tokens=512, timeout=None):
    """
    Send an instruction to the text generation backend and return its answer.

    The instruction is sent with the 'user' role rather than 'system': like the
    sibling SRL chat project, this backend does not reliably act on a
    standalone system message.

    :raises LLMError: if the backend is unreachable or answers with empty text.
    """
    if is_disabled():
        logger.warning("DISABLE_LLM=true - returning a canned answer")
        return "Dies ist eine Platzhalterantwort, da die Textgenerierung deaktiviert ist."

    if not BASE_URL:
        raise LLMError("BASE_URL is not configured. Copy example.env to .env and fill it in.")

    messages = [{"role": "user", "content": instruction}]
    if user_prompt:
        messages.append({"role": "user", "content": user_prompt})

    payload = {
        "model": _resolve_model(),
        "messages": messages,
        "stream": False,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    logger.debug("Instruction: %s", instruction)
    delay = 1.0
    last_error = "no attempt was made"

    for attempt in range(1, LLM_RETRIES + 1):
        try:
            response = requests.post(f"{BASE_URL}/chat/completions",
                                     json=payload,
                                     headers=_headers(),
                                     timeout=timeout or LLM_TIMEOUT)
            response.raise_for_status()
            content = _extract_content(response.json()).strip()
            if content:
                logger.debug("Answer: %s", content)
                return content
            last_error = "the backend returned empty content"
        except (requests.RequestException, ValueError) as error:
            last_error = str(error)

        logger.warning("Text generation attempt %s/%s failed: %s", attempt, LLM_RETRIES, last_error)
        if attempt < LLM_RETRIES:
            time.sleep(delay)
            delay *= 2
            # Nudge the sampler, a deterministic request tends to fail the same way twice.
            payload["temperature"] = min(payload["temperature"] + 0.1, 1.0)

    raise LLMError(f"Text generation failed after {LLM_RETRIES} attempts: {last_error}")
