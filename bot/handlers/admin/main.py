from aiogram import Dispatcher
from bot.handlers.admin.commands.adminhelp import cmd_adminhelp


def register_admin_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(cmd_adminhelp, commands=['adminhelp'])
