from datetime import datetime

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_calendar import SimpleCalendar, SimpleCalendarCallback

from Config.config import bd
from bot.Dao.ModelDao import ApplicationDao
from bot.FSM.FSM_anketa import Form
from bot.kb_commant_user.kb_user import check_data, get_time_keyboard
from bot.main_kb.main_kb import main_kb

handled_user_router = Router()



@handled_user_router.callback_query(F.data == 'fill_application')
async def start_zapic(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text='Введите ваше Имя!')
    await state.set_state(Form.client_name)

@handled_user_router.message(Form.client_name)
async def process_correct_name(message: Message, state: FSMContext):
    await state.update_data(client_name=message.text)
    await message.answer(text='Спасибо!\n\nА теперь введите фамилию')
    await state.set_state(Form.client_surname)

@handled_user_router.message(Form.client_surname)
async def process_correct_surname(message: Message, state: FSMContext):
    await state.update_data(client_surname=message.text)
    await message.answer(text='Отлично, теперь выберите дату:', reply_markup=await SimpleCalendar().start_calendar())
    await state.set_state(Form.appointment_date)


@handled_user_router.callback_query(SimpleCalendarCallback.filter(), Form.appointment_date)
async def process_simple_calendar(callback_query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.answer(text=f"Вы выбрали дату: {date.strftime('%Y-%m-%d')}")
        await state.update_data(appointment_date=date.strftime('%Y-%m-%d'))
        await callback_query.message.answer(text='Отлично, теперь введите время',reply_markup=get_time_keyboard())
        await state.set_state(Form.appointment_time)



@handled_user_router.callback_query(lambda call: call.data.startswith("time_selected:"), Form.appointment_time)
async def process_time_selection(call: types.CallbackQuery, state: FSMContext):
    selected_time_str = call.data.split(":")[1]

    # Проверяем, содержит ли строка только час, и добавляем ":00", если это так
    if len(selected_time_str) <= 2:  # Если строка содержит только час
        selected_time_str += ":00"

    # Преобразуем строку времени в объект времени
    selected_time = datetime.strptime(selected_time_str, "%H:%M").time()

    # Обновляем состояние с выбранным временем
    await state.update_data(correct_time=selected_time)

    # Получаем данные из состояния
    data = await state.get_data()

    # Форматируем время обратно в строку для отображения
    formatted_time = selected_time.strftime("%H:%M")

    await call.message.answer(
        text=f'Имя: {data["client_name"]}\nФамилия: {data["client_surname"]}\n'
             f'Дата: {data["appointment_date"]}\nВремя: {formatted_time}',
        reply_markup=check_data()
    )

    await state.set_state(Form.check_state)


@handled_user_router.callback_query(F.data == 'correct', Form.check_state)
async def save_data(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    data = await state.get_data()

    await ApplicationDao.create(
        client_name=data["client_name"],
        client_surname=data["client_surname"],
        appointment_date=data["appointment_date"],
        appointment_time=data["correct_time"],
        user_id=user_id
    )
    await call.message.answer('↙️ Выберите нужное меню ↘️',reply_markup=main_kb(user_id))
    await state.clear()



@handled_user_router.callback_query(F.data == 'incorrect', Form.check_state)
async def restart_questionnaire(call: CallbackQuery, state: FSMContext):
    await call.answer('Запускаем сценарий с начала')
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer('Введите ваше Имя!')
    await state.set_state(Form.client_name)



# application
@handled_user_router.callback_query(F.data == 'application')
async def application(call:CallbackQuery):
    user_id = call.from_user.id




