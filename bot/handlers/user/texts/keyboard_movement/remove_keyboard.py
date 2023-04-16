from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove


async def txt_remove_keyboard(message: Message):
    """Высылает сообщение, с подсказкой о возвращении клавиатуры"""

    text = '🫥Клавиатура убрана\n\n' \
           '⌨️Чтобы вернуть ее <b>введите</b>\n' \
           '✦<u><b><i>/return_keyboard</i></b></u> (Можно <u><b><i>/rk</i></b></u>) или\n' \
           '✦"<i>Вернуть кнопки</i>" (Можно "<i>ВК</i>")'

    await message.answer(text, reply_markup=ReplyKeyboardRemove())
