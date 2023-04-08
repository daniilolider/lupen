from aiogram import Router, F

from bot.filters.user_level_filters.creator_filter import creator_check

creator_router = Router(name='CreatorRouter')
creator_router.message.filter(creator_check)
