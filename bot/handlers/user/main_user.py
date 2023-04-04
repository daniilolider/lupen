from aiogram import Dispatcher

from bot.handlers.user.texts.hello import txt_hello


def register_user_handlers(dp: Dispatcher) -> None:

    # region commands

    # handler....
    # handler....

    # endregion

    # region texts

    dp.register_message_handler(txt_hello, text='привет')
    # handler....

    # endregion
