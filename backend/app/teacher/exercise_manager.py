from app.grammar.engine import format_exercise


def give_exercise(topic):

    exercise = format_exercise(topic)

    if exercise is None:

        return {
            "status": "not_found",
            "answer": "❌ برای این درس هنوز تمرینی وجود ندارد."
        }

    return {
        "status": "success",
        "answer": exercise
    }
