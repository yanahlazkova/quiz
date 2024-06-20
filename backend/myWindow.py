import customtkinter as ctk
import os, json
import api_requests
import server

filename = 'questions.json'


class MyWindow(ctk.CTk):
    def __init__(self):

        super().__init__()

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
        pass

    def clear_questions(self):
        api_requests.clear_all_questions()

    def add_collection(self):
        pass

    def add_questions(self):
        """ добавление вопросов в БД"""
        # получает данные из файла json
        with open(filename, 'r', encoding='utf-8') as file:
            questions = json.load(file)

        api_requests.add_questions(questions)

if __name__ == "__main__":
    app = MyWindow()
    app.mainloop()