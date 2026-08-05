from app.grammar.lessons import GRAMMAR_LESSONS
from app.grammar.exercises import GRAMMAR_EXERCISES
from app.memory.memory import save_session

import random


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



def format_exercise(topic):

    topic = topic.lower().strip()

    if topic not in GRAMMAR_EXERCISES:
        return None

    exercise = random.choice(GRAMMAR_EXERCISES[topic])
    save_session("current_topic", topic)
    save_session("current_question", exercise["question"])
    save_session("correct_answer", exercise["answer"])

    answer = f"""
📝 Grammar Exercise

Topic:
{topic.title()}

Question:
{exercise["question"]}

Choices:

A) {exercise["choices"][0]}
B) {exercise["choices"][1]}
C) {exercise["choices"][2]}

✅ Correct Answer:
{exercise["answer"]}
"""

    return answer.strip()
