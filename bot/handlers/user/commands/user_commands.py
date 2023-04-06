from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command

from bot.filters.commands_filters import commands_filters


user_router = Router()
user_router.message.filter(commands_filters.whitelist_check)


@user_router.message(Command('start'))
async def cmd_start(message: Message) -> None:
    """Команда /start"""
    from bot.keyboards.start_bot import start_menu_kb

    start_text = 'Помогите мне! Эти изверги держат меня в заложниках!\n\n' \
                 'Хаха, шучу :) Я бот-помогатор студентов группы ПМР.\n\n' \
                 'Напишите /help или нажмите на соответсвующую кнопку,' \
                 ' чтобы узнать, чему меня научили\n' \
                 '(текст нужно допилить будет: отредачить и добавить смайлики)'

    await message.answer(start_text, reply_markup=start_menu_kb())
