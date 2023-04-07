from aiogram.types import CallbackQuery

from bot.modules.schedule.week_position import WEEK_POSITION


async def week_position(callback: CallbackQuery):
    """Выводит позицию недели (верхняя/нижняя)"""

    if WEEK_POSITION:
        await callback.message.answer('Сейчас нижняя неделя')
    else:
        await callback.message.answer('Сейчас верхняя неделя')