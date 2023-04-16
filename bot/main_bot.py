import logging
import openai
from aiogram import Dispatcher, Bot


from bot.misc.env import KEYS

from bot.routers.unregistered_router.unregistered_router import unregistered_router
from bot.routers.creator.creator_router import creator_router

from bot.callbacks.main_callbacks import reg_all_callbacks
from bot.handlers.main_handlers import reg_all_handlers


async def start_bot():

    logging.basicConfig(level=logging.INFO,
                        filename='logs.log',
                        format='[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s',
                        datefmt='%H:%M:%S',
                        filemode='w')

    openai.api_key = KEYS.chatgpt_TOKEN

    bot = Bot(token=KEYS.lupen_TOKEN, parse_mode='html')
    dp = Dispatcher()

    dp.include_routers(unregistered_router, creator_router)

    reg_all_handlers()
    reg_all_callbacks()

    print('Online!')
    await bot.send_message(KEYS.creator_ID, 'Online!')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
