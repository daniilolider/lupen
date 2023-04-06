from aiogram import Dispatcher, Bot

from bot.misc.env import KEYS

from bot.handlers.user.commands.user_commands import user_router
from bot.handlers.creator.creatorcommands import creator_router


async def start_bot():
    bot = Bot(token=KEYS.mathurai_TOKEN, parse_mode='html')
    dp = Dispatcher()

    dp.include_routers(user_router,
                       creator_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
