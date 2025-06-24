from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext

from Config.config import settings
from bot.Dao.ModelDao import MasterDao
from bot.FSM.FSM_anketa import Form_Master, Form
from bot.km_command_admin.kb_admin import cancel_kb_inline

fsm_admins = Router()

@fsm_admins.callback_query(F.data == 'add_master_admin', F.from_user.id.in_(settings.ID_ADMIN))
async def start_add_master(callback_query: types.CallbackQuery,state: FSMContext):
    await callback_query.message.edit_text(text="Пожалуйста, введите имя мастера:", reply_markup=cancel_kb_inline())
    await state.set_state(Form_Master.master_name)



@fsm_admins.message(Form_Master.master_name)
async def process_master_name(message: types.Message, state: FSMContext):
    master_name = message.text
    try:
        await MasterDao.add_master(master_name)
        await message.answer(f"Мастер {master_name} успешно добавлен!")
    except Exception as e:
        await message.answer(f"Не удалось добавить мастера {e}")

    await state.clear()