from aiogram.types import Message


async def txt_top_secret(message: Message):
    await message.reply('Согласен')
