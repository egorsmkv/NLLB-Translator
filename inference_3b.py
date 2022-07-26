import torch

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# CONFIG

TASK = 'translation'
CKPT = 'facebook/nllb-200-3.3B'

SRC = 'eng_Latn'
DST = 'ukr_Cyrl'

MAX_LEN = 400

TEXT = 'well i shared what my friend got (i dont need imaginary, i have real, if you know what that means)'

# RUN

device = 0 if torch.cuda.is_available() else -1

model = AutoModelForSeq2SeqLM.from_pretrained(CKPT)
tokenizer = AutoTokenizer.from_pretrained(CKPT)

translation_pipeline = pipeline(TASK,
                                    model=model,
                                    tokenizer=tokenizer,
                                    src_lang=SRC,
                                    tgt_lang=DST,
                                    max_length=MAX_LEN,
                                    device=device)

result = translation_pipeline(TEXT)

translated_text = result[0]['translation_text']

print('Source text:')
print(TEXT)
print()
print('---')
print()
print('Destination text:')
print(translated_text)
