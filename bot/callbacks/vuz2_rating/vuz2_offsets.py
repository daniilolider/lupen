from aiogram.types import CallbackQuery

from bot.modules.vuz2rating.vuz2_request import vuz2_request


async def send_vuz2_offsets(callback: CallbackQuery):
    """Выводит строку зачёты из таблицы рейтинга vuz2"""
    text = vuz2_request(callback.from_user.id, 1)
    await callback.message.answer(text)
