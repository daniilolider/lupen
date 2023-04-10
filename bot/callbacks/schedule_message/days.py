from aiogram.types import CallbackQuery

from bot.modules.schedule.week_position import WEEK_POSITION
from bot.data.schedule import days


text = '📄<b>Выбранное расписание:</b>\n\n'


async def monday(callback: CallbackQuery):
    """Выводит расписание на понедельник верхней/нижней недели"""
    if WEEK_POSITION:
        await callback.message.answer(text + days.MONDAY_DOWN)
    else:
        await callback.message.answer(text + days.MONDAY_UP)


async def tuesday(callback: CallbackQuery):
    """Выводит расписание на вторник верхней/нижней недели"""
    if WEEK_POSITION:
        await callback.message.answer(text + days.TUESDAY_DOWN)
    else:
        await callback.message.answer(text + days.TUESDAY_UP)


async def wednesday(callback: CallbackQuery):
    """Выводит расписание на среду верхней/нижней недели"""
    if WEEK_POSITION:
        await callback.message.answer(text + days.WEDNESDAY_DOWN)
    else:
        await callback.message.answer(text + days.WEDNESDAY_UP)


async def thursday(callback: CallbackQuery):
    """Выводит расписание на четверг верхней/нижней недели"""
    if WEEK_POSITION:
        await callback.message.answer(text + days.THURSDAY_DOWN)
    else:
        await callback.message.answer(text + days.THURSDAY_UP)


async def friday(callback: CallbackQuery):
    """Выводит расписание на пятницу верхней/нижней недели"""
    if WEEK_POSITION:
        await callback.message.answer(text + days.FRIDAY_DOWN)
    else:
        await callback.message.answer(text + days.FRIDAY_UP)
