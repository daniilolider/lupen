from aiogram import Router
from aiogram.filters import Command

from .chat_id import cmd_chat_id
from .add_whitelist import cmd_add_whitelist
from .delete_whitelist import cmd_delete_whitelist


def reg_creator_commands(router: Router):
    router.message.register(cmd_chat_id, Command('chat_id'))
    router.message.register(cmd_add_whitelist, Command('add_whitelist'))
    router.message.register(cmd_delete_whitelist, Command('delete_whitelist'))
