from fastapi import FastAPI
from app.ai.brain import nico

app = FastAPI()

@app.get("/")
def home():
    return {
        "name": "Nico",
        "status": "online"
    }

@app.get("/chat")
def chat(message: str):
    response = nico.think(message)
    return {
        "answer": response
    }
