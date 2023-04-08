from aiogram import Router

from bot.routers.unregistered_router.whitelist.whitelist_router import whitelist_router


user_texts_router = Router(name='UserTextsRouter')
whitelist_router.include_router(user_texts_router)
