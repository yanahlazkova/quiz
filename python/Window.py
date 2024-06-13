import customtkinter as ctk
import main_settings

class MyWindow(ctk.CTk):
    def __init__(self, db_quiz, db_sample_mflix):

        super().__init__()

        self.db_sample_mflix = db_sample_mflix
        self.db_quiz = db_quiz
        ctk.set_appearance_mode("light")  # Настройка внешнего вида (может быть "light", "dark", или "system")
        ctk.set_default_color_theme("blue")  # Установка темы

        self.title("Settings")
        self.geometry("500x300")

        # Frame 1
        self.frame_clear_collection = ctk.CTkFrame(self, border_width=2, border_color="#3B8ED0")
        self.frame_clear_collection.pack(side='left', pady=10, padx=10, expand=True, fill='both')

        # Frame 2
        self.frame_add_collection = ctk.CTkFrame(self, border_width=2, border_color="#3B8ED0")
        self.frame_add_collection.pack(side='left', pady=10, padx=10, expand=True, fill='both')

        # Clear Collection Widgets
        self.label_clear_collection = ctk.CTkLabel(self.frame_clear_collection, text="Clear or delete")
        self.label_clear_collection.pack(pady=5)
        self.button_clear_collection = ctk.CTkButton(self.frame_clear_collection, text="Clear all users",
                                                     command=self.clear_collection)
        self.button_clear_collection.pack(pady=5)

        self.button_clear_questions = ctk.CTkButton(self.frame_clear_collection, text="Clear all questions",
                                                    command=self.clear_questions)
        self.button_clear_questions.pack(pady=5)

        # Add Collection Widgets
        self.label_add_collection = ctk.CTkLabel(self.frame_add_collection, text="Add collection")
        self.label_add_collection.pack(pady=5)
        self.button_add_collection = ctk.CTkButton(self.frame_add_collection, text="Add users",
                                                   command=self.add_collection)
        self.button_add_collection.pack(pady=5)

        self.button_add_questions = ctk.CTkButton(self.frame_add_collection, text="Add questions",
                                                  command=self.add_questions)
        self.button_add_questions.pack(pady=5)


    def clear_collection(self):
        collection_users = self.db_quiz.users
        collection_users.delete_many({})
        print(collection_users.count_documents({}))

    def clear_questions(self):
        collection_questions = self.db_quiz.questions
        collection_answers = self.db_quiz.answer_options
        collection_questions.delete_many({})
        collection_questions.delete_many({})
        print(collection_questions.count_documents({}))
        print(collection_answers.count_documents({}))

    def add_collection(self):
        collections_users_db_sample_mflix = self.db_sample_mflix.users
        collections_users_db_quiz = self.db_quiz.users

        users_list = list(collections_users_db_sample_mflix.find({}))

        collections_users_db_quiz.insert_many(users_list)

        print("Add collection", collections_users_db_quiz.count_documents({}))


    def add_questions(self):
        source_questions = main_settings.load_data_from_file()
        collection_questions = self.db_quiz.questions
        collection_answers = self.db_quiz.answer_options

        # Разделение данных на две части
        questions = []
        answers = []

        for item in source_questions:
            # Добавление данных в коллекцию вопросов
            question = {
                "order": item["order"],
                "text": item["text"]
            }
            questions.append(question)

            # Добавление данных в коллекцию ответов
            answer = {
                "order": item["order"],
                "answers": item["answer"]
            }
            answers.append(answer)

        collection_questions.insert_many(questions)
        collection_answers.insert_many(answers)

        print("Add questions", collection_questions.count_documents({}))
