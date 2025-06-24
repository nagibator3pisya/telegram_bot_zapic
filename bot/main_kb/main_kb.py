from aiogram import types
from aiogram.filters import Command
from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from Config.config import settings


def main_kb(user_id):

    kb_Inline_main =[
        [InlineKeyboardButton(text="📖 О нас",callback_data="about_us")],
        [InlineKeyboardButton(text="📝 Заполнить заявку",callback_data="fill_application")],
        [InlineKeyboardButton(text="Мои заявки", callback_data="application")],
        [InlineKeyboardButton(text="📚 Услуги",callback_data="services")]
    ]
    if user_id in settings.ID_ADMIN:
        kb_Inline_main.append([InlineKeyboardButton(text="⚙️ Админ панель",callback_data="admin_panel")])
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_Inline_main)
    return keyboard






def home_bk ():
    kb_hom = InlineKeyboardBuilder()
    kb_hom.button(text="🏠 На главную", callback_data="home")






