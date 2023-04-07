# !!!!!!!!!!!!!!!!!СДЕЛАТЬ НЕ В ОДНОМ ФАЙЛЕ!!!!!!!!!!!!!!!!!!!
from aiogram import Router

from bot.filters.commands_filters.commands_filters import whitelist_check, creator_check

whitelist_router = Router()
whitelist_router.message.filter(whitelist_check)


user_texts_router = Router()
user_texts_router.message.filter(whitelist_check)

user_commands_router = Router()
user_commands_router.message.filter(whitelist_check)


creator_router = Router()
creator_router.message.filter(creator_check)
