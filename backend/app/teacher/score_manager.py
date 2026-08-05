from app.memory.memory import get_session, save_session


def initialize_score():

    save_session("score", 0)
    save_session("questions", 0)
    save_session("correct_answers", 0)

    return {
        "status": "initialized",
        "message": "Score system started."
    }


def update_score(is_correct):

    score = get_session("score") or 0
    questions = get_session("questions") or 0
    correct_answers = get_session("correct_answers") or 0


    questions += 1


    if is_correct:
        score += 1
        correct_answers += 1


    save_session("score", score)
    save_session("questions", questions)
    save_session("correct_answers", correct_answers)


    return {
        "score": score,
        "questions": questions,
        "correct_answers": correct_answers
    }


def get_score():

    return {
        "score": get_session("score") or 0,
        "questions": get_session("questions") or 0,
        "correct_answers": get_session("correct_answers") or 0
    }
