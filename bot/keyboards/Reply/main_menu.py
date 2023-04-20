from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu() -> ReplyKeyboardMarkup:
    """Клавиатура главного меню"""

    schedule_button = KeyboardButton(text='📋Расписание')
    chatgpt_quest_button = KeyboardButton(text='🤖Вопрос ChatGPT')
    vuz2_rating_button = KeyboardButton(text='🔢Рейтинг')
    what_couple_button = KeyboardButton(text='❓Какая сейчас пара?❔')
    remove_keyboard = KeyboardButton(text='⬇️Скрыть клавиатуру')
    help_button = KeyboardButton(text='❔Помощь')

    kb = [
        [schedule_button, chatgpt_quest_button, vuz2_rating_button],
        [what_couple_button],
        [help_button, remove_keyboard]
    ]

    keyboard = ReplyKeyboardMarkup(keyboard=kb,
                                   resize_keyboard=True,
                                   input_field_placeholder='Что будем делать?')

    return keyboard

