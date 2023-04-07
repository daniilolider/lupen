from aiogram.types import Message


async def text_schedule(message: Message):
    """Сообщение с расписаниями"""
    from bot.keyboards.Inline.schedule_message import schedule_message

    text = 'Выберите 📚раcписание, которое вам нужно:'

    await message.answer(text, reply_markup=schedule_message())
