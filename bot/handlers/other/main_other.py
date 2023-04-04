from aiogram import Dispatcher

from bot.handlers.other.other import other_echo


def register_other_handlers(dp: Dispatcher) -> None:

    # region commands

    # handler....
    # handler....

    # endregion

    # region texts

    dp.register_message_handler(other_echo, content_types=['text'])
    # handler....

    # endregion
