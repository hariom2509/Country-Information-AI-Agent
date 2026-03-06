from fastapi import FastAPI
from pydantic import BaseModel

from app.graph import graph

app = FastAPI()


class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
def ask(request: QuestionRequest):

    question = request.question.strip()

    if not question:
        return {"error": "Question cannot be empty"}

    result = graph.invoke({
        "question": question
    })

    return {
        "question": question,
        "answer": result["answer"]
    }