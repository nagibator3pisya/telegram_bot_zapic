from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from Config.config import async_session_maker
from Connect_sql.connect import connection


class BaseDAO:
    model = None

    @classmethod
    async def create(cls, **data):
        async with async_session_maker() as session:
            try:
                # Проверка на запись создана или нет
                unique_field = next(iter(data))  # +- поле уникальное
                existing_instance = await session.execute(
                    select(cls.model).filter_by(**{unique_field: data[unique_field]})
                )
                existing_instance = existing_instance.scalar_one_or_none()

                if existing_instance:
                    return existing_instance

                # Если записи нет, создаем новую
                instance = cls.model(**data)
                session.add(instance)
                await session.commit()
                return instance
            except SQLAlchemyError as e:
                await session.rollback()
                raise e

    @classmethod
    async def find_one_or_none_by_id(cls, data_id):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=data_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def update(cls, data_id, update_data):
        async with async_session_maker() as session:
            async with session.begin():
                query = select(cls.model).filter_by(id=data_id)
                result = await session.execute(query)
                instance = result.scalar_one_or_none()
                if instance:
                    for key, value in update_data.items():
                        setattr(instance, key, value)
                    await session.commit()
                    return instance
                return None

    @classmethod
    async def delete(cls, data_id):
        async with async_session_maker() as session:
            async with session.begin():
                query = select(cls.model).filter_by(id=data_id)
                result = await session.execute(query)
                instance = result.scalar_one_or_none()
                if instance:
                    await session.delete(instance)
                    await session.commit()
                    return True
                return False

    @classmethod
    async def find_by_condition(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model)
            for key, value in kwargs.items():
                query = query.filter(getattr(cls.model, key) == value)
            result = await session.execute(query)
            return result.scalars().all()


