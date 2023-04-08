from aiogram import Router
from aiogram.filters import Text

from .help_message import text_help
from .menu import text_menu


def reg_user_texts(router: Router):
    router.message.register(text_help, Text('❔Помощь'))
    router.message.register(text_menu, Text('📓Меню'))
