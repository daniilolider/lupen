from pathlib import Path
from json import loads
from aiogram.types import Message


def vuz2_users_filter(message: Message):
    """Проверяет, есть ли пользователь в списке людей, которым доступен просмотр рейтинга"""

    path = Path('bot', 'data', 'databases', 'vuz2_list', 'vuz2_list.json')
    with open(path, 'r', encoding='utf-8') as vuz2_list:
        vuz2_list = loads(vuz2_list.read())

    user_id = str(message.from_user.id)
    if user_id in vuz2_list:
        return True
    else:
        return False
