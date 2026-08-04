from app.language.normalizer import normalize
from app.language.detector import detect_language


def process_text(text):

    clean_text = normalize(text)

    language = detect_language(clean_text)

    return {
        "text": clean_text,
        "language": language
    }
