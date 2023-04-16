from aiogram.types import Message


async def cmd_chat_id(message: Message) -> None:
    """Выводит в консоль chatid"""
    from bot.misc.env import KEYS

    if KEYS.WHITELIST_STATUS:  # whitelist должен быть включен
        print(message.chat.id)
    else:
        print("whitelist isn't enable")
