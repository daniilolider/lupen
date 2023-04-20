from aiogram.types import CallbackQuery

from bot.modules.vuz2rating.vuz2_request import vuz2_request


async def send_vuz2_passes(callback: CallbackQuery):
    """Выводит пропуски из vuz2"""
    text = vuz2_request(callback.from_user.id, 'passes')
    await callback.message.answer(text)
