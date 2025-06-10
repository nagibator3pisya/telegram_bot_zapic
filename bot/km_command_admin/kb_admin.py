
from aiogram.utils.keyboard import InlineKeyboardBuilder


def admin_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text='1 К')
    kb.button(text='2 К')
    return kb.as_markup()