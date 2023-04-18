import datetime

from bot.data.schedule.couple_constants import up_week, down_week
from .time_interval import time_interval
from .week_position import WEEK_POSITION
from .event_remains import event_remains


def what_couple_now():
    """Опредяет что должно выводится в определённый промежуток времени"""
    week = (up_week, down_week)[WEEK_POSITION]  # Наша неделя, верхняя/нижняя
    now = datetime.datetime.now().time()  # Время, когда вызвали функцию
    up_or_down = "⬇️<i>Нижняя неделя</i>⬇️" if WEEK_POSITION else "⬆️<i>Верхняя неделя</i>⬆️"

    # weekday - день недели
    # lesson_status - пара или перемена. True - пара, False - перемена
    # lesson_number - номер пары или перемены
    weekday, lesson_status, lesson_number = time_interval(now)

    date = datetime.datetime.now().date().strftime('%d.%m.%Y')  # Сегодняшняя дата

    # Дни недели
    weekdays = {0: 'понедельник',
                1: 'вторник',
                2: 'среда',
                3: 'четверг',
                4: 'пятница',
                5: 'суббота',
                6: 'воскресенье'}

    # Если сейчас выходные (суббота или воскресенье) ИЛИ сейчас пятница и это конец дня (закончилась пятая пара)
    if lesson_status == 'weekend' or (weekday == 4 and lesson_status == 'day_end'):

        result = '\n'.join(week[0])

        text = f'💤Сейчас {"уже" if weekday == 4 else ""} выходной {date} <b>{weekdays[weekday]}</b>\n' \
               f'{up_or_down}\n\n' \
               '📄<b><u>Следующие пары будут только в понедельник:</u></b>\n' \
               f'{result}'

        return text

    # Если сейчас утро
    elif lesson_status == 'morning':

        mornings = {0: 'понедельника', 1: 'вторника', 2: 'среды', 3: 'четверга', 4: 'пятницы'}

        result = '\n'.join(week[weekday])

        text = f'☀️Сейчас утро <b>{mornings[weekday]}</b> {date}\n' \
               f'{up_or_down}\n\n' \
               f'📄<u><b>Сегодня такие пары:</b></u>\n' \
               f'{result}'

        return text

    # Если сейчас пара
    elif lesson_status == 'lesson':

        text = f'📆Сейчас <b>{weekdays[weekday]}</b> {date}\n' \
               f'{up_or_down}\n\n'

        if lesson_number == 0:
            text += f'✏️Сейчас:{week[weekday][0]}\n' \
                    f'⏳Осталось: <i>{event_remains(lesson_number, lesson_status)}</i>\n' \
                    f'▶️Будет:{week[weekday][1]}'

        elif lesson_number == 4:
            text += f'◀️Была:{week[weekday][lesson_number - 1]}\n' \
                    f'✏️Сейчас:{week[weekday][lesson_number]}'

        else:
            text += f'◀️Была:{week[weekday][lesson_number - 1]}\n' \
                    f'✏️Сейчас:{week[weekday][lesson_number]}\n' \
                    f'⏳Осталось: <i>{event_remains(lesson_number, lesson_status)}</i>\n' \
                    f'▶️Будет:{week[weekday][lesson_number + 1]}'

        return text

    # Если сейчас перемена
    elif lesson_status == 'turn':

        text = f'📆Сейчас <b>{weekdays[weekday]}</b> {date}\n' \
               f'{up_or_down}\n\n'

        if lesson_number == 0:
            text += f'▶️Будет:{week[weekday][0]}'

        elif lesson_number == 4:
            text += f'◀️Была:{week[weekday][lesson_number]}\n' \
                    f'✏️Сейчас: 🔚<i>Учеба уже закончилась</i>'
        else:
            text += f'◀️Была:{week[weekday][lesson_number - 1]}\n' \
                    f'✏️Сейчас: 🤟<i>Перемена</i>\n' \
                    f'⏳Осталось: <i>{event_remains(lesson_number, lesson_status)}</i>\n' \
                    f'▶️Будет:{week[weekday][lesson_number]}'

        return text

    # Если пары уже закончились
    elif lesson_status == 'day_end':

        result = '\n'.join(week[weekday + 1])

        text = f'📆Сейчас <b>{weekdays[weekday]}</b> {date}\n' \
               f'{up_or_down}\n\n' \
               f'🔚Учеба закончилась🔚\n\n' \
               f'📄<u><b>Пары на следующий день:</b></u>\n' \
               f'{result}'

        return text
