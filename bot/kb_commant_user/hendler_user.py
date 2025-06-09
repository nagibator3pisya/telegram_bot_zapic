from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.FSM.FSM_anketa import Form

hendler_user_router = Router()
@hendler_user_router.message(F.text.contains('Заполнить заявку'))
async def start_zapic(message: types.Message,state: FSMContext):
    await state.clear()
    await message.answer(
        text='Введите ваше Имя!'
    )
    await  state.set_state(Form.client_name)

async def process_correct_name(message: Message, state: FSMContext):
    """
    Хэндлер будет срабатывать, если введено корректное имя и переводить в
    состояние ожидания ввода возраста

    Args:
        message (Message): _description_
        state (FSMContext): _description_
    """
    # Cохраняем введенное имя в хранилище по ключу "name"
    await state.update_data(name=message.text)
    await message.answer(text='Спасибо!\n\nА теперь введите фамилию')
    # Устанавливаем состояние ожидания ввода возраста
    await state.set_state(Form.client_surname)