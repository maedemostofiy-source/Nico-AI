from app.vocabulary.dictionary import VOCABULARY


def search_word(word):

    word = word.lower().strip()

    if word not in VOCABULARY:
        return None

    return VOCABULARY[word]


def format_word(word):

    data = search_word(word)

    if not data:
        return None

    answer = f"""
📖 Word: {word}

🇮🇷 Meaning:
{data["meaning"]}

🔊 Pronunciation:
{data["pronunciation"]}

📝 Part of Speech:
{data["part_of_speech"]}

💡 Example:
{data["example"]}

📚 Translation:
{data["translation"]}

🎯 Level:
{data["level"]}

🔄 Synonyms:
{", ".join(data["synonyms"]) if data["synonyms"] else "None"}

🚫 Antonyms:
{", ".join(data["antonyms"]) if data["antonyms"] else "None"}
"""

    return answer.strip()
