from aiogram import Router

from bot.filters.user_level_filters.creator_filter import creator_check

creator_router = Router()
creator_router.message.filter(creator_check)
