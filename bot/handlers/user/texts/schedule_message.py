from aiogram.types import Message

from bot.keyboards.Inline.schedule_message import schedule_message


async def text_schedule(message: Message):
    """Сообщение с расписаниями"""

    text = '📚<b>Выберите то, что хотите узнать:</b>'

    await message.answer(text, reply_markup=schedule_message())
