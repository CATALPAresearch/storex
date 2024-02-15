"""
Class to get speech from an input text.

By using the 'suno/bark-small' transformer model from the huggingface hub, the input text is transformed into audio,
which is then output over the speakers.
"""
import simpleaudio
import torch

from optimum.bettertransformer import BetterTransformer
from transformers import AutoProcessor, BarkModel

import logging
logger = logging.getLogger()

class TextToSpeech:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Text-to-Speech device: {self.device}")

        model_name = "suno/bark-small"
        self.processor = AutoProcessor.from_pretrained(model_name)
        self.model = BarkModel.from_pretrained(model_name).to(self.device)

        # Optimize the speed by converting the model into a BetterTransformer
        self.model = BetterTransformer.transform(self.model, keep_original_model=False)  # Same? model = model.to_bettertransformer()
        if self.device == "cuda":
            self.model.enable_cpu_offload()

        self.voice_preset = "v2/de_speaker_3"  # German speakers: v2/de_speaker_0 to 9 (speakers 3 and 8 are female)

    def get_audio(self, input_text):
        """
        Converts text into audio and plays it back.

        :param input_text: Text to be converted into speech.
        """
        inputs = self.processor(input_text, voice_preset=self.voice_preset).to(self.device)  # , return_tensors="pt")

        audio_array = self.model.generate(**inputs, pad_token_id=10000)
        audio_array = audio_array.cpu().numpy().squeeze()
        sampling_rate = self.model.generation_config.sample_rate

        # Play audio. To save audio to disk: scipy.io.wavfile.write("bark_generation.wav", sampling_rate, audio_array)
        num_channels = 1
        bytes_per_sample = 4  # float32
        play_obj = simpleaudio.play_buffer(audio_array, num_channels, bytes_per_sample, sampling_rate)

        # Wait for playback to finish before exiting
        play_obj.wait_done()
