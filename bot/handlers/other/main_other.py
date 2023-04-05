from aiogram import Dispatcher
from aiogram.dispatcher.filters import Command

from bot.handlers.other import other


def register_other_handlers(dp: Dispatcher) -> None:

    # region commands

    dp.register_message_handler(other.chat_id, Command(['chat_id']))
    # handler....

    # endregion

    # region texts

    dp.register_message_handler(other.echo, content_types=['text'])
    # handler....

    # endregion
