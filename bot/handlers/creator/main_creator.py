from bot.routers.routers import creator_router
from .commands.main_creator_commands import reg_creator_commands


def reg_creator_handlers():
    reg_creator_commands(creator_router)