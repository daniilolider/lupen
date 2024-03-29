import openai
from aiogram.types import Message


# НАДО НА ASYNC ПЕРЕПИСАТЬ
async def reply_ChatGPT(message: Message):
    """Ответ ChatGPT"""
    messages = []

    user_message = message.text[2:].lstrip()

    messages.append({"role": "user", "content": user_message})

    chat = await openai.ChatCompletion.acreate(model="gpt-3.5-turbo", messages=messages)

    reply = chat.choices[0].message.content

    answer = f"<b><i>ChatGPT:\n</i></b>{reply}"

    return answer
