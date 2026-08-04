from app.memory.memory import save_memory, get_memory
from app.personality.personality import apply_style
from app.language.processor import process_text
from app.language.intent import detect_intent
from app.vocabulary.engine import format_word


def think(message):

    # پردازش متن
    processed = process_text(message)

    clean_message = processed["text"]

    # تشخیص هدف
    intent = detect_intent(clean_message)

    # -----------------------------
    # Vocabulary
    # -----------------------------
    lower = clean_message.lower()

    if lower.startswith("meaning of "):

        word = lower.replace("meaning of ", "").strip()

        result = format_word(word)

        if result:
            return {
                "answer": apply_style(result),
                "intent": "vocabulary",
                "language": processed["language"]
            }

        return {
            "answer": apply_style("این کلمه هنوز داخل دیکشنری نیکو نیست."),
            "intent": "vocabulary",
            "language": processed["language"]
        }

    if lower.startswith("معنی "):

        word = lower.replace("معنی", "").strip()

        result = format_word(word)

        if result:
            return {
                "answer": apply_style(result),
                "intent": "vocabulary",
                "language": processed["language"]
            }

        return {
            "answer": apply_style("این کلمه هنوز داخل دیکشنری نیکو نیست."),
            "intent": "vocabulary",
            "language": processed["language"]
        }

    # -----------------------------
    # کاربر اسم می‌پرسد
    # -----------------------------
    if intent == "ask_name":

        name = get_memory("name")

        if name:
            answer = f"اسم شما {name} است."
        else:
            answer = "هنوز اسم شما را نمی‌دانم."

        return {
            "answer": apply_style(answer),
            "intent": intent,
            "language": processed["language"]
        }

    # -----------------------------
    # کاربر اسم معرفی می‌کند
    # -----------------------------
    if intent == "set_name":

        name = clean_message.replace("اسم من", "")
        name = name.replace("است", "")
        name = name.strip()

        save_memory("name", name)

        answer = f"باشه، اسم شما {name} ذخیره شد."

        return {
            "answer": apply_style(answer),
            "intent": intent,
            "language": processed["language"]
        }

    # -----------------------------
    # سلام
    # -----------------------------
    if intent == "greeting":

        answer = "سلام 😊 خوشحالم می‌بینمت."

        return {
            "answer": apply_style(answer),
            "intent": intent,
            "language": processed["language"]
        }

    # -----------------------------
    # ناشناخته
    # -----------------------------
    return {
        "answer": apply_style("هنوز این موضوع را یاد نگرفتم."),
        "intent": intent,
        "language": processed["language"]
    }
