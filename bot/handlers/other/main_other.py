from bot.routers.unregistered_router.unregistered_router import unregistered_router
from .commands.main_other_commands import reg_other_commands


def reg_other_handlers():
    reg_other_commands(unregistered_router)