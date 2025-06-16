from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from Config.config import logger
from bot.Dao.ModelDao import ProfileDao, UserDao

user_router = Router()


@user_router.callback_query(F.data == 'profile')
async def get_profile(call: CallbackQuery):
    telegram_id = call.from_user.id
    logger.info(f"Получение профиля для telegram_id: {telegram_id}")
    user_profile = await UserDao.find_one_or_none(telegram_id=telegram_id)

    if user_profile:
        profile_info = (
            f'ID: {user_profile.telegram_id}\n'
            f'Имя: {user_profile.first_name}\n'
            f'Фамилия: {user_profile.last_name}\n'
            f'Username: {user_profile.username}'
        )
        kb_back = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='home')]
        ])

        await call.message.edit_text(profile_info,reply_markup=kb_back)
    else:
        await call.answer('Профиль не найден.')


def get_time_keyboard():
    keyboard = InlineKeyboardMarkup()
    times = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    for time in times:
        keyboard.add(InlineKeyboardButton(time, callback_data=f"time_selected:{time}"))
    return keyboard





def check_data():
    kb_list = [
        [InlineKeyboardButton(text="✅Все верно", callback_data='correct')],
        [InlineKeyboardButton(text="❌Заполнить сначала", callback_data='incorrect')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard