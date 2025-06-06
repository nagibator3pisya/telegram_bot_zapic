from Config.config import logger
from bot.Dao.BaseDao import BaseDAO
from bot.models.model import User, Service, Master, Application, Profile


class UserDao(BaseDAO):
    model = User


    @classmethod
    async  def register_user(cls,telegram_id:int,first_name:str,last_name:str,username:str):
        user_data={
            'telegram_id':telegram_id,
            'first_name':first_name,
            'last_name':last_name,
            'username':username
        }
        return await cls.create(**user_data)

    @classmethod
    async def check_profile(cls, telegram_id: int):
        logger.info(f"Проверка профиля с telegram_id: {telegram_id}")
        user_profile = await cls.find_one_or_none_by_id(data_id=telegram_id)
        logger.info(f"Результат проверки профиля: {user_profile}")
        return user_profile

class ProfileDao(BaseDAO):
    model = Profile

    @classmethod
    async def register_profile(cls, user_id: int, first_name: str, last_name: str):
        profile_data = {
            'user_id': user_id,
            'first_name': first_name,
            'last_name': last_name
        }
        logger.info(f"Создание профиля с данными: {profile_data}")
        return await cls.create(**profile_data)




class MasterDao(BaseDAO):
    model = Master


class ServiceDao(BaseDAO):
    model = Service



class ApplicationDao(BaseDAO):
    model = Application

