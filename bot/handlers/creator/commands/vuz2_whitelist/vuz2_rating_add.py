from pathlib import Path
from aiogram.types import Message
import json


async def cmd_add_rating_whitelist(message: Message) -> None:
    """Добавляет пользователя в список для рейтинга vuz2"""

    path = Path('bot', 'data', 'databases', 'vuz2_list', 'vuz2_list.json')
    with open(path, 'r', encoding='utf-8') as f:
        vuz2_list = json.loads(f.read())

    user_id, vuz2_id = (message.text.split()[1:])

    if user_id not in vuz2_list:  # Пользователя не должно в списке

        vuz2_list[user_id] = vuz2_id

        with open(path, 'w') as f:
            json.dump(vuz2_list, f)
        print('user has been added in the whitelist in vuz2 rating list')

    else:
        print('user is already in the whitelist in vuz2 rating list')

