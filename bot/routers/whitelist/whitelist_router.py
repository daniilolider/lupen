from aiogram import Router

from bot.filters.user_level_filters.whitelist_filter import whitelist_check


whitelist_router = Router()
whitelist_router.message.filter(whitelist_check)
