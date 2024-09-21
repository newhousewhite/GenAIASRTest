"""
whisper prompting references
1. https://cookbook.openai.com/examples/whisper_prompting_guide
2. https://medium.com/axinc-ai/prompt-engineering-in-whisper-6bb18003562d: prompt vs prefix

Prompt examples:
1, capitalization of name (e.g., President Biden)
2, Pass names in the prompt to prevent misspellings
    prompt="Glossary: Aimee, Shawn, BBQ, Whisky, Doughnuts, Omelet"
3, Long prompts may be more reliable at steering Whisper.
  # long prompts are more reliable
  prompt="i have some advice for you. multiple sentences help establish a pattern. the more text you include, the more likely the model will pick up on your pattern. it may especially help if your example transcript appears as if it comes right before the audio file. in this case, that could mean mentioning the contacts i stick in my eyes."

"""

import sys
from openai import OpenAI
import os


_, audio_path = sys.argv

# prompt = "<Instruction> Try to use Glossary and Misspelling correction guide for closely sounded words for your transcription" + \
#          "\nGlossary: Michelle, Yong-in, P E" + \
#          "\nMisspelling correction: correct P.E. to P E"
# prompt = "Glossary: Aimee, Shawn, BBQ, Whisky, Doughnuts, Omelet"
# prompt = "Glossary: Pee-ee"
prompt = "Transcribe in Korean using glossary: 피이, 홈워크, 짐내스틱"
# prompt = ""

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

audio_file = open(audio_path, "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  response_format="verbose_json",
  # timestamp_granularities=["word"],
  prompt=prompt,
)
print(transcription.text)

print("END!")
