from app.memory.memory import get_session


def check_answer(user_answer):

    correct_answer = get_session("correct_answer")

    if correct_answer is None:
        return {
            "status": "no_question",
            "message": "هیچ تمرین فعالی وجود ندارد."
        }

    user_answer = user_answer.strip().lower()
    correct_answer = correct_answer.strip().lower()

    if user_answer == correct_answer:

        return {
            "status": "correct",
            "message": "✅ Correct!"
        }

    return {
        "status": "wrong",
        "message": f"❌ Wrong.\n\nCorrect Answer:\n{correct_answer}"
    }
