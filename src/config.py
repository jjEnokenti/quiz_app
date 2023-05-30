import os

from dotenv import load_dotenv

load_dotenv()

__all__ = (
    'settings',
)


class Config:
    USER = os.getenv('DB_USER', 'postgres')
    PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
    HOST = os.getenv('DB_HOST', 'localhost')
    PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'postgres')

    WEB_HOST = os.getenv('WEB_HOST', 'localhost')
    WEB_PORT = os.getenv('WEB_PORT', '8000')

    DATABASE_URL = (f'postgresql+asyncpg://'
                    f'{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')


settings = Config()
