from aiogram.types import Message


async def cmd_adminhelp(message: Message) -> None:
    """Помощь админа"""
    await message.answer('Тут должна быть помощь админа')


async def cmd_addwhitelist(message: Message) -> None:
    """Добавляет в белый список"""
    from pathlib import Path
    path = Path('bot', 'data', 'databases', 'whitelist', 'whitelist.txt')
    with open(path, 'r', encoding='utf-8') as f:
        whitelist_to_write = f.readlines()

    whitelist_to_write.append(str(message.chat.id) + '\n')

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(whitelist_to_write)

