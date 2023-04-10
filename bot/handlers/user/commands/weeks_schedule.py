from aiogram.types import Message

from bot.data.schedule import weeks


text = '📄<b>Выбранное расписание:</b>\n\n'


async def cmd_week(message: Message):
    """Выводит расписание на всю неделю"""
    await message.answer(text + weeks.WEEK)


async def cmd_down_week(message: Message):
    """Выводит расписание на нижнюю неделю"""
    await message.answer(text + weeks.DOWN_WEEK)


async def cmd_up_week(message: Message):
    """Выводит расписание на верхнюю неделю"""
    await message.answer(text + weeks.UP_WEEK)
