from aiogram.types import Message


async def cmd_chat_id(message: Message) -> None:
    """Выводит в консоль chatid"""
    print(message.chat.id)
