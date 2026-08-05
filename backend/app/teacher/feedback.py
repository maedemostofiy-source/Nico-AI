def generate_feedback(result, user_answer=None, correct_answer=None):

    if result == "correct":

        return {
            "status": "success",
            "feedback": "✅ عالی! پاسخ شما درست است."
        }


    if result == "wrong":

        return {
            "status": "error",
            "feedback": (
                "❌ پاسخ اشتباه است.\n\n"
                f"پاسخ شما: {user_answer}\n\n"
                f"پاسخ صحیح: {correct_answer}"
            )
        }


    return {
        "status": "unknown",
        "feedback": "⚠️ نتیجه قابل تشخیص نیست."
    }
