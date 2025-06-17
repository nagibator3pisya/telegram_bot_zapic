import datetime
from sqlalchemy import func, TIMESTAMP, Integer
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Базовый класс для моделей
class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True  # Этот класс не будет создавать отдельную таблицу

    # Общее поле "id" для всех таблиц
    # id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


    # Автоматическое определение имени таблицы
    @classmethod
    @property
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'