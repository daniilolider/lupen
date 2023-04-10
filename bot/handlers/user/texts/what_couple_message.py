from aiogram.types import Message

from bot.modules.schedule.what_couple_now import what_couple_now


async def txt_what_couple(message: Message):
    """Сообщение с расписаниями"""
    await message.answer(what_couple_now())
