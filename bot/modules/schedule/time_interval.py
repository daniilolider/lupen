import datetime

from bot.data.schedule.couple_constants import FIRTS_START, SECOND_START, THIRD_START, FOURTH_START, FIFTH_START, DAY_START
from bot.data.schedule.couple_constants import FIRST_END, SECOND_END, THIRD_END, FOURTH_END, FIFTH_END, DAY_END


def time_interval(now):
    """Определяет, какой сейчас день недели, какая пара или перемена по счёту и определяет идёт пара или перемена"""
    weekday = datetime.datetime.now().weekday()
    lesson_status = None
    lesson_number = 0

    if weekday == 5 or weekday == 6:  # Выходные
        lesson_status = 'weekend'

    elif DAY_START <= now < FIRTS_START:  # Утро любого дня
        lesson_status = 'morning'
        lesson_number = 0

    elif FIRTS_START <= now < FIRST_END:  # Первая пара
        lesson_status = 'lesson'
        lesson_number = 0

    elif FIRST_END <= now < SECOND_START:  # Первая перемена
        lesson_status = 'turn'
        lesson_number = 1

    elif SECOND_START <= now <= SECOND_END:  # Вторая пара
        lesson_status = 'lesson'
        lesson_number = 1

    elif SECOND_END <= now < THIRD_START:  # Вторая перемена
        lesson_status = 'turn'
        lesson_number = 2

    elif THIRD_START <= now < THIRD_END:  # Третья пара
        lesson_status = 'lesson'
        lesson_number = 2

    elif THIRD_END <= now < FOURTH_START:  # Третья перемена
        lesson_status = 'turn'
        lesson_number = 3

    elif FOURTH_START <= now < FOURTH_END:  # Четвертая пара
        lesson_status = 'lesson'
        lesson_number = 3

    elif FOURTH_END <= now < FIFTH_START:  # Четвертая перемена
        lesson_status = 'turn'
        lesson_number = 4

    elif FIFTH_START <= now < FIFTH_END:  # Пятая пара
        lesson_status = 'lesson'
        lesson_number = 4

    elif FIFTH_END <= now < DAY_END:  # Конец учёбы
        lesson_status = 'day_end'

    return weekday, lesson_status, lesson_number
