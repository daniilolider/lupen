from aiogram import Router
from aiogram.filters import Text

from bot.callbacks.schedule_message.week_position import week_position
from bot.callbacks.schedule_message.days import monday, tuesday, wednesday, thursday, friday
from bot.callbacks.schedule_message.weeks import week, down_week, up_week
from bot.callbacks.schedule_message.photo_week import photo_week
from bot.callbacks.schedule_message.now_couple import now_couple


def reg_schedule_message_callbacks(router: Router):
    router.callback_query.register(week_position, Text('week_position'))
    router.callback_query.register(monday, Text('monday_schedule'))
    router.callback_query.register(tuesday, Text('tuesday_schedule'))
    router.callback_query.register(wednesday, Text('wednesday_schedule'))
    router.callback_query.register(thursday, Text('thursday_schedule'))
    router.callback_query.register(friday, Text('friday_schedule'))
    router.callback_query.register(week, Text('week_schedule'))
    router.callback_query.register(down_week, Text('down_week_schedule'))
    router.callback_query.register(up_week, Text('up_week_schedule'))
    router.callback_query.register(photo_week, Text('photo_week_schedule'))
    router.callback_query.register(now_couple, Text('now_couple'))
