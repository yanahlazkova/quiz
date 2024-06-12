import Window as MyApp
from pymongo import MongoClient

# Строка подключения (замените <password> на ваш реальный пароль)
connection_string = "mongodb+srv://yglazkova8:s7Y3J3UOZyVGnebK@cluster0.f8nniok.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# connection_string2 = "mongodb+srv://ecovod2003:Andrey_76@cluster0.m33ehwo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Создание клиента MongoDB
client = MongoClient(connection_string)
# client2 = MongoClient(connection_string2)

# Получение доступа к базе данных (например, 'test')
db_quiz = client.quiz
print(type(db_quiz))
db_sample_mflix = client.sample_mflix

# Проверка подключения, вывод списка коллекций в базе данных
print(db_quiz.list_collection_names())
print(db_sample_mflix.list_collection_names())


# collection_users = db_quiz.users

# delete_all_users = collection_users.delete_many({})

app = MyApp.MyWindow(db_quiz, db_sample_mflix)
app.mainloop()
