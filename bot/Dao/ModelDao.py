from aiogram.types import Message
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

from Config.config import logger, async_session_maker
from bot.Dao.BaseDao import BaseDAO
from bot.models.model import User, Service, Master, Application


class UserDao(BaseDAO):
    model = User

    @classmethod
    async def register_user(cls, telegram_id: int, first_name: str, last_name: str, username: str):
        # проверка есть ли такой id
        existing_user = await cls.find_one_or_none(telegram_id=telegram_id)
        if existing_user:
            return existing_user
        # add нового
        user_data = {
            'telegram_id': telegram_id,
            'first_name': first_name,
            'last_name': last_name,
            'username': username
        }
        return await cls.create(**user_data)




# class ProfileDao(BaseDAO):
#     model = Profile
#
#     @classmethod
#     async def register_profile(cls, user_id: int, first_name: str, last_name: str):
#
#         existing_profile = await cls.find_one_or_none(user_id=user_id)
#         if existing_profile:
#             return existing_profile
#
#         profile_data = {
#             'user_id': user_id,
#             'first_name': first_name,
#             'last_name': last_name
#         }
#         return await cls.create(**profile_data)




class MasterDao(BaseDAO):
    model = Master


class ServiceDao(BaseDAO):
    model = Service



class ApplicationDao(BaseDAO):
    model = Application

    @classmethod
    async def get_applications_by_user(cls, user_id: int):
        """
        Возвращает все заявки пользователя по user_id с дополнительной информацией
        о мастере и услуге.

        Аргументы:
            user_id: Идентификатор пользователя.

        Возвращает:
            Список заявок пользователя с именами мастеров и услуг.
        """
        async with async_session_maker() as session:
            try:
                # Используем joinedload для ленивой загрузки связанных объектов
                query = (
                    select(cls.model)
                    .options(joinedload(cls.model.master), joinedload(cls.model.service))
                    .filter_by(user_id=user_id)
                )
                result = await session.execute(query)
                applications = result.scalars().all()

                # Возвращаем список словарей с нужными полями
                return [
                    {
                        "application_id": app.id,
                        'client_name': app.client_name,
                        'client_surname': app.client_surname,
                        'client_phone': app.client_phone,
                        "appointment_date": app.appointment_date,
                        "appointment_time": app.appointment_time,
                    }
                    for app in applications
                ]
            except SQLAlchemyError as e:
                print(f"Error while fetching applications for user {user_id}: {e}")
                return None


    @classmethod
    async def get_all_applications(cls):
        """
        Возвращает все заявки в базе данных с дополнительной информацией о мастере и услуге.

        Возвращает:
            Список всех заявок с именами мастеров и услуг.
        """
        async with async_session_maker() as session:
            try:
                # Используем joinedload для загрузки связанных данных
                query = (
                    select(cls.model)
                    .options(joinedload(cls.model.master), joinedload(cls.model.service))
                )
                result = await session.execute(query)
                applications = result.scalars().all()

                # Возвращаем список словарей с нужными полями
                return [
                    {
                        "application_id": app.id,
                        "user_id": app.user_id,
                        # "service_name": app.service.service_name,  # Название услуги
                        # "master_name": app.master.master_name,  # Имя мастера
                        "appointment_date": app.appointment_date,
                        "appointment_time": app.appointment_time,
                        "client_name": app.client_name,  # Имя клиента

                    }
                    for app in applications
                ]
            except SQLAlchemyError as e:
                print(f"Error while fetching all applications: {e}")
                return None
