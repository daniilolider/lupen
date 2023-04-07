from aiogram.types import CallbackQuery


async def send_schedule_command(callback: CallbackQuery):
    """Отправляет команды пункта меню Расписание"""

    schedule_help_text = 'ТУТ ДОЛЖНЫ БЫТЬ КОМАНДЫ РАСПИСАНИЯ\nмб с кнопкой назад'

    await callback.message.answer(schedule_help_text)