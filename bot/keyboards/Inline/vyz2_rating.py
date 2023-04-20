from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def vuz2_keyboard() -> InlineKeyboardMarkup:
    """Inline клавиатура сообщения Рeйтинг"""

    exams = InlineKeyboardButton(text='Экзамены', callback_data='vuz2_exams')
    offsets = InlineKeyboardButton(text='Зачеты', callback_data='vuz2_offsets')
    first_module = InlineKeyboardButton(text='Первый модуль', callback_data='vuz2_first_module')
    second_module = InlineKeyboardButton(text='Второй модуль', callback_data='vuz2_second_module')
    finale_module = InlineKeyboardButton(text='Итоговый модуль', callback_data='vuz2_finale_module')
    passes_button = InlineKeyboardButton(text='Пропуски', callback_data='vuz2_passes')

    kb = [
        [exams, offsets],
        [first_module, second_module],
        [finale_module, passes_button]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard
