from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_menu_kb() -> ReplyKeyboardMarkup:
    """Клавиатура при запуске бота"""

    builder = ReplyKeyboardBuilder()

    builder.button(text='📓Меню')
    builder.button(text='❔Помощь')

    keyboard = builder.as_markup(resize_keyboard=True, input_field_placeholder='Куда пойдем?')

    return keyboard
