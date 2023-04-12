from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def vuz2_keyboard() -> InlineKeyboardMarkup:
    """Inline клавиатура сообщения Рeйтинг"""

    builder = InlineKeyboardBuilder()

    exams = InlineKeyboardButton(text='Экзамены', callback_data='exams')
    offsets = InlineKeyboardButton(text='Зачеты', callback_data='offsets')
    first_module = InlineKeyboardButton(text='Первый модуль', callback_data='first_module')
    second_module = InlineKeyboardButton(text='Второй модуль', callback_data='second_module')
    finale_module = InlineKeyboardButton(text='Итоговый модуль', callback_data='finale_module')

    builder.row(exams, offsets)
    builder.row(first_module, second_module)
    builder.row(finale_module)

    keyboard = builder.as_markup()

    return keyboard
