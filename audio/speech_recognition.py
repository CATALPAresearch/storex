"""
Class to transcribe spoken answers into text.

Audio either comes from a local microphone (command line exam, see
audio.microphone) or as an uploaded recording from the browser (web app). Both
are transcribed by the same Whisper pipeline.
"""
import logging
import os
import tempfile

import numpy

from transformers import WhisperProcessor, WhisperTokenizer, pipeline
from transformers.pipelines.audio_utils import ffmpeg_read

logger = logging.getLogger(__name__)

MODEL_NAME = "openai/whisper-base"  # Or: "openai/whisper-medium"
SAMPLING_RATE = 16000

# Whisper does not answer silence with nothing, it invents a sentence, and that
# sentence is not predictable. So silence is detected in the audio instead, and
# the recording is not even transcribed. The threshold is the one the local
# microphone uses (MIN_VOLUME of 100 on 16 bit samples), see audio/microphone.py.
SILENCE_RMS = 100 / 32768

# Second line of defence: a few stock phrases Whisper is known to produce for
# noise that is just above the threshold.
SILENCE_ARTEFACTS = {
    "vielen dank.",
    "vielen dank",
    "danke.",
    "untertitelung des zdf, 2020",
    "untertitel im auftrag des zdf, 2017",
    "untertitel von stephanie geiges",
    "copyright wdr 2021",
    "das war's.",
}
MIN_TRANSCRIPT_LENGTH = 3


def is_silence(transcription):
    """True if a transcription holds no usable answer."""
    if not transcription:
        return True
    text = transcription.strip()
    return len(text) < MIN_TRANSCRIPT_LENGTH or text.lower() in SILENCE_ARTEFACTS


def volume(samples):
    """Root-mean-square level of decoded audio in [-1, 1]."""
    if samples is None or len(samples) == 0:
        return 0.0
    return float(numpy.sqrt(numpy.mean(numpy.square(samples))))


class SpeechRecognition:
    def __init__(self):
        """
        Initializes forced decoder ids and the pipeline for automatic speech recognition.
        """
        device = 'cpu'  # Loading to cpu, due to torch.cuda.OutOfMemoryErrors

        # Load processor and tokenizer
        processor = WhisperProcessor.from_pretrained(MODEL_NAME)
        tokenizer = WhisperTokenizer.from_pretrained(MODEL_NAME, language="german")

        self.forced_decoder_ids = processor.get_decoder_prompt_ids(language="german", task="transcribe")

        # Create pipeline for Long-Form Transcription
        self.pipeline = pipeline('automatic-speech-recognition',
                                 model=MODEL_NAME,
                                 tokenizer=tokenizer,
                                 chunk_length_s=30,
                                 device=device)

    def transcribe(self, audio, mime_type=None):
        """
        Transcribes a recording into text.

        :param audio: raw bytes of an audio file, as uploaded by the browser, or
                      a path to an audio file.
        :param mime_type: content type reported by the browser, for logging only.
        :return: the transcription, or None if the recording holds only silence.
        """
        if isinstance(audio, (bytes, bytearray)):
            logger.info("Transcribing %s bytes of uploaded audio (%s)", len(audio), mime_type or "unknown type")
            # ffmpeg handles the webm/opus of Chrome as well as the mp4 of Safari
            audio = ffmpeg_read(bytes(audio), SAMPLING_RATE)
            level = volume(audio)
            if level < SILENCE_RMS:
                logger.info("Recording discarded as silence, level %.5f", level)
                return None

        transcription = self.pipeline(
            audio,
            generate_kwargs={"forced_decoder_ids": self.forced_decoder_ids})["text"]

        if is_silence(transcription):
            logger.info("Transcription discarded as silence: %r", transcription)
            return None
        return transcription.strip()

    def get_audio_to_text(self):
        """
        Records from the local microphone and transcribes it into text.
        Returns the transcribed recording, or None if only silence was recorded.
        """
        # Imported here so that the web app never needs PortAudio
        from audio import microphone

        audio_frames, sample_size, silence = microphone.record_speech()
        if silence:
            return None

        # Save the recording to a temporary file for the pipeline to read
        handle, output_file = tempfile.mkstemp(prefix="oral-exam-", suffix=".wav")
        os.close(handle)
        try:
            microphone.save_recording(audio_frames, sample_size, output_file)
            return self.transcribe(output_file)
        finally:
            os.unlink(output_file)
