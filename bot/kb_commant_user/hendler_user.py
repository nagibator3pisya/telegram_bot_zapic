from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_calendar import SimpleCalendar, get_user_locale, SimpleCalendarCallback

from Config.config import bd, logger
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
    await message.answer(text='Отлично, теперь введите дату',reply_markup=await SimpleCalendar().start_calendar())
    await state.set_state(Form.appointment_date)


@handled_user_router.callback_query(SimpleCalendarCallback.filter(), StateFilter(Form.appointment_date))
async def process_simple_calendar(callback_query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.answer(text=f"Вы выбрали дату: {date.strftime('%Y-%m-%d')}")
        await state.update_data(appointment_date=date.strftime('%Y-%m-%d'))
        await callback_query.message.answer("Пожалуйста, выберите время:", reply_markup=get_time_keyboard())
        await state.set_state(Form.appointment_time)


@handled_user_router.callback_query(lambda call: call.data.startswith("time_selected:"), Form.appointment_time)
async def process_time_selection(call: types.CallbackQuery, state: FSMContext):
    selected_time = call.data.split(":")[1]
    await state.update_data(correct_time=selected_time)
    data = await state.get_data()
    await call.message.answer(
        text=f'Имя: {data["client_name"]}\nФамилия: {data["client_surname"]}\nДата: {data["appointment_date"]}\nВремя: {selected_time}',
        reply_markup=check_data()
    )
    await state.set_state(Form.check_state)




@handled_user_router.callback_query(F.data == 'correct', Form.check_state)
async def save_data(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    await call.answer('Данные сохранены')
    data = await state.get_data()

    await ApplicationDao.create(
        client_name=data["client_name"],
        client_surname=data["client_surname"],
        appointment_date=data["correct_date"],
        appointment_time=data["correct_time"]
    )

    logger.info(f'Данные сохранены {data}')



    await call.message.answer('↙️ Выберите нужное меню ↘️',reply_markup=main_kb(user_id))
    await state.clear()



@handled_user_router.callback_query(F.data == 'incorrect', Form.check_state)
async def restart_questionnaire(call: CallbackQuery, state: FSMContext):
    await call.answer('Запускаем сценарий с начала')
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer('Введите ваше Имя!')
    await state.set_state(Form.client_name)


