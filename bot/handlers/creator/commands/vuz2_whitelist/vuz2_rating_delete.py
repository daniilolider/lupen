from pathlib import Path
from aiogram.types import Message
import json


async def cmd_delete_rating_whitelist(message: Message) -> None:
    """Удаляет пользователя из списка для рейтинга vuz2"""

    path = Path('bot', 'data', 'databases', 'vuz2_list', 'vuz2_list.json')
    with open(path, 'r', encoding='utf-8') as f:
        vuz2_list = json.loads(f.read())

    user_id = message.text.split()[1]

    if user_id in vuz2_list:  # Пользователь должен быть в списке

        del vuz2_list[user_id]

        with open(path, 'w') as f:
            json.dump(vuz2_list, f)
        print('user has been removed in the whitelist in vuz2 rating list')

    else:
        print("user isn't already in the whitelist in vuz2 rating list")

