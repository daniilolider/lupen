from aiogram.types import Message

from bot.keyboards.Reply.main_menu import main_menu


async def cmd_return_keyboard(message: Message) -> None:
    """Возвращает клавиатуру"""
    await message.answer('👍Клавиатура возвращена', reply_markup=main_menu())
