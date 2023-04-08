from aiogram import Router

from bot.routers.unregistered_router.whitelist.whitelist_router import whitelist_router


user_commands_router = Router(name='UserCommandsRouter')
whitelist_router.include_router(user_commands_router)
