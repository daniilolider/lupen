from aiogram.types import CallbackQuery


async def send_schedule_commands(callback: CallbackQuery):
    """Отправляет команды Расписание"""

    schedule_help_text = '<b>🗓Команды <u>Расписаниe</u></b>:\n\n' \
                         '' \
                         '<i>☝️Каждой команде в этом разделе есть альтернатива в виде</i> <b>кнопки</b>, ' \
                         '<i>в соответствующем разделе, а также</i> ' \
                         '<b>русский</b><i> и </i><b>сокращенный вариант</b> команд\n\n' \
                         '' \
                         '✦<b><i><u>/week_position</u></i></b> - Выводят позицию недели (верхняя/нижняя)\n' \
                         '<b><i>/позиция, /поз</i></b>\n\n' \
                         '' \
                         '✦<b><i><u>/monday</u></i></b> - Выводят расписание на понедельник\n' \
                         '<b><i>/понедельник, /пн</i></b>\n\n' \
                         '' \
                         '✦<b><i><u>/tuesday</u></i></b> - Выводят расписание на вторник\n' \
                         '<b><i>/вторник, /вт</i></b>\n\n' \
                         '' \
                         '✦<b><i><u>/wednesday</u></i></b> - Выводят расписание на среду\n' \
                         '<b><i>/среда, /ср</i></b>\n\n' \
                         '' \
                         '✦<b><i><u>/thursday</u></i></b> - Выводят расписание на четверг\n' \
                         '<b><i>/четверг, /чт\n\n</i></b>' \
                         '' \
                         '✦<b><i><u>/friday</u></i></b> - Выводят расписание на пятницу\n' \
                         '<b><i>/пятница, /пт</i></b>\n\n' \
                         '' \
                         '✦<b><i><u>/week</u></i></b> - Выводят расписание на всю неделю\n' \
                         '<b><i>/неделя, /нед</i></b>\n\n' \
                         '' \
                         '✦<b><i><u>/down_week</u></i></b> - Выводят расписание на нижнюю неделю\n' \
                         '<b><i>/нижняя_неделя, /ннед</i></b>\n\n' \
                         '' \
                         '✦<b><i><u>/up_week</u></i></b> - Выводят расписание на верхнюю неделю\n' \
                         '<b><i>/верхняя_неделя, /внед</i></b>\n\n' \
                         '' \
                         '✦<b><i><u>/photo_schedule</u></i></b> - Выводит фото расписания на всю неделю\n' \
                         '<b><i>/фото_расписания, /фр</i></b>\n\n' \
                         '' \
                         '✦<b><i><u>/now_couple</u></i></b> - Выводит, какая сейчас пара\n' \
                         '<b><i>/сейчас_пара, /сп</i></b>'

    await callback.message.answer(schedule_help_text)
