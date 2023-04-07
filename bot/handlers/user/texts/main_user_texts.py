from aiogram import Router
from aiogram.filters import Text

from .help_message import text_help
from .menu import text_menu
from .schedule_message import text_schedule


def reg_user_texts(router: Router):
    router.message.register(text_help, Text('❔Помощь'))
    router.message.register(text_menu, Text('📓Меню'))
    router.message.register(text_schedule, Text('📋Расписание'))
