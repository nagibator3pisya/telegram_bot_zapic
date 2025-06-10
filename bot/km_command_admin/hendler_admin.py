from aiogram import Router, F
from aiogram.types import CallbackQuery

from Config.config import settings
from bot.km_command_admin.kb_admin import admin_keyboard

admin_router = Router()


@admin_router.callback_query(F.text.contains == "Админ панель", F.from_user.id.in_(settings.ID_ADMIN))
async def start_admin(call: CallbackQuery):
    await call.answer('Доступ в админ-панель разрешен!')
    await call.message.edit_text(
        text="Вам разрешен доступ в админ-панель. Выберите необходимое действие.",
        reply_markup=admin_keyboard()
    )