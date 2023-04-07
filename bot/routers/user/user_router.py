from aiogram import Router

from bot.routers.whitelist.whitelist_router import whitelist_router


user_texts_router = Router()
whitelist_router.include_router(user_texts_router)

user_commands_router = Router()
whitelist_router.include_router(user_commands_router)
