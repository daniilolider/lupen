from aiogram.types import Message

from bot.modules.ChatGPT.ChatGPT_reply import reply_ChatGPT


async def cmd_chatgpt_message(message: Message):
    """Сообщение для ChatGPT"""
    reply = reply_ChatGPT(message)
    await message.answer(reply)
