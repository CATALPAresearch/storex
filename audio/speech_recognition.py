"""
Functions to transcribe audio recorded from a microphone.

Speech is recorded from the microphone until disrupted by KeyboardInterrupt or long period of silence.
The audio is then transcribed into predicted text and returned.
"""
import torch
import pyaudio
import wave
import threading
from utils import colours
from transformers import WhisperProcessor, WhisperTokenizer, pipeline
from array import array
from queue import Queue, Full


# Todo: Check for silence and stopp the recording.

# TODO Remove:
#  ALSA lib pcm_dsnoop.c:601:(snd_pcm_dsnoop_open) unable to open slave
#  ALSA lib pcm_dmix.c:1032:(snd_pcm_dmix_open) unable to open slave
#  ALSA lib pcm_oss.c:397:(_snd_pcm_oss_open) Cannot open device /dev/dsp
#  ALSA lib confmisc.c:160:(snd_config_get_card) Invalid field card
#  ALSA lib pcm_usb_stream.c:482:(_snd_pcm_usb_stream_open) Invalid card 'card'

# Microphone stream configurations
CHUNK_SIZE = 1024               # Number of frames that signals are split into
FORMAT = pyaudio.paInt16        # Sound is stored in a signed 16-bit binary string
CHANNELS = 1                    # Samples per frame
RATE = 16000                    # Or: 44100? Sampling rate (frames per second)
MIN_VOLUME = 500                # Threshold intensity that defines silence and noise signal
SILENCE_LIMIT = 2               # Max amount of seconds where only silence is recorded
BUF_MAX_SIZE = CHUNK_SIZE * 10  # If the recording thread can't consume fast enough, the listener will start discarding


def main_check():
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

    :return frames: Array of bytes representing audio.
    :return sample_size: Size of each sample.
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
    Save audio frames to a file.

    :param frames: Array of bytes representing audio.
    :param sampling_width: Size of each sample.
    :param output_file: Path to output file.
    """
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(sampling_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def get_text(audio_path):
    """
    Transcribe audio into text.

    :param audio_path: Path to audio file.
    :return prediction: Prediction of transcribed audio file.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Load processor and tokenizer
    model = "openai/whisper-base"
    processor = WhisperProcessor.from_pretrained(model)

    tokenizer = WhisperTokenizer.from_pretrained(model, language="german")
    forced_decoder_ids = processor.get_decoder_prompt_ids(language="german", task="transcribe")

    # Create pipeline for Long-Form Transcription
    whisper_pipeline = pipeline('automatic-speech-recognition',
                                model=model,
                                tokenizer=tokenizer,
                                chunk_length_s=30,
                                device=device)

    prediction = whisper_pipeline(audio_path,
                                  batch_size=8,
                                  generate_kwargs={"forced_decoder_ids": forced_decoder_ids})["text"]
    return prediction


def get_audio_to_text():
    """
    Record and transcribe speech.

    :return transcription: Transcribed recording.
    """
    audio_frames, sample_size = record_speech()

    output_file = "/tmp/output.wav"
    save_recording(audio_frames, sample_size, output_file)

    transcription = get_text(output_file)
    # TODO: Fix writing errors in transcription.

    return transcription
