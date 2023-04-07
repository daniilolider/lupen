from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def help_message() -> InlineKeyboardMarkup:
    """Клавиатура сообщения Помощь"""

    builder = InlineKeyboardBuilder()

    schedule_button = InlineKeyboardButton(text='Расписания', callback_data='schedule')
    chatgpt_button = InlineKeyboardButton(text='Общение с Chat_GPT', callback_data='chatgpt')

    builder.row(schedule_button, chatgpt_button)

    keyboard = builder.as_markup(row_width=3)

    return keyboard

