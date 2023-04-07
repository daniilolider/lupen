from aiogram import Router
from aiogram.filters import Text

from .chatgpt_callback import send_chat_gpt
from .schedule_callback import send_schedule_command


def reg_all_callbacks(router: Router):
    router.callback_query.register(send_chat_gpt, Text('chatgpt'))

    router.callback_query.register(send_schedule_command, Text('schedule'))