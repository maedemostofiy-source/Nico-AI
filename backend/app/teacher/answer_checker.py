from app.memory.memory import get_session


def check_student_answer(user_answer):

    correct_answer = get_session("correct_answer")

    if correct_answer is None:
        return {
            "status": "no_active_exercise",
            "message": "❌ تمرین فعالی برای بررسی وجود ندارد."
        }

    user_answer = user_answer.strip().lower()
    correct_answer = correct_answer.strip().lower()

    if user_answer == correct_answer:
        return {
            "status": "correct",
            "message": "✅ پاسخ شما درست است."
        }

    return {
        "status": "wrong",
        "message": f"❌ پاسخ اشتباه است.\n\nپاسخ صحیح: {correct_answer}"
    }
