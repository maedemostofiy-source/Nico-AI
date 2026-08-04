from app.vocabulary.engine import format_word


def route(message, intent, language):
    """
    Router:
    تصمیم می‌گیرد هر پیام به کدام Engine فرستاده شود.
    """

    lower = message.lower().strip()

    # -------------------------
    # Vocabulary
    # -------------------------

    if lower.startswith("meaning of "):

        word = lower.replace("meaning of ", "").strip()

        result = format_word(word)

        if result:
            return {
                "handled": True,
                "answer": result,
                "intent": "vocabulary"
            }

        return {
            "handled": True,
            "answer": "این کلمه هنوز داخل دیکشنری نیکو نیست.",
            "intent": "vocabulary"
        }

    if lower.startswith("معنی "):

        word = lower.replace("معنی", "").strip()

        result = format_word(word)

        if result:
            return {
                "handled": True,
                "answer": result,
                "intent": "vocabulary"
            }

        return {
            "handled": True,
            "answer": "این کلمه هنوز داخل دیکشنری نیکو نیست.",
            "intent": "vocabulary"
        }

    # هنوز هیچ ماژولی این پیام را نگرفته
    return {
        "handled": False
    }
