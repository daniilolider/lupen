from aiogram import Router
from aiogram.filters import Text

from bot.handlers.user.texts.main_buttons.help_message import text_help
from bot.handlers.user.texts.main_buttons.menu import text_menu
from bot.handlers.user.texts.schedule.schedule_message import text_schedule
from bot.handlers.user.texts.schedule.what_couple_message import txt_what_couple
from bot.handlers.user.texts.ChatGPT.ChatGPT_questmessage import txt_chatgpt_questmessage
from bot.handlers.user.texts.vuz2_rating.vuz2_rating import txt_vuz2_rating
from bot.handlers.user.texts.keyboard_movement.remove_keyboard import txt_remove_keyboard
from bot.handlers.user.texts.keyboard_movement.return_keyboard_message import txt_return_keyboard
from bot.handlers.user.texts.top_secret.top_secret import txt_top_secret


def reg_user_texts(router: Router):
    router.message.register(text_help, Text('❔Помощь'))
    router.message.register(text_menu, Text('📓Меню'))
    router.message.register(text_schedule, Text('📋Расписание'))
    router.message.register(txt_what_couple, Text('❓Какая сейчас пара?❔'))
    router.message.register(txt_chatgpt_questmessage, Text('🤖Вопрос ChatGPT'))
    router.message.register(txt_vuz2_rating, Text('🔢Рейтинг'))
    router.message.register(txt_remove_keyboard, Text('⬇️Скрыть клавиатуру'))
    router.message.register(txt_return_keyboard, Text(['Вернуть кнопки', 'ВК']))
    router.message.register(txt_top_secret, Text(['Артём лох', 'Артем лох']))
