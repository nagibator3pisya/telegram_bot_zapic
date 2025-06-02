from Config.config import async_session_maker
from bot.Dao.BaseDao import BaseDAO
from bot.models.model import User, Service, Master, Application, Profile


class UserDao(BaseDAO):
    model = User


    @classmethod
    async def register_user(cls, telegram_id: int, first_name: str, last_name: str, username: str):
        async with async_session_maker() as session:
            async with session.begin():
                user = cls.model(
                    telegram_id=telegram_id,
                    first_name=first_name,
                    last_name=last_name,
                    username=username
                )
                session.add(user)
                await session.commit()
                return user

class ProfileDao(BaseDAO):
    model = Profile

    @classmethod
    async  def register_profile(cls,user_id:int,first_name:str, last_name:str):
        profile_data = {
            'user_id':user_id,
            'first_name':first_name,
            'last_name':last_name
        }
        return await cls.create(**profile_data)


class MasterDao(BaseDAO):
    model = Master


class ServiceDao(BaseDAO):
    model = Service



class ApplicationDao(BaseDAO):
    model = Application

