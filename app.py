from fastapi import FastAPI
from pydantic import BaseModel
from rag_engine import brain
from logger import RagLogger

class UserQuestion(BaseModel):
    query:str

app=FastAPI(title="Rag Q/A")

@app.get("/")
def health_check():
    return {"message":"Api is working"}

@app.post("/ask")
def ask_question(question:UserQuestion):
    response=brain(question.query)
    RagLogger.info(f"Recived question {question.query[:100]}")
    RagLogger.info(f"AI message {response[:100]}")
    return {"AiMessage":response}