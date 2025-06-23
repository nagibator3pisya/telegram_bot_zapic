from gc import callbacks

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from Config.config import logger
from bot.Dao.ModelDao import UserDao

user_router = Router()




def get_time_keyboard():
    # Создаем список списков для кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=time, callback_data=f"time_selected:{time}")]
        for time in ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    ])
    return keyboard




def check_data():
    kb_list = [
        [InlineKeyboardButton(text="✅Все верно", callback_data='correct')],
        [InlineKeyboardButton(text="❌Заполнить сначала", callback_data='incorrect')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)
    return keyboard

def paginate(items, page_size, page):
    start = page * page_size
    end = start + page_size
    return items[start:end]

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_pagination_keyboard(current_page: int, total_pages: int):
    # Создаем список для кнопок
    keyboard_buttons = []

    keyboard_buttons.append([InlineKeyboardButton(text='Меню', callbacks_data="home")])

    # Кнопка "Назад", если текущая страница не первая
    if current_page > 0:
        keyboard_buttons.append([InlineKeyboardButton(text ="⬅️ Назад", callback_data=f"page_{current_page - 1}")])



    # Кнопка "Вперед", если текущая страница не последняя
    if current_page < total_pages - 1:
        keyboard_buttons.append([InlineKeyboardButton(text ="Вперед ➡️", callback_data=f"page_{current_page + 1}")])

    # Создаем клавиатуру с кнопками
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
    return keyboard