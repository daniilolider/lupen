from aiogram.types import Message


def chatgpt_message_filter(message: Message) -> bool:
    """Проверяет, написано ли сообщение для ChatGPT"""
    if message.text.rstrip()[:2] in ('/?', '/q', '!?', '!q'):
        return True
    else:
        return False
