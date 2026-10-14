"""
Records three seconds from the local microphone and writes them to a WAV file.
Use this to check that the microphone works before starting an exam.
"""
import pyaudio

from oral_exam.audio import microphone
from oral_exam.utils.paths import run_file

SECONDS = 3
FILENAME = run_file("microphone_test.wav")

interface = pyaudio.PyAudio()
print('Recording')

stream = interface.open(format=microphone.FORMAT,
                        channels=microphone.CHANNELS,
                        rate=microphone.RATE,
                        frames_per_buffer=microphone.CHUNK_SIZE,
                        input=True)

frames = []
for _ in range(int(microphone.RATE / microphone.CHUNK_SIZE * SECONDS)):
    frames.append(stream.read(microphone.CHUNK_SIZE))

# Read the sample size before shutting PortAudio down
sample_size = interface.get_sample_size(microphone.FORMAT)
stream.stop_stream()
stream.close()
interface.terminate()

print('Finished recording')
microphone.save_recording(frames, sample_size, FILENAME)
print(f'Saved to {FILENAME}')
