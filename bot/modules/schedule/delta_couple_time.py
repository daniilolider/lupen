import datetime

from .couple_constants import FIRST_END, SECOND_END, THIRD_END, FOURTH_END, FIFTH_END


def delta_couple_time(number_of_couple: int):
    """Считает, сколько оcталось до конца соответствующей пары"""

    couples = {0: FIRST_END, 1: SECOND_END, 2: THIRD_END, 3: FOURTH_END, 4: FIFTH_END}

    now = datetime.datetime.now()

    couple_hour = couples[number_of_couple].hour
    couple_minutes = couples[number_of_couple].minute

    delta = str(datetime.datetime(now.year, now.month, now.day, couple_hour, couple_minutes) - now)

    return delta[: -7]
