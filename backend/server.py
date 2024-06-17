from pymongo import MongoClient
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware
import logging
from bson import ObjectId
from bson.json_util import dumps

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
    text: str


class AnswerOption(BaseModel):
    order: int
    answers: Dict[str, str]


class QuestionsAndAnswers(BaseModel):
    questions: List[Question]
    answers: List[AnswerOption]


@app.get('/questions', response_model=List[Dict])
async def get_all_questions():
    """Get all questions"""
    # questions = list(collection_questions.find({}, {'_id': 0}))
    # answers = list(collection_answers.find({}, {'_id': 0}))

    try:
        pipeline = [
            {
                "$lookup": {
                    "from": "answer_options",
                    "localField": "order",
                    "foreignField": "order",
                    "as": "answers"
                }
            },
            {
                "$addFields": {
                    "answers": {
                        "$arrayElemAt": ["$answers.answers", 0]
                    }
                }
            },
            {
                "$group": {
                    "_id": "$_id",
                    "order": {"$first": "$order"},
                    "text": {"$first": "$text"},
                    "answers": {"$first": "$answers"}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "order": 1,
                    "text": 1,
                    "answers": 1
                }
            }
        ]

        questions_with_answers = list(collection_questions.aggregate(pipeline))
        return questions_with_answers

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

        # return dumps(questions_with_answers)

    # questions = list(collection_questions.find({}))
    # answers = list(collection_answers.find({}))
    # # Создаем словарь для временного хранения данных по ключу "order"
    # combined_dict = {}
    #
    # # Добавляем ответы в словарь
    # for answer in answers:
    #     order = answer["order"]
    #     if order not in combined_dict:
    #         combined_dict[order] = {}
    #     combined_dict[order].update(answer)
    #
    # # Добавляем вопросы в словарь
    # for question in questions:
    #     order = question["order"]
    #     if order not in combined_dict:
    #         combined_dict[order] = {}
    #     combined_dict[order].update(question)
    #
    #     # Перетворюємо тимчасовий словник на список
    #     combined_list = list(combined_dict.values())
    #     logger.info((combined_list))
    #     questions_json = dumps(combined_list)  # Використовуємо bson.json_util.dumps для серіалізації BSON у JSON
    #     # logger.info(questions_json)
    #     return questions_json

@app.post('/questions', status_code=201)
async def add_questions_and_answers(data: QuestionsAndAnswers):
    """Upload questions and answers"""
    print('server')
    questions = [q.dict() for q in data.questions]
    answers = [a.dict() for a in data.answers]

    collection_questions.insert_many(questions)
    collection_answers.insert_many(answers)
    return {"message": "Questions and answers added successfully"}

@app.delete('/questions')
async def clear_all_questions():
    collection_questions.delete_many({})
    collection_answers.delete_many({})
    print(collection_questions.count_documents({}))
    print(collection_answers.count_documents({}))
