from aiogram import Dispatcher
from aiogram.filters import Command

from .my_id import my_id


def reg_other_commands(dp: Dispatcher):
    dp.message.register(my_id, Command('my_id'))
