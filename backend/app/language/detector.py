def detect_language(text):

    persian_chars = 0
    english_chars = 0

    for char in text:
        if '\u0600' <= char <= '\u06FF':
            persian_chars += 1

        elif char.isalpha():
            english_chars += 1


    if persian_chars > english_chars:
        return "fa"

    elif english_chars > persian_chars:
        return "en"

    return "unknown"
