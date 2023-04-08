from bot.callbacks.help_message.main_callbacks import reg_help_message_callbacks
from bot.routers.callback.callback_router import callback_router


def reg_all_callbacks():
    reg_help_message_callbacks(callback_router)