from aiogram import Router
from aiogram.filters import CommandStart

from .start import cmd_start


def reg_user_commands(router: Router):
    router.message.register(cmd_start, CommandStart)