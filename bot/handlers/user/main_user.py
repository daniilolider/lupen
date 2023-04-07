from bot.handlers.user.commands.main_user_commands import reg_user_commands
from bot.handlers.user.texts.main_user_texts import reg_user_texts
from bot.routers.user.user_router import user_texts_router, user_commands_router


def reg_user_handlers():
    reg_user_texts(user_texts_router)
    reg_user_commands(user_commands_router)
