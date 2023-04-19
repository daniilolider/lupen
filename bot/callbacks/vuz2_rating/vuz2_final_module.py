from aiogram.types import CallbackQuery

from bot.modules.vuz2rating.vuz2_request import vuz2_request


async def send_vuz2_final_module(callback: CallbackQuery):
    """Выводит строку итоговый модуль из таблицы рейтинга vuz2"""
    text = vuz2_request(callback.from_user.id, 'Итоговый модуль')
    await callback.message.answer(text)
