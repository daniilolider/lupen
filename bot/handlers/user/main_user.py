from bot.handlers.user.commands.main_user_commands import reg_user_commands
from bot.handlers.user.texts.main_user_texts import reg_user_texts
from bot.routers import routers


def reg_user_handlers():
    reg_user_texts(routers.user_texts_router)

    reg_user_commands(routers.user_commands_router)