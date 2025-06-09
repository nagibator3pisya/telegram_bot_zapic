from aiogram.types import Message



from Config.config import logger
from bot.Dao.BaseDao import BaseDAO
from bot.models.model import User, Service, Master, Application, Profile


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




class ProfileDao(BaseDAO):
    model = Profile

    @classmethod
    async def register_profile(cls, user_id: int, first_name: str, last_name: str):

        existing_profile = await cls.find_one_or_none(user_id=user_id)
        if existing_profile:
            return existing_profile

        profile_data = {
            'user_id': user_id,
            'first_name': first_name,
            'last_name': last_name
        }
        return await cls.create(**profile_data)




class MasterDao(BaseDAO):
    model = Master


class ServiceDao(BaseDAO):
    model = Service



class ApplicationDao(BaseDAO):
    model = Application

