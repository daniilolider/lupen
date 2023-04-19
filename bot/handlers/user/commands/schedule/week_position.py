from aiogram.types import Message

from bot.modules.schedule.week_position import up_down_week


async def cmd_week_position(message: Message):
    """Выводит позицию недели (верхняя/нижняя)"""
    if up_down_week():
        await message.answer('⬇️Сейчас нижняя неделя⬇️')
    else:
        await message.answer('⬆️Сейчас верхняя неделя⬆️')
