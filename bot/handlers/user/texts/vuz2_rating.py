from aiogram.types import Message

from bot.keyboards.Inline.vyz2_rating import vuz2_keyboard
from bot.filters.vuz2_users_filter.vuz2_users_filter import vuz2_users_filter


async def txt_vuz2_rating(message: Message):
    """Выводит сообщение с инлайн кнопками по рейтингу"""

    if vuz2_users_filter(message):
        text = '🏆<b>Выберите, что конкретно интересует:</b>'
        await message.answer(text, reply_markup=vuz2_keyboard())
    else:
        text = 'К сожалению😢\nВы не можете посмотреть свои баллы через меня 🚫\n' \
               '🔮Обратитесь к моему <b><i>создателю @olider_db</i></b>, чтобы получить <b><i>доступ</i></b>☑️'
        await message.answer(text)
