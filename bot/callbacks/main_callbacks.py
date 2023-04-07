from bot.callbacks.help_message.main_callbacks import reg_help_message_callbacks
from bot.routers.whitelist.whitelist_router import whitelist_router


def reg_all_callbacks():
    reg_help_message_callbacks(whitelist_router)