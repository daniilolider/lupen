from aiogram.types import CallbackQuery

from bot.data.schedule import weeks


async def week(callback: CallbackQuery):
    """Выводит расписание на всю неделю"""

    text = 'Выбранное расписание:\n'

    await callback.message.answer(text + weeks.WEEK)


async def down_week(callback: CallbackQuery):
    """Выводит расписание на нижнюю неделю"""

    text = 'Выбранное расписание:\n'

    await callback.message.answer(text + weeks.DOWN_WEEK)


async def up_week(callback: CallbackQuery):
    """Выводит расписание на верхнюю неделю"""

    text = 'Выбранное расписание:\n'

    await callback.message.answer(text + weeks.UP_WEEK)
