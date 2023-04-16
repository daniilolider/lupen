from aiogram import Router
from aiogram.filters import Command

from bot.handlers.creator.commands.other.chat_id import cmd_chat_id
from bot.handlers.creator.commands.whitelist.add_whitelist import cmd_add_whitelist
from bot.handlers.creator.commands.whitelist.delete_whitelist import cmd_delete_whitelist
from bot.handlers.creator.commands.other.creator_help import cmd_help_creator
from bot.handlers.creator.commands.whitelist.add_whitelist_by_id import cmd_add_whitelist_by_id
from bot.handlers.creator.commands.whitelist.delete_whitelist_by_id import cmd_delete_whitelist_by_id
from bot.handlers.creator.commands.vuz2_whitelist.vuz2_rating_add import cmd_add_rating_whitelist
from bot.handlers.creator.commands.vuz2_whitelist.vuz2_rating_delete import cmd_delete_rating_whitelist


def reg_creator_commands(router: Router):
    router.message.register(cmd_chat_id, Command('chat_id', prefix='/!'))
    router.message.register(cmd_add_whitelist, Command('add_whitelist', prefix='/!'))
    router.message.register(cmd_delete_whitelist, Command('delete_whitelist', prefix='/!'))
    router.message.register(cmd_help_creator, Command('help_creator', prefix='/!'))
    router.message.register(cmd_add_whitelist_by_id, Command('add_id_whitelist', prefix='/!'))
    router.message.register(cmd_delete_whitelist_by_id, Command('delete_id_whitelist', prefix='/!'))
    router.message.register(cmd_add_rating_whitelist, Command('add_rating_whitelist', prefix='/!'))
    router.message.register(cmd_delete_rating_whitelist, Command('delete_rating_whitelist', prefix='/!'))
