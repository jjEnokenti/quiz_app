from fastapi import status

from services import service
from src.app import app
from src.db.schemas import QuestionResponse, QuestionRequest


@app.post(
    '/',
    response_model=list[QuestionResponse],
    description='Речка выдачи вопросов пользователю и добавления новых в базу',
    summary='Выдача и добавление в базу новых вопросов',
    status_code=status.HTTP_200_OK
)
async def index(request: QuestionRequest) -> list[QuestionResponse]:
    return await service.add_question(request.questions_num)
