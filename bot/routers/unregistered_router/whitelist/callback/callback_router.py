from aiogram import Router

from bot.routers.unregistered_router.whitelist.whitelist_router import whitelist_router


callback_router = Router(name='CallbackRouter')
whitelist_router.include_router(callback_router)
