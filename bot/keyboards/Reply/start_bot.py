from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_menu_kb() -> ReplyKeyboardMarkup:
    """Клавиатура при запуске бота"""

    menu_button = KeyboardButton(text='📓Меню')
    help_button = KeyboardButton(text='❔Помощь')

    kb = [[menu_button, help_button]]

    keyboard = ReplyKeyboardMarkup(keyboard=kb,
                                   resize_keyboard=True,
                                   input_field_placeholder='Куда пойдем?')

    return keyboard
