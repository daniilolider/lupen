from pathlib import Path
from aiogram.types import Message
from json import loads

from bot.modules.vuz2rating.handler_vuz2 import vuz2_request


async def txt_vuz2_rating(message: Message):
    """Выводит таблицу рейтинга с сайта http://vuz2.bru.by/rate/"""

    path = Path('bot', 'data', 'databases', 'vuz2_list', 'vuz2_list.json')
    with open(path, 'r', encoding='utf-8') as vuz2_list:
        vuz2_list = loads(vuz2_list.read())

    user_id = str(message.from_user.id)
    if user_id in vuz2_list:
        text = vuz2_request(vuz2_list[user_id])
        await message.answer(text)
    else:
        text = 'К сожалению😢\nВы не можете посмотреть свои баллы через меня 🚫\n' \
               '🔮Обратитесь к моему <b><i>создателю @olider_db</i></b>, чтобы получить <b><i>доступ</i></b>☑️'
        await message.answer(text)
