from bot.routers.unregistered_router.whitelist.callback.callback_router import callback_router
from bot.callbacks.help_message.main_help import reg_help_message_callbacks
from bot.callbacks.schedule_message.main_schedule import reg_schedule_message_callbacks


def reg_all_callbacks():
    reg_help_message_callbacks(callback_router)
    reg_schedule_message_callbacks(callback_router)
