from aiogram import Router
from aiogram.filters import Command

from .start import cmd_start
from .help import cmd_help


def reg_user_commands(router: Router):
    router.message.register(cmd_start, Command('start', prefix='/!'))
    router.message.register(cmd_help, Command('help', prefix='/!'))