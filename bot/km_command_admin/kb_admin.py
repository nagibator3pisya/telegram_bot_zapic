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




def get_pagination_keyboard_admin(current_page: int, total_pages: int):
    # Создаем список для кнопок
    keyboard_buttons = []

    # Создаем ряд для кнопок
    button_row = []

    # Кнопка "Меню"


    # Кнопка "Назад", если текущая страница не первая
    if current_page > 0:
        button_row.append(InlineKeyboardButton(text="⬅️ Назад", callback_data=f"page_{current_page - 1}"))

    button_row.append(InlineKeyboardButton(text='Меню', callback_data="home_admin"))
    # Кнопка "Вперед", если текущая страница не последняя
    if current_page < total_pages - 1:
        button_row.append(InlineKeyboardButton(text="Вперед ➡️", callback_data=f"page_{current_page + 1}"))

    # Добавляем ряд кнопок в клавиатуру
    keyboard_buttons.append(button_row)

    # Создаем клавиатуру с кнопками
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
    return keyboard



def paginate_admin(items, page_size, page):
    start = page * page_size
    end = start + page_size
    return items[start:end]