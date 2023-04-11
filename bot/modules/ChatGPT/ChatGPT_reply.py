import openai
from aiogram.types import Message


def reply_ChatGPT(message: Message):
    """Ответ ChatGPT"""
    messages = []

    user_message = message.text[2:].lstrip()

    if user_message != '':

        messages.append({"role": "user", "content": user_message})

        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        reply = chat.choices[0].message.content

        answer = f"<b><i>ChatGPT:\n</i></b>{reply}"

    else:
        answer = 'Вы ввели пустую строку :(\nПожалуйста, введите текст для ChatGPT'

    return answer  # НАДО НА ASYNC ПЕРЕПИСАТЬ
