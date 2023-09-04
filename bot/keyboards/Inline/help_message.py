from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def help_message() -> InlineKeyboardMarkup:
    """Inline клавиатура сообщения Помощь"""

    schedule_button = InlineKeyboardButton(text='Расписаниe', callback_data='schedule_help')
    chatgpt_button = InlineKeyboardButton(text='Общение с Chat_GPT', callback_data='chatgpt_help')
    #rating_button = InlineKeyboardButton(text='Рейтинг', callback_data='rating_help')

    kb = [[schedule_button, chatgpt_button]]  # Без rating_button

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard

