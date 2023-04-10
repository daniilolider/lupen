from aiogram import Router
from aiogram.filters import Command

from .start import cmd_start
from .help import cmd_help
from .week_position import cmd_week_position
from .days_schedule import cmd_monday, cmd_tuesday, cmd_wednesday, cmd_thursday, cmd_friday
from .weeks_schedule import cmd_week, cmd_down_week, cmd_up_week
from .photo_week import cmd_photo_week
from .what_couple_now import cmd_now_couple


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
