from aiogram import types
from aiogram.filters import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from Config.config import settings


def main_kb(user_id):
    kb_list_main = [
        [KeyboardButton(text="📖 О нас"), KeyboardButton(text="👤 Профиль")],
        [KeyboardButton(text="📝 Заполнить заявку"), KeyboardButton(text="📚 Мастера")]
    ]
    if user_id in settings.ID_ADMIN:
        kb_list_main.append([KeyboardButton(text="⚙️ Админ панель")])
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list_main, resize_keyboard=True, one_time_keyboard=True)
    return keyboard






