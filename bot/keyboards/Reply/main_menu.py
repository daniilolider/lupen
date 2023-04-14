from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu() -> ReplyKeyboardMarkup:
    """Клавиатура галвного меню"""

    builder = ReplyKeyboardBuilder()

    builder.button(text='📋Расписание')
    builder.button(text='🤖Вопрос ChatGPT')
    builder.button(text='🔢Рейтинг')
    what_couple_button = KeyboardButton(text='❓Какая сейчас пара?❔')
    builder.row(what_couple_button)
    remove_keyboard = KeyboardButton(text='⬇️Скрыть клавиатуру')
    help_button = KeyboardButton(text='❔Помощь')
    builder.row(help_button, remove_keyboard)

    keyboard = builder.as_markup(resize_keyboard=True, input_field_placeholder='Что будем делать?')

    return keyboard

