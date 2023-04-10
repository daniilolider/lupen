from aiogram import Router
from aiogram.filters import Text

from .help_message import text_help
from .menu import text_menu
from .schedule_message import text_schedule
from .what_couple_message import txt_what_couple


def reg_user_texts(router: Router):
    router.message.register(text_help, Text('❔Помощь'))
    router.message.register(text_menu, Text('📓Меню'))
    router.message.register(text_schedule, Text('📋Расписание'))
    router.message.register(txt_what_couple, Text('❓Какая сейчас пара?❔'))
