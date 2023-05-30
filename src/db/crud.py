from typing import Any

from sqlalchemy import select

from db import Question, session
from db.schemas import QuestionSchemaDB


async def get_question_db(question_id: Any) -> Question | None:
    statement = select(Question).where(Question.id == question_id)
    result = await session.execute(statement=statement)

    return result.scalar_one_or_none()


async def add_question(question: QuestionSchemaDB) -> Question | None:
    new_question = Question(
        **question.dict()
    )

    session.add(new_question)

    return new_question
