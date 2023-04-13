from aiogram import Router
from aiogram.filters import Text

from bot.callbacks.help_message.chatgpt_help import send_ChatGPT_help
from bot.callbacks.help_message.schedule_commands import send_schedule_commands
from bot.callbacks.help_message.vuz2_rating_commands import send_vuz2_rating_commands


def reg_help_message_callbacks(router: Router):
    router.callback_query.register(send_ChatGPT_help, Text('chatgpt_help'))
    router.callback_query.register(send_schedule_commands, Text('schedule_help'))
    router.callback_query.register(send_vuz2_rating_commands, Text('rating_help'))
