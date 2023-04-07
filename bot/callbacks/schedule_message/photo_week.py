from aiogram.types import CallbackQuery


async def photo_week(callback: CallbackQuery):
    """Выводит фотку всего расписания"""

    await callback.message.answer('Фотка расписания:')
    await callback.message.answer_photo('https://disk.yandex.ru/i/GmUJu3KXc3q3sQ')
