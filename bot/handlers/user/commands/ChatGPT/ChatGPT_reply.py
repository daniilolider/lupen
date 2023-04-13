from aiogram.types import Message

from bot.modules.ChatGPT.ChatGPT_reply import reply_ChatGPT


async def cmd_chatgpt_message(message: Message):
    """Сообщение для ChatGPT"""

    if message.text[2:].rstrip() != '':
        experctation_text = '🤖ChatGPT печатает для вас ответ✏️\nПожалуйста, подождите...⏳'
        await message.answer(experctation_text)
        reply = reply_ChatGPT(message)
        await message.answer(reply)
    else:
        await message.answer('Вы ввели пустую строку :(\nПожалуйста, введите текст для ChatGPT')
