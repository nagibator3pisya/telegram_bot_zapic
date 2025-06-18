from aiogram import Router, F,types
from aiogram.types import CallbackQuery
from aiogram.types import Message
from Config.config import settings
from bot.Dao.ModelDao import ApplicationDao
from bot.km_command_admin.kb_admin import admin_keyboard

admin_router = Router()

@admin_router.callback_query(F.data == "admin_panel", F.from_user.id.in_(settings.ID_ADMIN))
async def start_admin(call: CallbackQuery):
    await call.answer('Доступ в админ-панель разрешен!')
    await call.message.edit_text(
        text="Выберите необходимое действие",
        reply_markup=admin_keyboard()
    )


@admin_router.callback_query(F.data == "application_admin", F.from_user.id.in_(settings.ID_ADMIN))
async def application_admin(callback_query: types.CallbackQuery):
    # Предположим, что у вас есть идентификатор пользователя, заявки которого вы хотите просмотреть
    user_id = callback_query.from_user.id  # Или другой способ получения user_id

    # Получаем заявки пользователя
    applications = await ApplicationDao.get_all_applications()

    if applications is not None:
        if applications:
            # Формируем сообщение с информацией о заявках
            response = "Список заявок пользователя:\n\n"
            for app in applications:
                response += (
                    f"ID заявки: {app['application_id']}\n"
                    f'Имя {app["client_name"]}\n'
                    f"Дата: {app['appointment_date']}\n"
                    f"Время: {app['appointment_time']}\n\n"
                )
        else:
            response = "У пользователя нет заявок."
    else:
        response = "Произошла ошибка при получении заявок пользователя."

    # Отправляем ответ пользователю
    await callback_query.message.answer(response)




    
