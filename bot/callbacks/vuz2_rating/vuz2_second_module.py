from aiogram.types import CallbackQuery

from bot.modules.vuz2rating.vuz2_request import vuz2_request


async def send_vuz2_second_module(callback: CallbackQuery):
    """Выводит строку второй модуль из таблицы рейтинга vuz2"""
    text = vuz2_request(callback.from_user.id, '2-ой модуль')
    await callback.message.answer(text)
