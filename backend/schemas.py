from pydantic import BaseModel


class Question(BaseModel):
    order: int
    text: str
    is_correct: bool


class AnswerOption(BaseModel):
    order: int
    answer: list[str, str, str, str]