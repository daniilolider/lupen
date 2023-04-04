from aiogram import Dispatcher


from bot.handlers.admin.main_admin import register_admin_handlers
from bot.handlers.user.main_user import register_user_handlers
from bot.handlers.other.main_other import register_other_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_admin_handlers,
        register_user_handlers,
        register_other_handlers
    )

    for handler in handlers:
        handler(dp)
