from pathlib import Path
from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command

from bot.filters.commands_filters import commands_filters


creator_router = Router()
creator_router.message.filter(commands_filters.creator_check)

# region cmd_chat_id

@creator_router.message(Command('chat_id'))
async def cmd_chat_id(message: Message) -> None:
    """Выводит в консоль chatid"""
    print(message.chat.id)

# endregion


# region cmd_add_whitelist

@creator_router.message(Command('add_whitelist'))
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

# endregion


# region cmd_delete_whitelist

@creator_router.message(Command('delete_whitelist'))
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

# endregion

