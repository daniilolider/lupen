from aiogram.types import Message

from bot.modules.schedule.what_couple_now import what_couple_now


async def cmd_now_couple(message: Message):
    """Выводит какая сейчас пара"""
    await message.answer(what_couple_now())
