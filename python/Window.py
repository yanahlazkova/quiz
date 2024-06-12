import customtkinter as ctk

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

        self.button_clear_questions = ctk.CTkButton(self.frame_clear_collection, text="Clear all questions")
        self.button_clear_questions.pack(pady=5)

        # Add Collection Widgets
        self.label_add_collection = ctk.CTkLabel(self.frame_add_collection, text="Add collection")
        self.label_add_collection.pack(pady=5)
        self.button_add_collection = ctk.CTkButton(self.frame_add_collection, text="Add users",
                                                   command=self.add_collection)
        self.button_add_collection.pack(pady=5)

        self.button_add_questions = ctk.CTkButton(self.frame_add_collection, text="Add questions")
        self.button_add_questions.pack(pady=5)


    def clear_collection(self):
        collection_users = self.db_quiz.users
        collection_users.delete_many({})
        print(collection_users.count_documents({}))

    def add_collection(self):
        collections_users_db_sample_mflix = self.db_sample_mflix.users
        collections_users_db_quiz = self.db_quiz.users

        users_list = list(collections_users_db_sample_mflix.find({}))

        collections_users_db_quiz.insert_many(users_list)

        print("Add collection", collections_users_db_quiz.count_documents({}))
