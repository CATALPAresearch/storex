"""
Class to transcribe audio recorded from a microphone.

Speech is recorded from the microphone until disrupted by KeyboardInterrupt or long period of silence.
The audio is then transcribed into predicted text and returned.
"""
import audioop
import pyaudio
import wave

from transformers import WhisperProcessor, WhisperTokenizer, pipeline
from utils import colours

import logging
logger = logging.getLogger()

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
MIN_VOLUME = 100  # Threshold intensity that defines silence and noise signal
SILENCE_LIMIT = 3  # Max amount of seconds, where only silence is recorded
BUF_MAX_SIZE = CHUNK_SIZE * 10  # If the recording thread can't consume fast enough, the listener will start discarding


def record_speech():
    """
    Records audio from microphone input until the set silence limit is reached.
    Returns the audio frames and used sampling size as well as information if only silence was detected.
    """
    # Set the microphone stream
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK_SIZE)

    colours.print_red("*** Recording started ***")

    frames = []
    silence_counter = 0
    silence = True

    try:
        # Record the microphone input from stream
        while True:
            data = stream.read(CHUNK_SIZE)
            frames.append(data)

            # Check for silence via root-mean-square
            rms = audioop.rms(data, 2)
            if rms < MIN_VOLUME:
                silence_counter += CHUNK_SIZE / RATE
                logger.debug(silence_counter)
            # Reset the silence counter and mark the recording as not solely containing silence
            else:
                silence_counter = 0
                silence = False
            # Stop recording, when silence limit is reached
            if silence_counter >= SILENCE_LIMIT:
                break
    # Stop recording when pressing of Ctr+C is detected
    except KeyboardInterrupt:
        pass

    colours.print_red("*** Recording ended ***")

    # Close the microphone stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    sample_size = p.get_sample_size(FORMAT)
    return frames, sample_size, silence


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
        audio_frames, sample_size, silence = record_speech()
        transcription = None

        if not silence:
            # Save the recording to a temporary directory
            output_file = "/tmp/output.wav"
            save_recording(audio_frames, sample_size, output_file)

            # Transcribe the recording
            transcription = self.pipeline(output_file,
                                          batch_size=8,
                                          generate_kwargs={"forced_decoder_ids": self.forced_decoder_ids})["text"]

        return transcription
