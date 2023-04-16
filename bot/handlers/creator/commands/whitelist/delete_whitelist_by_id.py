from pathlib import Path
from aiogram.types import Message


async def cmd_delete_whitelist_by_id(message: Message) -> None:
    """Добавляет chatid (чат) в белый список"""
    from bot.misc.env import KEYS

    if KEYS.WHITELIST_STATUS:  # whitelist должен быть включен

        path = Path('bot', 'data', 'databases', '', 'whitelist.txt')
        with open(path, 'r', encoding='utf-8') as f:
            whitelist = [id for id in f.readlines()]

        # Есть ли chat_id уже в whitelist
        if str(message.text.split()[-1]) in [id.rstrip() for id in whitelist]:
            whitelist.remove(f'{message.text.split()[-1]}\n')

            # Удаляем
            with open(path, 'w', encoding='utf-8') as f:
                f.writelines(whitelist)
            print('chat_id has been removed')

        else:
            print("such chat_id isn't in the whitelist")

    else:
        print("whitelist isn't enable")
