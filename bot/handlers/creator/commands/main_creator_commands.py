from aiogram import Router
from aiogram.filters import Command

from .chat_id import cmd_chat_id
from .add_whitelist import cmd_add_whitelist
from .delete_whitelist import cmd_delete_whitelist
from .creator_help import cmd_help_creator
from .add_whitelist_by_id import cmd_add_whitelist_by_id
from .delete_whitelist_by_id import cmd_delete_whitelist_by_id
from .vuz2_rating_add import cmd_add_rating_whitelist
from .vuz2_rating_delete import cmd_delete_rating_whitelist


def reg_creator_commands(router: Router):
    router.message.register(cmd_chat_id, Command('chat_id', prefix='/!'))
    router.message.register(cmd_add_whitelist, Command('add_whitelist', prefix='/!'))
    router.message.register(cmd_delete_whitelist, Command('delete_whitelist', prefix='/!'))
    router.message.register(cmd_help_creator, Command('help_creator', prefix='/!'))
    router.message.register(cmd_add_whitelist_by_id, Command('add_id_whitelist', prefix='/!'))
    router.message.register(cmd_delete_whitelist_by_id, Command('delete_id_whitelist', prefix='/!'))
    router.message.register(cmd_add_rating_whitelist, Command('add_rating_whitelist', prefix='/!'))
    router.message.register(cmd_delete_rating_whitelist, Command('delete_rating_whitelist', prefix='/!'))
