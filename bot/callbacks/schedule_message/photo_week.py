from aiogram.types import CallbackQuery


async def photo_week(callback: CallbackQuery):
    """Выводит фотку всего расписания"""
    await callback.message.answer('🖼<u><b>Фотка расписания:</b></u>')
    await callback.message.answer_photo('https://disk.yandex.com.am/i/5_8UOoPCwhqqkA')
