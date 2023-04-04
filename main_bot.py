from aiogram import Dispatcher, Bot
from aiogram.utils import executor

from bot.misc.env import TOKENS
from bot.handlers.main_handlers import register_all_handlers
from bot.data.database.main_database import register_all_database


async def __on_starup(dp: Dispatcher) -> None:
    register_all_database()
    register_all_handlers(dp)
    print('Online')


def start_bot():
    bot = Bot(token=TOKENS.mathurai_TOKEN, parse_mode='html')
    dp = Dispatcher(bot)
    executor.start_polling(dp, skip_updates=True, on_startup=__on_starup)
