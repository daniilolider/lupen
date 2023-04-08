from aiogram import Router
from aiogram.filters import Text

from bot.callbacks.help_message.chatgpt_callback import send_chat_gpt
from bot.callbacks.help_message.schedule_callback import send_schedule_command


def reg_help_message_callbacks(router: Router):
    router.callback_query.register(send_chat_gpt, Text('chatgpt'))
    router.callback_query.register(send_schedule_command, Text('schedule'))
