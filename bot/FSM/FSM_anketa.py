from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    client_name = State()
    client_surname = State()
    client_phone = State()
    appointment_date = State()
    appointment_time = State()
    check_state = State()



