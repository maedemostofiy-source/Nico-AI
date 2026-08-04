import json
import os

MEMORY_FILE = "user_memory.json"


def save_memory(key, value):
    data = load_memory()
    data[key] = value

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_memory(key):
    data = load_memory()
    return data.get(key, None)
