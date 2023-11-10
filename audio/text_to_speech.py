"""
Function to get speech from an input text.

By using the 'suno/bark-small' transformer model from the huggingface hub, the input text is transformed into audio,
which is then output over the speakers.
"""
import torch
import simpleaudio
from transformers import AutoProcessor, BarkModel
from optimum.bettertransformer import BetterTransformer

import logging
logger = logging.getLogger()

# TODO Remove: "The BetterTransformer implementation does not support padding during training, as the fused
#  kernels do not support attention masks. Beware that passing padded batched data during training may result in
#  unexpected outputs. Please refer to https://huggingface.co/docs/optimum/bettertransformer/overview for more details."
# TODO Remove: The attention mask and the pad token id were not set. As a consequence, you may observe unexpected
#  behavior. Please pass your input's `attention_mask` to obtain reliable results.
#  Setting `pad_token_id` to `eos_token_id`:10000 for open-end generation.


def get_audio(input_text):
    """
    Converts text into audio and plays it back.

    :param input_text: Text to be converted into speech.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    logger.info(f"Device: {device}")

    processor = AutoProcessor.from_pretrained("suno/bark-small")
    model = BarkModel.from_pretrained("suno/bark-small").to(device)

    # Optimize the speed by converting the model into a BetterTransformer
    model = BetterTransformer.transform(model, keep_original_model=False)  # Same? model = model.to_bettertransformer()
    if device == "cuda":
        model.enable_cpu_offload()

    voice_preset = "v2/de_speaker_3"  # German speakers: v2/de_speaker_0 to 9 (speakers 3 and 8 are female)
    inputs = processor(input_text, voice_preset=voice_preset).to(device)  # , return_tensors="pt")

    # TODO: Voice sometimes continues after sentence with some weird sounds
    audio_array = model.generate(**inputs)  # , do_sample=True)
    audio_array = audio_array.cpu().numpy().squeeze()
    sampling_rate = model.generation_config.sample_rate

    # Play audio. To save audio to disk: scipy.io.wavfile.write("bark_generation.wav", sampling_rate, audio_array)
    num_channels = 1
    bytes_per_sample = 4  # float32
    play_obj = simpleaudio.play_buffer(audio_array, num_channels, bytes_per_sample, sampling_rate)

    # Wait for playback to finish before exiting
    play_obj.wait_done()
