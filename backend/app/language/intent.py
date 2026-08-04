def detect_intent(message):

    message = message.lower()


    # پرسیدن اسم
    if any(word in message for word in [
        "اسمم چیه",
        "اسم من چیه",
        "منو چی صدا میکنی",
        "یادت هست اسمم"
    ]):
        return "ask_name"



    # معرفی اسم
    if "اسم من" in message and "است" in message:
        return "set_name"



    # سلام
    if any(word in message for word in [
        "سلام",
        "درود",
        "hello"
    ]):
        return "greeting"



    return "unknown"
