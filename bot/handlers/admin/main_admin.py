from aiogram import Dispatcher
from aiogram.dispatcher.filters import Command

from .commands import admincommands


def register_admin_handlers(dp: Dispatcher) -> None:

    # region commands

    dp.register_message_handler(admincommands.cmd_adminhelp, Command(['adminhelp']))
    dp.register_message_handler(admincommands.cmd_addwhitelist, Command(['addwhitelist']))

    # endregion

    # region texts

    # handler....
    # handler....

    # endregion
