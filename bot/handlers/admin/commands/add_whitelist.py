from aiogram.types import Message
from bot.data.database.whitelist.create import create


async def cmd_add_whitelist(message: Message) -> None:
    """Добавление в белый список"""
    import sqlite3

    conn = sqlite3.connect('bot\data\database\whitelist\whitelist.db')
    cur = conn.cursor()

    cur.execute(create(0, message.chat.id)[0], create(0, message.chat.id)[1])
    conn.commit()
