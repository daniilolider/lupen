import datetime

from bot.data.schedule.couple_constants import FIRTS_START, SECOND_START, THIRD_START, FOURTH_START, FIFTH_START
from bot.data.schedule.couple_constants import FIRST_END, SECOND_END, THIRD_END, FOURTH_END, FIFTH_END


def event_remains(number_of_couple: int, event_status: str) -> str:
    """Считает, сколько оcталось до конца соответствующей пары или перемны"""

    if event_status == 'lesson':
        event = {0: FIRST_END, 1: SECOND_END, 2: THIRD_END, 3: FOURTH_END, 4: FIFTH_END}
    else:
        event = {0: FIRTS_START, 1: SECOND_START, 2: THIRD_START, 3: FOURTH_START, 4: FIFTH_START}

    now = datetime.datetime.now()

    event_hour = event[number_of_couple].hour
    event_minutes = event[number_of_couple].minute

    delta = str(datetime.datetime(now.year, now.month, now.day, event_hour, event_minutes) - now)

    return delta[: -7]
