from aiogram.types import Message

from bot.filters.vuz2_users_filter.vuz2_users_filter import vuz2_users_filter
from bot.modules.vuz2rating.vuz2_request import vuz2_request


async def cmd_vuz2_rating_first_module(message: Message):
    """Выводит строку первый модуль из таблицы рейтинга vuz2"""

    if vuz2_users_filter(message):
        text = vuz2_request(message.from_user.id, '1-ый модуль')
    else:
        text = 'К сожалению😢\nВы не можете посмотреть свои баллы через меня 🚫\n' \
               '🔮Обратитесь к моему <b><i>создателю @olider_db</i></b>, чтобы получить <b><i>доступ</i></b>☑️'

    await message.answer(text)
