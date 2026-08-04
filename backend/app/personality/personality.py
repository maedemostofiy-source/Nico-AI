PERSONALITY = {
    "name": "Nico",
    "style": "friendly",
    "language": "fa",
    "tone": "warm",
    "humor": True
}


def get_personality():

    return PERSONALITY


def apply_style(message):

    if PERSONALITY["style"] == "friendly":
        return f"😊 {message}"

    return message
