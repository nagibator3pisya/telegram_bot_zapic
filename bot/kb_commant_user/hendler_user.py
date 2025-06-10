from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Config.config import bd
from bot.FSM.FSM_anketa import Form
from bot.kb_commant_user.kb_user import check_data

handled_user_router = Router()



@handled_user_router.message(F.text.contains('Заполнить заявку'))
async def start_zapic(message: types.Message, state: FSMContext):
    await message.answer(text='Введите ваше Имя!')
    await state.set_state(Form.client_name)

@handled_user_router.message(Form.client_name)
async def process_correct_name(message: Message, state: FSMContext):
    await state.update_data(client_name=message.text)
    await message.answer(text='Спасибо!\n\nА теперь введите фамилию')
    await state.set_state(Form.client_surname)

@handled_user_router.message(Form.client_surname)
async def process_correct_surname(message: Message, state: FSMContext):
    await state.update_data(client_surname=message.text)
    await message.answer(text='Отлично, теперь введите дату')
    await state.set_state(Form.appointment_date)

@handled_user_router.message(Form.appointment_date)
async def process_correct_date(message: Message, state: FSMContext):
    await state.update_data(correct_date=message.text)
    await message.answer(text='Отлично, теперь введите время')
    await state.set_state(Form.appointment_time)

@handled_user_router.message(Form.appointment_time)
async def process_correct_time(message: Message, state: FSMContext):
    await state.update_data(correct_time=message.text)
    data = await state.get_data()
    await message.answer(
        text=f'Имя: {data["client_name"]} Фамилия: {data["client_surname"]}\nДата: {data["correct_date"]}\nВремя: {data["correct_time"]}',
        reply_markup=check_data()
    )
    await state.set_state(Form.check_state)

# Save data
@handled_user_router.callback_query(F.data == 'correct', Form.check_state)
async def save_data(call: CallbackQuery, state: FSMContext):
    await call.answer('Данные сохранены')
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer('Благодарю за регистрацию. Ваши данные успешно сохранены!')
    await state.clear()

# Restart the questionnaire
@handled_user_router.callback_query(F.data == 'incorrect', Form.check_state)
async def restart_questionnaire(call: CallbackQuery, state: FSMContext):
    await call.answer('Запускаем сценарий с начала')
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer('Введите ваше Имя!')
    await state.set_state(Form.client_name)


