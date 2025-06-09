from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message

from Config.config import logger
from bot.Dao.ModelDao import ProfileDao, UserDao

user_router = Router()

@user_router.message(Command('profile'))
@user_router.message(F.text.contains('Профиль'))
async def get_profile(message: Message):
    telegram_id = message.from_user.id
    logger.info(f"Получение профиля для telegram_id: {telegram_id}")
    user_profile = await UserDao.find_one_or_none(telegram_id=telegram_id)

    if user_profile:
        profile_info = (
            f'ID: {user_profile.telegram_id}\n'
            f'Имя: {user_profile.first_name}\n'
            f'Фамилия: {user_profile.last_name}\n'
            f'Username: {user_profile.username}'
        )
        await message.answer(profile_info)
    else:
        await message.answer('Профиль не найден.')