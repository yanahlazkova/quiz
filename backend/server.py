from pymongo import MongoClient
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware
import logging
from decoder import Decoder

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Дозволені домени
    allow_credentials=True,
    allow_methods=["*"],  # Дозволені методи (GET, POST і т.д.)
    allow_headers=["*"],  # Дозволені заголовки
)

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
    question: str
    answers: list[str]
    correct_answer: int


class QuestionList(BaseModel):
    questions: List[Question]


@app.get('/questions', response_model=List[Dict])
async def get_all_questions():
    logger.info("get questions")
    """Get all questions"""
    questions = list(collection_questions.find({})) #, {'_id': 0}))

    # try:
    #     pipeline = [
    #         {
    #             "$lookup": {
    #                 "from": "answer_options",
    #                 "localField": "order",
    #                 "foreignField": "order",
    #                 "as": "answers"
    #             }
    #         },
    #         {
    #             "$addFields": {
    #                 "answers": {
    #                     "$arrayElemAt": ["$answers.answers", 0]
    #                 }
    #             }
    #         },
    #         {
    #             "$group": {
    #                 "_id": "$_id",
    #                 "order": {"$first": "$order"},
    #                 "text": {"$first": "$text"},
    #                 "answers": {"$first": "$answers"}
    #             }
    #         },
    #         {
    #             "$project": {
    #                 "_id": 0,
    #                 "order": 1,
    #                 "text": 1,
    #                 "answers": 1
    #             }
    #         }
    #     ]

        # questions_with_answers = list(collection_questions.aggregate(pipeline))
    decoder_question_dict = Decoder.decryption(questions)
    logger.info(decoder_question_dict)
    return decoder_question_dict
    #
    # except Exception as e:
    #     logger.error(f"An error occurred: {e}")
    #     raise HTTPException(status_code=500, detail="Internal Server Error")


@app.post('/questions', status_code=201)
async def add_questions(data: QuestionList):
    """Upload questions and answers"""
    print('server')
    questions = [q.dict() for q in data.questions]

    collection_questions.insert_many(questions)
    return {"message": "Questions added successfully"}

@app.delete('/questions', status_code=200)
async def clear_all_questions():
    logger.info("Clear")
    collection_questions.delete_many({})
    collection_answers.delete_many({})
    logger.info(collection_questions.count_documents({}))

