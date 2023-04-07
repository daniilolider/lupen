from aiogram.types import Message


async def text_menu(message: Message):
    """Выводит кнопки меню"""
    from bot.keyboards.Reply.main_menu import main_menu

    await message.answer('С чем я могу вам помочь? 😇', reply_markup=main_menu())
