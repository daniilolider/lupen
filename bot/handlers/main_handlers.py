from bot.handlers.user.main_user import reg_user_handlers
from bot.handlers.creator.main_creator import reg_creator_handlers
from bot.handlers.other.main_other import reg_other_handlers


def reg_all_handlers():
    reg_user_handlers()
    reg_creator_handlers()
    reg_other_handlers()