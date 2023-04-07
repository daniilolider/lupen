from pathlib import Path
from aiogram.types import Message


async def cmd_delete_whitelist(message: Message):
    """Удаляет chatid (чат) из белого списка"""
    path = Path('bot', 'data', 'databases', 'whitelist', 'whitelist.txt')
    with open(path, 'r', encoding='utf-8') as f:
        whitelist = f.readlines()

    # Есть ли chat_id уже в whitelist
    if str(message.chat.id) in [id.rstrip() for id in whitelist]:
        whitelist.remove(f'{str(message.chat.id)}\n')

        # Записываем
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(whitelist)
        print('chat_id has been removed')

    else:
        print("such chat_id isn't in the whitelist")
