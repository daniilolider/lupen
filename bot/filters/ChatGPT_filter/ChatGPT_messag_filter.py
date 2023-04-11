from aiogram.types import Message


def chatgpt_message_filter(message: Message) -> bool:
    """Проверяет, написано ли сообщение для ChatGPT"""
    if message.text.rstrip()[:2] == '/?' or message.text.rstrip()[:2] == '/q' or \
            message.text.rstrip()[:2] == '!?' or message.text.rstrip()[:2] == '!q':
        return True
    else:
        return False
