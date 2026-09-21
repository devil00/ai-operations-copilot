from fastapi import FastAPI
from pydantic import BaseModel

from app.copilot import Copilot


app = FastAPI(
    title="AI Operations Copilot",
    version="0.1.0",
)

copilot = Copilot()


class AskRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/copilot/ask")
def ask(request: AskRequest):
    return copilot.answer(request.question)
