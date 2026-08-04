def normalize(text):

    text = text.strip()

    text = text.replace("؟", "")
    text = text.replace("!", "")
    text = text.replace("?", "")

    text = " ".join(text.split())

    return text
