import requests

API_URL = "http://127.0.0.1:8000"

def add_questions(questions, answers):
    print('api_requests.py')
    data = {
        "questions": questions,
        "answers": answers
    }
    response = requests.post(f"{API_URL}/questions", json=data)
    if response.status_code == 201:
        print("Questions and answers added successfully")
    else:
        print(f"Failed to add questions and answers: {response.status_code}, {response.text}")


def get_all_questions():
    response = requests.get(f"{API_URL}/questions")
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve questions:", response.status_code, response.text)
        return []

# другие функции для работы с API
