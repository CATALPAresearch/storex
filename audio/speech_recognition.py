"""
Class to transcribe audio recorded from a microphone.

Speech is recorded from the microphone until disrupted by KeyboardInterrupt or long period of silence.
The audio is then transcribed into predicted text and returned.
"""
import pyaudio
import threading
import wave

from array import array
from queue import Queue, Full
from transformers import WhisperProcessor, WhisperTokenizer, pipeline
from utils import colours

import logging
logger = logging.getLogger()
# TODO: Check for silence and stopp the recording.
# TODO: If only silence, stop after a few seconds and return a message.
# TODO: Training with specific materials?
# TODO: Remove 'ehm', 'öhm', 'bla'

# TODO Remove:
#  ALSA lib pcm_dsnoop.c:601:(snd_pcm_dsnoop_open) unable to open slave
#  ALSA lib pcm_dmix.c:1032:(snd_pcm_dmix_open) unable to open slave
#  ALSA lib pcm_oss.c:397:(_snd_pcm_oss_open) Cannot open device /dev/dsp
#  ALSA lib confmisc.c:160:(snd_config_get_card) Invalid field card
#  ALSA lib pcm_usb_stream.c:482:(_snd_pcm_usb_stream_open) Invalid card 'card'

# Microphone stream configurations
CHUNK_SIZE = 1024  # Number of frames that signals are split into
FORMAT = pyaudio.paInt16  # Sound is stored in a signed 16-bit binary string
CHANNELS = 1  # Samples per frame
RATE = 16000  # Or: 44100? Sampling rate (frames per second)
MIN_VOLUME = 500  # Threshold intensity that defines silence and noise signal
SILENCE_LIMIT = 2  # Max amount of seconds where only silence is recorded
BUF_MAX_SIZE = CHUNK_SIZE * 10  # If the recording thread can't consume fast enough, the listener will start discarding


def speech_check():
    """
    Checks for speech. TODO: WIP
    """
    stopped = threading.Event()
    q = Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK_SIZE)))

    listen_t = threading.Thread(target=listen, args=(stopped, q))
    listen_t.start()
    record_t = threading.Thread(target=record, args=(stopped, q))
    record_t.start()

    try:
        while True:
            listen_t.join(0.1)
            record_t.join(0.1)
    except KeyboardInterrupt:
        stopped.set()

    listen_t.join()
    record_t.join()


def record(stopped, q):
    """
    Prints 'O' while speaking and '-' while silence. TODO: WIP
    """
    while True:
        if stopped.wait(timeout=0):
            break
        chunk = q.get()
        vol = max(chunk)
        if vol >= MIN_VOLUME:
            # TODO: write to file
            print("O")
        else:
            print("-")


def listen(stopped, q):
    """
    Listens to microphone input. TODO: WIP
    """
    stream = pyaudio.PyAudio().open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK_SIZE,
    )

    while True:
        if stopped.wait(timeout=0):
            break
        try:
            q.put(array('h', stream.read(CHUNK_SIZE)))
        except Full:
            pass  # discard


def record_speech():
    """
    Records audio from microphone input.
    Returns the audio frames and used sampling size.
    """
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK_SIZE)

    colours.print_red("*** Recording started ***")

    frames = []

    try:
        while True:
            data = stream.read(CHUNK_SIZE)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    colours.print_red("*** Recording ended ***")

    stream.stop_stream()
    stream.close()
    p.terminate()

    sample_size = p.get_sample_size(FORMAT)
    return frames, sample_size


def save_recording(frames, sampling_width, output_file):
    """
    Saves given audio frames to a given file using the specified sampling size.
    """
    audio_file = wave.open(output_file, 'wb')
    audio_file.setnchannels(CHANNELS)
    audio_file.setsampwidth(sampling_width)
    audio_file.setframerate(RATE)
    audio_file.writeframes(b''.join(frames))
    audio_file.close()


class SpeechRecognition:
    def __init__(self):
        """
        Initializes forced decoder ids and the pipeline for automatic speech recognition.
        """
        device = 'cpu'  # Loading to cpu, due to torch.cuda.OutOfMemoryErrors

        # Load processor and tokenizer
        model_name = "openai/whisper-medium"
        processor = WhisperProcessor.from_pretrained(model_name)
        tokenizer = WhisperTokenizer.from_pretrained(model_name, language="german")

        self.forced_decoder_ids = processor.get_decoder_prompt_ids(language="german", task="transcribe")

        # Create pipeline for Long-Form Transcription
        self.pipeline = pipeline('automatic-speech-recognition',
                                 model=model_name,
                                 tokenizer=tokenizer,
                                 chunk_length_s=30,
                                 device=device)

    def get_audio_to_text(self):
        """
        Records and transcribe audio into text.
        Returns the transcribed recording.
        """
        # Record the microphone input
        audio_frames, sample_size = record_speech()

        # Save the recording to a temporary directory
        output_file = "/tmp/output.wav"
        save_recording(audio_frames, sample_size, output_file)

        # Transcribe the recording
        transcription = self.pipeline(output_file,
                                      batch_size=8,
                                      generate_kwargs={"forced_decoder_ids": self.forced_decoder_ids})["text"]

        return transcription
