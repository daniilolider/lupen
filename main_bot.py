from aiogram import Dispatcher, Bot

from bot.misc.env import KEYS




from bot.callbacks.main_callbacks import reg_all_callbacks
from bot.handlers.main_handlers import reg_all_handlers


from bot.routers.routers import user_commands_router, user_texts_router
from bot.routers.routers import creator_router





async def start_bot():
    bot = Bot(token=KEYS.mathurai_TOKEN, parse_mode='html')
    dp = Dispatcher()

    dp.include_routers(user_commands_router,
                       user_texts_router,
                       creator_router)


    reg_all_handlers()
    reg_all_callbacks(user_texts_router)

    print('Online!')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
