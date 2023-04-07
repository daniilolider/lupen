from aiogram.types import Message


def creator_check(message: Message) -> bool:
    """Проверяет создатель ли пользователь"""
    from bot.misc.env import KEYS

    creator_username = KEYS.creator_USERNAME

    if message.from_user.username == creator_username:
        return True
    else:
        return False
