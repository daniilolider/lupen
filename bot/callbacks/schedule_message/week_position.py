from aiogram.types import CallbackQuery

from bot.modules.schedule.week_position import WEEK_POSITION


async def week_position(callback: CallbackQuery):
    """Выводит позицию недели (верхняя/нижняя)"""
    if WEEK_POSITION:
        await callback.message.answer('⬇️Сейчас <b>нижняя</b> неделя⬇️')
    else:
        await callback.message.answer('⬆️Сейчас <b>верхняя</b> неделя⬆️')
