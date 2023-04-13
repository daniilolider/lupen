from aiogram.types import Message

from bot.modules.schedule.week_position import WEEK_POSITION


async def cmd_week_position(message: Message):
    """Выводит позицию недели (верхняя/нижняя)"""
    if WEEK_POSITION:
        await message.answer('⬇️Сейчас нижняя неделя⬇️')
    else:
        await message.answer('⬆️Сейчас верхняя неделя⬆️')
