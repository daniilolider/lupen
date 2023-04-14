from aiogram.types import Message

from bot.modules.ChatGPT.ChatGPT_reply import reply_ChatGPT
from bot.misc.env import KEYS


async def cmd_chatgpt_message(message: Message):
    """Сообщение для ChatGPT"""

    if KEYS.ChatGPT_STATUS:  # Чат должен быть включён

        if message.text[2:].rstrip() != '':
            experctation_text = '🤖ChatGPT печатает для вас ответ✏️\nПожалуйста, подождите...⏳'
            await message.answer(experctation_text)
            reply = reply_ChatGPT(message)
            await message.answer(reply)
        else:
            text = '😞Вы ввели пустую строку\n' \
                   '🙏Пожалуйста, введите <b>свой вопрос</b> для ChatGPT'
            await message.answer(text)

    else:
        text = '😞<b>К сожалению, в данный момент ChatGPT находится в отпуске</b>🌴'
        await message.answer(text)
