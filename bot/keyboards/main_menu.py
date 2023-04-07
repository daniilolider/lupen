from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def main_menu() -> ReplyKeyboardMarkup:
    """Клавиатура галвного меню"""

    builder = ReplyKeyboardBuilder()

    builder.button(text='Расписание')

    keyboard = builder.as_markup(resize_keyboard=True, input_field_placeholder='Что будем делать?')

    return keyboard

