import requests

API_URL = "http://127.0.0.1:8000"

def add_questions(questions):
    print('api_requests.py')
    data = {
        "questions": questions
    }
    response = requests.post(f"{API_URL}/questions", json=data)
    if response.status_code == 201:
        print("Questions and answers added successfully")
    else:
        print(f"Failed to add questions and answers: {response.status_code}, {response.text}")


def clear_all_questions():
    print("Очистка")
    response = requests.delete(f"{API_URL}/questions")
    if response.status_code == 200:
        print("response.status_code:", response.status_code)
        return response.json()
    else:
        print("response.status_code:", response.status_code)
        print("Failed to retrieve questions:", response.status_code, response.text)
        return []

# другие функции для работы с API
