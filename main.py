from fastapi import FastAPI
from pydantic import BaseModel
from scoring import scoring

app = FastAPI()


@app.get("/scoring")
def predict(address : str, surface : float, room_number : int):
    score = scoring(
        address=address,
        surface=surface,
        room_number=room_number)

    return {"score": score}

@app.get("/")
def root():
    return {"greeting": "Hello"}