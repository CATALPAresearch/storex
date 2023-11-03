import os
import torch
from transformers import pipeline, AutoProcessor, AutoModel, BarkModel
from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio
from scipy.io.wavfile import write

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

# synthesiser = pipeline("text-to-speech", model="suno/bark-small")
# speech = synthesiser("Wie geht es dir?", forward_params={"do_sample": True})
# Audio(speech, rate=SAMPLE_RATE)  # TypeError
# exit(0)

# # Optimizing:
# device = "cuda" if torch.cuda.is_available() else "cpu"
# # load in fp16
# model = BarkModel.from_pretrained("suno/bark-small", torch_dtype=torch.float16).to(device)
# # convert to bettertransformer
# model = model.to_bettertransformer()
# # model = BetterTransformer.transform(model, keep_original_model=False)
# # enable CPU offload
# model.enable_cpu_offload()

processor = AutoProcessor.from_pretrained("suno/bark-small")
model = AutoModel.from_pretrained("suno/bark-small")  # .to(device)  # Or BarkModel?

voice_preset = "v2/en_speaker_6"
inputs = processor("Hello, my dog is cute", voice_preset=voice_preset)  # , return_tensors="pt") or .to(device)

audio_array = model.generate(**inputs)  # , do_sample=True)
audio_array = audio_array.cpu().numpy().squeeze()

sampling_rate = model.generation_config.sample_rate
Audio(audio_array, rate=sampling_rate)
exit(0)

# Save audio to disk (working)
# write("bark_generation.wav", sampling_rate, audio_array)

text_prompt = """
     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
     But I also have other interests such as playing tic tac toe.
"""
audio_array = generate_audio(text_prompt)
Audio(audio_array, rate=SAMPLE_RATE)

# Running locally with bark:
# download and load all models
preload_models()

# generate audio from text
text_prompt = """
     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
     But I also have other interests such as playing tic tac toe.
"""
speech_array = generate_audio(text_prompt)

# play text in notebook
Audio(speech_array, rate=SAMPLE_RATE)
