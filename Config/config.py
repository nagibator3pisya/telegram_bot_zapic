import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
#
# from bot.main import start_router

load_dotenv()


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    BOT_TOKEN: str
    ID_ADMIN:int
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    )

    def get_db_url(self):
        return (f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")



settings = Settings()
# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=settings.BOT_TOKEN)
bd = Dispatcher()

# Регистрация роутеров
# bd.include_router(start_router)


database_url = settings.get_db_url()
print(database_url)
engine = create_async_engine(url=database_url)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession,expire_on_commit=False)