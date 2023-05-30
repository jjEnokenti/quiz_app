from sqlalchemy import Column, Integer, String, DateTime, func

from .db import Base


class Question(Base):
    """Модель Вопроса."""
    __tablename__ = 'quetions'

    id = Column(Integer(), primary_key=True)
    question = Column(String(500))
    answer = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
