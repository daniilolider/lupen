from pathlib import Path
from aiogram.types import Message


async def cmd_add_whitelist(message: Message) -> None:
    """Добавляет chatid (чат) в белый список"""
    path = Path('bot', 'data', 'databases', 'whitelist', 'whitelist.txt')
    with open(path, 'r', encoding='utf-8') as f:
        whitelist = f.readlines()

    # Есть ли chat_id уже в whitelist
    if str(message.chat.id) in [id.rstrip() for id in whitelist]:
        print('chat_id is already in the whitelist')

    else:
        whitelist.append(str(message.chat.id) + '\n')

        # Записываем
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(whitelist)
        print('chat_id has been added')
