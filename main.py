from aiogram import Dispatcher, Bot
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.misc.env import TOKENS
from bot.handlers.main import register_all_handlers


async def __on_starup(dp: Dispatcher) -> None:
    register_all_handlers(dp)
    print('Online')


def start_bot():
    bot = Bot(token=TOKENS.mathurai_TOKEN, parse_mode='html')
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_starup)
