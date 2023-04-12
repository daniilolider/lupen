from aiogram.types import CallbackQuery

from bot.modules.vuz2rating.vuz2_request import vuz2_request


async def vuz2_first_module(callback: CallbackQuery):
    """Выводит строку первый модуль из таблицы рейтинга vuz2"""
    text = vuz2_request(callback.message.chat.id, 3)
    await callback.message.answer(text)
