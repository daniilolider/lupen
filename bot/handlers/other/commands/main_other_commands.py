from aiogram import Dispatcher
from aiogram.filters import Command

from .my_id import cmd_my_id


def reg_other_commands(dp: Dispatcher):
    dp.message.register(cmd_my_id, Command('my_id'))
