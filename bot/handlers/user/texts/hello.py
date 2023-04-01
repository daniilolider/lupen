from aiogram.types import Message


async def txt_hello(message: Message):
    await message.reply('И тебе привет')
