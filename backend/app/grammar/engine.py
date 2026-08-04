from app.grammar.lessons import GRAMMAR_LESSONS


def search_grammar(topic):

    topic = topic.lower().strip()

    if topic in GRAMMAR_LESSONS:
        return GRAMMAR_LESSONS[topic]

    return None



def format_grammar(topic):

    lesson = search_grammar(topic)

    if not lesson:
        return None


    answer = f"""
📚 Grammar: {lesson["title"]}


📝 Explanation:
{lesson["description"]}


⚙️ Formula:
{lesson["formula"]}


💡 Examples:
"""


    for example in lesson["examples"]:
        answer += f"""
English:
{example["english"]}

Persian:
{example["persian"]}
"""


    answer += "\n📌 Rules:\n"

    for rule in lesson["rules"]:
        answer += f"- {rule}\n"


    answer += f"""
🎯 Level:
{lesson["level"]}
"""


    return answer.strip()
