from aiogram import Router, F,types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import bold

from Config.config import settings
from bot.Dao.ModelDao import ApplicationDao, MasterDao
from bot.FSM.FSM_anketa import Form_Master

from bot.km_command_admin.kb_admin import admin_keyboard, get_pagination_keyboard_admin,paginate_admin

admin_router = Router()

@admin_router.callback_query(F.data == "admin_panel", F.from_user.id.in_(settings.ID_ADMIN))
async def start_admin(call: CallbackQuery):
    await call.answer('Доступ в админ-панель разрешен!')
    await call.message.edit_text(
        text="Выберите необходимое действие",
        reply_markup=admin_keyboard()
    )

@admin_router.callback_query(F.data == "cancel", F.from_user.id.in_(settings.ID_ADMIN))
async def cancel_kb_inline(call: CallbackQuery,state:FSMContext):
    await state.clear()
    await call.answer('Отмена..')
    await call.message.delete()
    await call.message.answer(text='Выберите необходимое действие',reply_markup=admin_keyboard())


@admin_router.callback_query(F.data == "application_admin", F.from_user.id.in_(settings.ID_ADMIN))
async def application_admin(callback_query: types.CallbackQuery):
    page_size = 1  # Количество заявок на одной странице
    current_page = 0  # Текущая страница

    # Получаем заявки пользователя
    applications = await ApplicationDao.get_all_applications()

    if applications is not None:
        if applications:
            paginated_applications = paginate_admin(applications, page_size, current_page)

            response = "Список заявок пользователя:\n\n"
            for app in paginated_applications:
                response+=(
                    f"ID заявки: {app['application_id']}\n"
                    f"Имя: {app['client_name']}\n"
                    f"Фамилия: {app['client_surname']}\n"
                    f"Телефон: {app['client_phone']}\n"
                    f"Дата: {app['appointment_date']}\n"
                    f"Время: {app['appointment_time']}\n\n")


            total_pages = (len(applications) + page_size - 1) // page_size
            keyboard = get_pagination_keyboard_admin(current_page, total_pages)
            await callback_query.message.edit_text(response, reply_markup=keyboard)
        else:
            response = "Пока что нет заявок!"
            await callback_query.message.answer(response)
    else:
        response = "Произошла ошибка при получении заявок пользователя."
        await callback_query.message.answer(response)


@admin_router.callback_query(F.data.startswith("page_"))
async def handle_pagination(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    applications =await ApplicationDao.get_all_applications()

    page_size = 1  # Количество заявок на одной странице
    current_page = int(callback_query.data.split("_")[1])

    if applications is not None:
        if applications:
            paginated_applications = paginate_admin(applications, page_size, current_page)
            response = "Список заявок пользователя:\n\n"
            for app in paginated_applications:
                response += (f"ID заявки: {app['application_id']}\n"
                             f"Имя: {app['client_name']}\n"
                             f"Дата: {app['appointment_date']}\n"
                             f"Время: {app['appointment_time']}\n\n")

            total_pages = (len(applications) + page_size - 1) // page_size
            keyboard = get_pagination_keyboard_admin(current_page, total_pages)
            await callback_query.message.edit_text(response, reply_markup=keyboard)







