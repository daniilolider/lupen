from aiogram.types import Message


async def echo(message: Message):
    await message.answer(message.text)


async def chat_id(message: Message) -> None:
    print(message.chat.id)
