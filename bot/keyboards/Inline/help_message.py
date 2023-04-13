from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def help_message() -> InlineKeyboardMarkup:
    """Inline клавиатура сообщения Помощь"""

    builder = InlineKeyboardBuilder()

    schedule_button = InlineKeyboardButton(text='Расписаниe', callback_data='schedule_help')
    chatgpt_button = InlineKeyboardButton(text='Общение с Chat_GPT', callback_data='chatgpt_help')
    rating_button = InlineKeyboardButton(text='Рейтинг', callback_data='rating_help')

    builder.row(schedule_button, chatgpt_button, rating_button)

    keyboard = builder.as_markup()

    return keyboard

