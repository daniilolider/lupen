from aiogram.types import Message


async def cmd_photo_week(message: Message):
    """Выводит фотку всего расписания"""
    await message.answer('🖼<u><b>Фотка расписания:</b></u>')
    await message.answer_photo('https://disk.yandex.ru/i/GmUJu3KXc3q3sQ')
