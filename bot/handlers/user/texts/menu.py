from aiogram.types import Message

from bot.keyboards.Reply.main_menu import main_menu


async def text_menu(message: Message):
    """Выводит кнопки меню"""

    text = '<b>⚜️Выберите, чем хотите воспользоваться</b>'

    await message.answer(text, reply_markup=main_menu())
