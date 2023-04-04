from aiogram import Dispatcher
from aiogram.dispatcher.filters import Command

from bot.handlers.admin.commands.adminhelp import cmd_adminhelp
from bot.handlers.admin.commands.add_whitelist import cmd_add_whitelist


def register_admin_handlers(dp: Dispatcher) -> None:

    # region commands

    dp.register_message_handler(cmd_adminhelp, Command(commands=['adminhelp']))
    dp.register_message_handler(cmd_add_whitelist, Command(commands=['add_whitelist']))

    # endregion

    # region texts

    # handler....
    # handler....

    # endregion
