from app.grammar.engine import format_grammar


def teach_lesson(topic):

    lesson = format_grammar(topic)

    if lesson is None:
        return {
            "status": "not_found",
            "answer": "❌ این درس هنوز داخل نیکو وجود ندارد."
        }

    return {
        "status": "success",
        "answer": lesson
    }
