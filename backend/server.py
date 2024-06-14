from pymongo import MongoClient
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Connection string (replace <password> with your real password)
connection_string = "mongodb+srv://yglazkova8:s7Y3J3UOZyVGnebK@cluster0.f8nniok.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create MongoDB client
client = MongoClient(connection_string)

# Access database
db = client.quiz
collection_questions = db.questions
collection_answers = db.answer_options

class Question(BaseModel):
    order: int
    text: str

class AnswerOption(BaseModel):
    order: int
    answers: Dict[str, str]

class QuestionsAndAnswers(BaseModel):
    questions: List[Question]
    answers: List[AnswerOption]

@app.get('/questions')
async def get_all_questions():
    """Get all questions"""
    questions = list(collection_questions.find({}, {'_id': 0}))
    return questions

@app.post('/questions', status_code=201)
async def add_questions_and_answers(data: QuestionsAndAnswers):
    """Upload questions and answers"""
    questions = [q.dict() for q in data.questions]
    answers = [a.dict() for a in data.answers]

    collection_questions.insert_many(questions)
    collection_answers.insert_many(answers)
    return {"message": "Questions and answers added successfully"}
