from aiogram.types import Message


async def cmd_adminhelp(message: Message):
    """Помощь админа"""
    await message.answer('Тут должна быть помощь админа')
