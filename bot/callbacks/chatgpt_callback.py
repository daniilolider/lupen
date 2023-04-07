from aiogram.types import CallbackQuery


async def send_chat_gpt(callback: CallbackQuery):
    """Отправляет команды пункта меню ChatGPT"""

    schedule_help_text = 'ТУТ ДОЛЖНЫ БЫТЬ КОМАНДЫ ЧАТ БОТА\nмб с кнопкой назад'

    await callback.message.answer(schedule_help_text)