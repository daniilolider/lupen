import datetime

from .couple_constants import up_week, down_week
from .time_interval import time_interval
from .week_position import WEEK_POSITION
from .delta_couple_time import delta_couple_time
from .delta_turn_time import delta_turn_time


def what_couple_now():
    """Опередяет что должно выводится в определённый промежуток времени"""

    week = (up_week, down_week)[WEEK_POSITION]  # Наша неделя, верхняя/нижняя
    now = datetime.datetime.now().time()  # Время, когда вызвали функцию

    # weekday - день недели
    # lesson_status - пара или перемена. True - пара, False - перемена
    # lesson_number - номер пары или перемены
    weekday, lesson_status, lesson_number = time_interval(now)

    date = datetime.datetime.now().date().strftime('%d.%m.%Y')  # Сегодняшняя дата
    # Дни недели
    weekdays = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг', 4: 'пятница', 5: 'суббота', 6: 'воскресенье'}

    # Если сейчас выходные (суббота или воскресенье) ИЛИ сейчас пятница и это конец дня (закончилась пятая пара)
    if lesson_status == 'weekend' or (weekday == 4 and lesson_status == 'day_end'):

        # Строка пар
        result = []
        for line in week[0]:
            result.append(line + '\n')
        result = ''.join(result)

        text = f'Сейчас {"уже" if weekday == 4 else ""} выходной {date} {weekdays[weekday]}\n' \
               f'{"Нижняя неделя" if WEEK_POSITION else "Верхняя неделя"}\n' \
               'Следующие пары будут только в понедельник:\n' \
               f'{result}'

        return text

    # Если сейчас утро
    elif lesson_status == 'morning':

        mornings = {0: 'понедельника', 1: 'вторника', 2: 'среды', 3: 'четверга', 4: 'пятницы'}

        # Строка пар
        result = []
        for line in week[weekday]:
            result.append(line + '\n')
        result = ''.join(result)

        text = f'Сейчас утро {mornings[weekday]} {date}\n' \
               f'{"Нижняя неделя" if WEEK_POSITION else "Верхняя неделя"}\n' \
               f'Сегодня такие пары:\n' \
               f'{result}'

        return text

    # Если сейчас пара
    elif lesson_status == 'lesson':

        text = f'Сейчас {weekdays[weekday]} {date}\n' \
               f'{"Нижняя неделя" if WEEK_POSITION else "Верхняя неделя"}\n\n'

        if lesson_number == 0:
            text += f'Сейчас - {week[weekday][0]}\n' \
                    f'Осталось {delta_couple_time(lesson_number)}\n' \
                    f'Будет - {week[weekday][1]}'

        elif lesson_number == 4:
            text += f'Была - {week[weekday][lesson_number - 1]}\n' \
                    f'Сейчас - {week[weekday][lesson_number]}'

        else:
            text += f'Была - {week[weekday][lesson_number - 1]}\n' \
                    f'Сейчас - {week[weekday][lesson_number]}\n' \
                    f'Осталось {delta_couple_time(lesson_number)}\n' \
                    f'Будет - {week[weekday][lesson_number + 1]}'

        return text

    # Если сейчас перемена
    elif lesson_status == 'turn':

        text = f'Сейчас {weekdays[weekday]} {date}\n' \
               f'{"Нижняя неделя" if WEEK_POSITION else "Верхняя неделя"}\n\n'

        if lesson_number == 0:
            text += f'Будет - {week[weekday][0]}'

        elif lesson_number == 4:
            text += f'Была - {week[weekday][lesson_number]}\n' \
                    f'Сейчас - учеба закончилась'
        else:
            text += f'Была - {week[weekday][lesson_number - 1]}\n' \
                    f'Сейчас - перемена\n' \
                    f'Осталось - {delta_turn_time(lesson_number)}\n' \
                    f'Будет - {week[weekday][lesson_number]}'

        return text

    # Если пары уже закончились
    elif lesson_status == 'day_end':

        # Строка пар
        result = []
        for line in week[weekday]:
            result.append(line + '\n')
        result = ''.join(result)

        text = f'Сейчас {weekdays[weekday]} {date}\n' \
               f'{"Нижняя неделя" if WEEK_POSITION else "Верхняя неделя"}\n\n' \
               f'Учеба уже закончилась\n' \
               f'Пары на следующий день:\n' \
               f'{result}'

        return text
