from aiogram.types import Message

from bot.modules.schedule.week_position import up_down_week
from bot.data.schedule import days


text = '📄<b>Выбранное расписание:</b>\n\n'


async def cmd_monday(message: Message):
    """Выводит расписание на понедельник верхней/нижней недели"""
    if up_down_week():
        await message.answer(text + days.MONDAY_DOWN)
    else:
        await message.answer(text + days.MONDAY_UP)


async def cmd_tuesday(message: Message):
    """Выводит расписание на вторник верхней/нижней недели"""
    if up_down_week():
        await message.answer(text + days.TUESDAY_DOWN)
    else:
        await message.answer(text + days.TUESDAY_UP)


async def cmd_wednesday(message: Message):
    """Выводит расписание на среду верхней/нижней недели"""
    if up_down_week():
        await message.answer(text + days.WEDNESDAY_DOWN)
    else:
        await message.answer(text + days.WEDNESDAY_UP)


async def cmd_thursday(message: Message):
    """Выводит расписание на четверг верхней/нижней недели"""
    if up_down_week():
        await message.answer(text + days.THURSDAY_DOWN)
    else:
        await message.answer(text + days.THURSDAY_UP)


async def cmd_friday(message: Message):
    """Выводит расписание на пятницу верхней/нижней недели"""
    if up_down_week():
        await message.answer(text + days.FRIDAY_DOWN)
    else:
        await message.answer(text + days.FRIDAY_UP)
