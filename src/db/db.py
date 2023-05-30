from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base

from src.config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL,
    future=True,
    echo=True
)

session = AsyncSession(
    bind=engine,
    expire_on_commit=False,
)

Base = declarative_base()
