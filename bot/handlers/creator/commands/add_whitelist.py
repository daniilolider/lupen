from pathlib import Path
from aiogram.types import Message


async def cmd_add_whitelist(message: Message) -> None:
    """Добавляет chatid (чат) в белый список"""
    from bot.misc.env import KEYS

    if KEYS.WHITELIST_STATUS:  # whitelist должен быть включен

        path = Path('bot', 'data', 'databases', 'whitelist', 'whitelist.txt')
        with open(path, 'r', encoding='utf-8') as f:
            chat_id = str(message.chat.id)
            whitelist = [id.rstrip() for id in f.readlines()]

        # Есть ли id чата уже в whitelist
        if chat_id in whitelist:
            print('chat_id is already in the whitelist')
        else:
            # Записываем новый id чата
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'{chat_id}\n')
            print('chat_id has been added')

    else:
        print("whitelist isn't enable")
