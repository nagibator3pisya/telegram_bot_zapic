from aiogram import F, types, Router
from aiogram.types import CallbackQuery

from Config.config import bd
from bot.km_command_admin.kb_admin import admin_keyboard
from bot.main_kb.main_kb import main_kb

hendler_router_main = Router()

@hendler_router_main.callback_query(F.data == 'home')
async def back_to_main_menu(call: CallbackQuery):
    telegram_id = call.from_user.id
    await call.message.edit_text('↙️ Выберите нужное меню ↘️', reply_markup=main_kb(telegram_id))




@hendler_router_main.callback_query(F.data == 'home_admin')
async def back_to_main_menu_admin(call: CallbackQuery):
    # telegram_id = call.from_user.id
    await call.message.edit_text('️Выберите необходимое действие', reply_markup=admin_keyboard())