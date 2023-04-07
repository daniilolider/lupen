from aiogram.types import CallbackQuery

from bot.modules.schedule.what_couple_now import what_couple_now


async def now_couple(callback: CallbackQuery):
    """Выводит какая сейчас пара"""
    await callback.message.answer(what_couple_now())
