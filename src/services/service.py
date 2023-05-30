import httpx

from db import session, crud
from db.schemas import QuestionSchemaDB
from utils.utils import get_api


async def add_question(questions_num: int):
    """Логика проверки и добавления новых вопросов из api викторины в базу"""

    new_questions = []
    api = get_api()

    # сессия для запросов к апи
    async with httpx.AsyncClient() as client:
        # сессия для обращений к базе
        async with session.begin():
            for _ in range(questions_num):
                while True:
                    response = await client.get(url=api)
                    question_data = response.json()[0]

                    question: QuestionSchemaDB = QuestionSchemaDB(**question_data)
                    is_question = await crud.get_question_db(question.id)

                    if not is_question:
                        new_question = await crud.add_question(question)
                        new_questions.append(new_question)
                        break

    return new_questions
