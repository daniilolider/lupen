from aiogram.types import Message


async def other_echo(message: Message):
    await message.answer(message.text)
