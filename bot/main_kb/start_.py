from aiogram import types, Router
from aiogram.filters import Command

from Config.config import bd, logger
from bot.Dao.ModelDao import ProfileDao, UserDao
from bot.main_kb.main_kb import main_kb

start_router = Router()

@start_router.message(Command('start'))
async def start_bot(message: types.Message):
    try:
        telegram_id = message.from_user.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        username = message.from_user.username

        logger.info(f"Получены данные пользователя: {telegram_id}, {first_name}, {last_name}, {username}")

        # Регистрация пользователя
        user = await UserDao.register_user(
            telegram_id=telegram_id,
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        logger.info(f"Пользователь зарегистрирован: {user}")

        # Регистрация профиля
        profile = await ProfileDao.register_profile(
            user_id=user.id,
            first_name=first_name,
            last_name=last_name
        )
        logger.info(f"Профиль создан: {profile}")

        await message.answer('Добро пожаловать!',reply_markup=main_kb(user_id=telegram_id))

    except Exception as e:
        logger.error(f"Произошла ошибка: {e}", exc_info=True)
        await message.answer('Произошла ошибка при регистрации.')