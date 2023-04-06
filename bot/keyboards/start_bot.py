from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_menu_kb() -> ReplyKeyboardMarkup:
    """Клавиатура при запуске бота"""

    keyboard = ReplyKeyboardBuilder()

    keyboard.button(text='Меню')
    keyboard.button(text='Помощь')
    keyboard.adjust(2)

    return keyboard.as_markup(resize_keyboard=True)
