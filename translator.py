from transformers import pipeline
translator = pipeline("translation_en_to_ru", "Helsinki-NLP/opus-mt-en-ru")
translator("I feel i ought to bring up another small matter")
