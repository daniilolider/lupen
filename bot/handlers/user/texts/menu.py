from aiogram.types import Message


async def text_menu(message: Message):
    """Выводит кнопки меню"""
    from bot.keyboards.main_menu import main_menu

    await message.answer('Вот что сейчас доступно', reply_markup=main_menu())
