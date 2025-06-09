from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    client_name:State()
    client_surname:State()
    appointment_date:State()
    appointment_time: State()



