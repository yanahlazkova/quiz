import pymongo.database
from fastapi import FastAPI, requests
import os, json
from pymongo import MongoClient


app = FastAPI()
filename = 'questions.json'

@app.post('/questions')
async def post_questions(db_questions):
    """ сохраняет данные из файла json в БД"""
    # получим данные из файла
    questions = load_data_from_file()
    # сохраним в БД
    if questions:
        # db_questions.insert_many(questions)
        print(questions)

def load_data_from_file():
    """ получает данные из файла json """
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            questions = json.load(file)

        return questions
    else:
        return []
