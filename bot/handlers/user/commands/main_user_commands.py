from aiogram import Router
from aiogram.filters import Command

from bot.handlers.user.commands.other.start import cmd_start
from bot.handlers.user.commands.other.help import cmd_help
from bot.handlers.user.commands.schedule.week_position import cmd_week_position
from bot.handlers.user.commands.schedule.days_schedule import cmd_monday, cmd_tuesday, cmd_wednesday, cmd_thursday, cmd_friday
from bot.handlers.user.commands.schedule.weeks_schedule import cmd_week, cmd_down_week, cmd_up_week
from bot.handlers.user.commands.schedule.photo_week import cmd_photo_week
from bot.handlers.user.commands.schedule.what_couple_now import cmd_now_couple
from bot.filters.ChatGPT_filter.ChatGPT_messag_filter import chatgpt_message_filter
from bot.handlers.user.commands.ChatGPT.ChatGPT_reply import cmd_chatgpt_message
from bot.handlers.user.commands.vuz2_rating.vuz2_rating_exams import cmd_vuz2_rating_exams
from bot.handlers.user.commands.vuz2_rating.vuz2_rating_offsets import cmd_vuz2_rating_offsets
from bot.handlers.user.commands.vuz2_rating.vuz2_rating_first_module import cmd_vuz2_rating_first_module
from bot.handlers.user.commands.vuz2_rating.vuz2_rating_second_module import cmd_vuz2_rating_second_module
from bot.handlers.user.commands.vuz2_rating.vuz2_rating_final_module import cmd_vuz2_rating_final_module
from bot.handlers.user.commands.other.return_keyboard import cmd_return_keyboard


def reg_user_commands(router: Router):
    router.message.register(cmd_start, Command('start', 'начало', prefix='/!'))

    router.message.register(cmd_help, Command('help', 'помощь', prefix='/!'))

    router.message.register(cmd_week_position, Command('week_position', 'позиция', 'поз', prefix='/!'))

    router.message.register(cmd_monday, Command('monday', 'понедельник', 'пн', prefix='/!'))
    router.message.register(cmd_tuesday, Command('tuesday', 'вторник', 'вт', prefix='/!'))
    router.message.register(cmd_wednesday, Command('wednesday', 'среда', 'ср', prefix='/!'))
    router.message.register(cmd_thursday, Command('thursday', 'четверг', 'чт', prefix='/!'))
    router.message.register(cmd_friday, Command('friday', 'пятница', 'пт', prefix='/!'))

    router.message.register(cmd_week, Command('week', 'неделя', 'нед', prefix='/!'))
    router.message.register(cmd_down_week, Command('down_week', 'нижняя_неделя', 'ннед', prefix='/!'))
    router.message.register(cmd_up_week, Command('up_week', 'верхняя_неделя', 'внед', prefix='/!'))

    router.message.register(cmd_photo_week, Command('photo_schedule', 'фото_расписания', 'фр', prefix='/!'))

    router.message.register(cmd_now_couple, Command('now_couple', 'сейчас_пара', 'сп', prefix='/!'))

    router.message.register(cmd_chatgpt_message,
                            chatgpt_message_filter,
                            Command('q', '?', prefix='/!'),
                            flags={'long_operation': 'typing'})

    router.message.register(cmd_vuz2_rating_exams, Command('vuz2_exams', 'экзамены', 'экзы', prefix='/!'))
    router.message.register(cmd_vuz2_rating_offsets, Command('vuz2_offsets', 'зачеты', 'зчт', prefix='/!'))
    router.message.register(cmd_vuz2_rating_first_module,
                            Command('vuz2_first_module', 'первый_модуль', 'пм', prefix='/!'))
    router.message.register(cmd_vuz2_rating_second_module,
                            Command('vuz2_second_module', 'второй_модуль', 'вм', prefix='/!'))
    router.message.register(cmd_vuz2_rating_final_module,
                            Command('vuz2_final_module', 'итоговый_модуль', 'им', prefix='/!'))

    router.message.register(cmd_return_keyboard, Command('return_keyboard', 'rk', prefix='/!'))
