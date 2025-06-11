from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# что б вернуться в адм понель (text="⚙️ Админ панель", callback_data="admin_panel")
def admin_keyboard():
    kb_Inline_main = [
        [InlineKeyboardButton(text="📖 О нас", callback_data="about_us")],
        [InlineKeyboardButton(text="👤 Добавить мастера", callback_data="profile")],
        [InlineKeyboardButton(text="📝 Просмотр заявок", callback_data="application_admin")],
        [InlineKeyboardButton(text="📚 Добавить услуги сервиса", callback_data="services_admin")],
        [InlineKeyboardButton(text="🏠 На главную", callback_data="home")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_Inline_main)
    return keyboard