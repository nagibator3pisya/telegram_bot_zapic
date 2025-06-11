from aiogram import F, types, Router
from aiogram.types import CallbackQuery

from Config.config import bd
from bot.main_kb.main_kb import main_kb

hendler_router_main = Router()

@hendler_router_main.callback_query(F.data == 'home')
async def back_to_main_menu(call: CallbackQuery):
    telegram_id = call.from_user.id
    await call.message.edit_text('↙️ Выберите нужное меню ↘️', reply_markup=main_kb(telegram_id))