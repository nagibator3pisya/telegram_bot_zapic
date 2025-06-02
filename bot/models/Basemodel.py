import datetime
from sqlalchemy import func, TIMESTAMP, Integer
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Базовый класс для моделей
class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True  # Этот класс не будет создавать отдельную таблицу

    # Общее поле "id" для всех таблиц
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # Поля времени создания и обновления записи
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now()
    )

    # Автоматическое определение имени таблицы
    @classmethod
    @property
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'