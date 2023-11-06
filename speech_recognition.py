import torch
import pyaudio
import wave
import numpy
import threading
import print_colors as pc
from transformers import WhisperProcessor, WhisperForConditionalGeneration, pipeline, WhisperTokenizer
from array import array
from queue import Queue, Full


# Microphone stream configurations
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000  # Or: 44100
MIN_VOLUME = 500
SILENCE_LIMIT = 1
# If the recording thread can't consume fast enough, the listener will start discarding
BUF_MAX_SIZE = CHUNK_SIZE * 10


def main():
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
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK_SIZE)

    pc.print_red("Recording started")

    frames = []

    try:
        while True:
            data = stream.read(CHUNK_SIZE)
            numpy_data = numpy.frombuffer(data, dtype=numpy.int16)
            frames.append(data)  # With numpy_data it'll be a list of numpy.ndarrays
    except KeyboardInterrupt:
        pass

    pc.print_red("Recording ended")

    # Convert the list of numpy-arrays into a 1D array (column-wise)
    # audio = numpy.hstack(frames)

    stream.stop_stream()
    stream.close()
    p.terminate()

    save_recording(frames, p.get_sample_size(FORMAT))


def save_recording(frames, sampling_width):
    output_file = "output.wav"

    wf = wave.open(output_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(sampling_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def get_text(audio_path):
    # Whisper Pipeline from Huggingface for Long-Form Transcription:
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Load model and processor
    processor = WhisperProcessor.from_pretrained("openai/whisper-base")
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-base")
    tokenizer = WhisperTokenizer.from_pretrained("openai/whisper-base", language="german")
    forced_decoder_ids = processor.get_decoder_prompt_ids(language="german", task="transcribe")

    whisper_pipeline = pipeline('automatic-speech-recognition',
                                model="openai/whisper-base",
                                tokenizer=tokenizer,
                                chunk_length_s=30,
                                device=device)

    prediction = whisper_pipeline(audio_path,
                                  batch_size=8,
                                  generate_kwargs={"forced_decoder_ids": forced_decoder_ids})["text"]
    print(prediction)


if __name__ == "__main__":
    main()
    record_speech()

    audio = "/home/luna/workspace/Dialogsteuerung/output.wav"
    get_text(audio)
