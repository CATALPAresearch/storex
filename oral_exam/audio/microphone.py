"""
Recording of speech from a local microphone.

Speech is recorded until disrupted by KeyboardInterrupt or a long period of
silence. This module is only used by the command line exam: it needs PortAudio
and a capture device, neither of which exists in a container. The web app
receives its audio from the browser instead, see audio.speech_recognition.
"""
import logging
import wave

import numpy
import pyaudio

from oral_exam.utils import colours

logger = logging.getLogger(__name__)

# Microphone stream configurations
CHUNK_SIZE = 1024  # Number of frames that signals are split into
FORMAT = pyaudio.paInt16  # Sound is stored in a signed 16-bit binary string
CHANNELS = 1  # Samples per frame
RATE = 44100  # Or: 16000 44100? Sampling rate (frames per second)
MIN_VOLUME = 100  # Threshold intensity that defines silence and noise signal
SILENCE_LIMIT = 3  # Max amount of seconds, where only silence is recorded


def chunk_volume(data):
    """
    Returns the root-mean-square volume of a chunk of signed 16-bit samples.

    This replaces audioop.rms, as audioop was removed from the standard library
    in Python 3.13.
    """
    samples = numpy.frombuffer(data, dtype=numpy.int16).astype(numpy.float64)
    if samples.size == 0:
        return 0
    return int(numpy.sqrt(numpy.mean(numpy.square(samples))))


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
            if chunk_volume(data) < MIN_VOLUME:
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

    # Read the sample size before closing down PortAudio, it is unavailable afterwards
    sample_size = p.get_sample_size(FORMAT)

    # Close the microphone stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames, sample_size, silence


def save_recording(frames, sampling_width, output_file):
    """
    Saves given audio frames to a given file using the specified sampling size.
    """
    with wave.open(output_file, 'wb') as audio_file:
        audio_file.setnchannels(CHANNELS)
        audio_file.setsampwidth(sampling_width)
        audio_file.setframerate(RATE)
        audio_file.writeframes(b''.join(frames))
