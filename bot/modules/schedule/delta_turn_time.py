import datetime

from .couple_constants import FIRTS_START, SECOND_START, THIRD_START, FOURTH_START, FIFTH_START


def delta_turn_time(number_of_couple: int):
    """Считает, сколько оcталось до конца соответствующей перемены"""

    turns = {0: FIRTS_START, 1: SECOND_START, 2: THIRD_START, 3: FOURTH_START, 4: FIFTH_START}

    now = datetime.datetime.now()

    turn_hour = turns[number_of_couple].hour
    turn_minutes = turns[number_of_couple].minute

    delta = str(datetime.datetime(now.year, now.month, now.day, turn_hour, turn_minutes) - now)

    return delta[: -7]
