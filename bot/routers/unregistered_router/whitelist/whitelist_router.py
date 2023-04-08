from aiogram import Router

from bot.filters.user_level_filters.whitelist_filter import whitelist_check
from bot.routers.unregistered_router.unregistered_router import unregistered_router


whitelist_router = Router(name='WhitelistRouter')
unregistered_router.include_routers(whitelist_router)
whitelist_router.message.filter(whitelist_check)
