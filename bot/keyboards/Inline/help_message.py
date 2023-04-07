from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def help_message() -> InlineKeyboardMarkup:
    """Inline клавиатура сообщения Помощь"""

    builder = InlineKeyboardBuilder()

    schedule_button = InlineKeyboardButton(text='Расписания', callback_data='schedule')
    chatgpt_button = InlineKeyboardButton(text='Общение с Chat_GPT', callback_data='chatgpt')
    rating_button = InlineKeyboardButton(text='Узнать свои баллы', callback_data='rating')

    builder.row(schedule_button, chatgpt_button, rating_button)

    keyboard = builder.as_markup()

    return keyboard

