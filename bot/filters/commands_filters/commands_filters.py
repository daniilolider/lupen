from aiogram.types import Message


def whitelist_check(message: Message) -> bool:
    """Фильтр для проверки на наличие чата в whitelist"""
    from pathlib import Path

    # Выгружаем whitelist для дальнейшей проверки
    path = Path('bot', 'data', 'databases', 'whitelist', 'whitelist.txt')
    with open(path, 'r', encoding='utf-8') as f:
        whitelist = [int(id.rstrip()) for id in f.readlines()]

    if message.chat.id in whitelist:  # Чат, в котором пытаются запустить бота находиться в whitelist
        return True
    else:
        return False


def creator_check(message: Message) -> bool:
    """Проверяет создатель ли пользователь"""
    from bot.misc.env import KEYS

    creator_username = KEYS.creator_USERNAME

    if message.from_user.username == creator_username:
        return True
    else:
        return False
