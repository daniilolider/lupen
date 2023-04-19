from aiogram.types import CallbackQuery

from bot.modules.schedule.week_position import up_down_week


async def week_position(callback: CallbackQuery):
    """Выводит позицию недели (верхняя/нижняя)"""
    if up_down_week():
        await callback.message.answer('⬇️Сейчас <b>нижняя</b> неделя⬇️')
    else:
        await callback.message.answer('⬆️Сейчас <b>верхняя</b> неделя⬆️')
