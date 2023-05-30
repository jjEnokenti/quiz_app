import datetime

from pydantic import BaseModel


class QuestionResponse(BaseModel):
    """Схема для выдачи вопроса пользователю."""
    question: str

    class Config:
        orm_mode = True


class QuestionRequest(BaseModel):
    """Схема для получения количества вопросов."""
    questions_num: int


class QuestionSchemaDB(BaseModel):
    """Схема вопроса для сохранения в базу."""
    id: int
    question: str
    answer: str
    created_at: datetime.datetime
