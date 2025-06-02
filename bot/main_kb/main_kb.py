from aiogram import types, Router
from aiogram.filters import Command

from Config.config import bd, logger
from bot.Dao.ModelDao import ProfileDao, UserDao
start_router = Router()

@start_router.message(Command('start'))
async def start_bot(message: types.Message):
    telegram_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    logger.info(f"Получены данные пользователя: {telegram_id}, {first_name}, {last_name}, {username}")
    # Регистрация пользователя
    user = await UserDao.register_user(telegram_id, first_name, last_name, username)

    # Создание профиля для пользователя
    await ProfileDao.register_profile(user.id, first_name, last_name)

    await message.answer('Добро пожаловать!')
