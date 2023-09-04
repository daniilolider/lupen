from datetime import time, datetime
import pytz


def utc_times(hours: int = 0, minutes: int = 0, seconds: int = 0, timezone_name: str = 'Europe/Minsk'):
    """Преобразует объект time по локальному поясу в time по UTC"""
    tz = pytz.timezone(timezone_name)
    utc_timezone = pytz.utc
    local_time = time(hours, minutes, seconds)
    _datetime = datetime.combine(datetime.today(), local_time)
    local_datetime = tz.localize(_datetime)
    return local_datetime.astimezone(utc_timezone).time()


# Первая пара
FIRTS_START = utc_times(8, 30)  # Начало
FIRST_END = utc_times(10, 5)  # Конец

# Вторая пара
SECOND_START = utc_times(10, 25)
SECOND_END = utc_times(12)

# Третья пара
THIRD_START = utc_times(12, 30)
THIRD_END = utc_times(14, 5)

# Четвертая пара
FOURTH_START = utc_times(14, 20)
FOURTH_END = utc_times(15, 55)

# Пятая пара
FIFTH_START = utc_times(16, 5)
FIFTH_END = utc_times(17, 40)

# Начало дня
DAY_START = utc_times(3, 0)

# Конец дня
DAY_END = utc_times(2, 59)


down_monday = [' <b>•</b> <i>Основы права</i> лекция <b>533</b>',
               ' <b>•</b> <i>Английский язык</i> <b>513</b>',
               ' <b>•</b> <i>Численный анализ</i> лекция <b>322</b>',
               ' <b>•</b> <i>СМС/ЧA</i> практики <b>233/405</b>',
               ' <b>✕</b> Пятой пары нет']

down_tuesday = [' <b>•</b> <i>Теория вероятности и случайные процессы</i> практика <b>407</b>',
                ' <b>•</b> <i>Физра</i>',
                ' <b>•</b> <i>Основы права</i> практика <b>549</b>',
                ' <b>•</b> <i>ОДУ</i> лекция <b>533</b>',
                ' <b>✕</b> Пятой пары нет']

down_wednesday = [' <b>•</b> <i>Численный анализ</i> практика <b>405</b> (первая группа)',
                  ' <b>•</b> <i>МатЛог и ТеорАлг</i> лекция <b>403 к4</b>',
                  ' <b>•</b> <i>Английский язык</i> <b>529</b>',
                  ' <b>•</b> <i>МатЛог и ТеорАлг</i> практика <b>549</b>',
                  ' <b>✕</b> Пятой пары нет']

down_thursday = [' <b>•</b> <i>Теория вероятности и случайные процессы</i> лекция <b>530</b>',
                 ' <b>•</b> <i>Современные математические системы</i> лекция <b>508</b>',
                 ' <b>•</b> <i>Философия</i> лекция <b>509</b>',
                 ' <b>•</b> <i>СМС</i> практика <b>233</b> (вторая группа)',
                 ' <b>✕</b> Пятой пары нет']

down_friday = [' <b>•</b> <i>Философия</i> практика <b>303</b>',
               ' <b>•</b> <i>ОДУ</i> практика <b>534</b>',
               ' <b>•</b> <i>Физра</i>',
               ' <b>✕</b> Четвёртой пары нет',
               ' <b>✕</b> Пятой пары нет']


up_monday = [' <b>✕</b> Первой пары нет',
             ' <b>•</b> <i>Английский язык</i> <b>513</b>',
             ' <b>•</b> <i>Численный анализ</i> лекция <b>322</b>',
             ' <b>•</b> <i>СМС/ЧA</i> практики <b>233/405</b>',
             ' <b>✕</b> Пятой пары нет']

up_tuesday = [' <b>•</b> <i>Теория вероятности и случайные процессы</i> практика <b>407</b>',
              ' <b>•</b> <i>Физра</i>',
              ' <b>•</b> <i>Основы права</i> практика <b>549</b>',
              ' <b>•</b> <i>ОДУ</i> лекция <b>533</b>',
              ' <b>✕</b> Пятой пары нет']

up_wednesday = [' <b>•</b> Первой пары нет',
                ' <b>•</b> <i>Численный анализ</i> практика <b>405</b> (первая группа)',
                ' <b>•</b> <i>МатЛог и ТеорАлг</i> лекция <b>403 к4</b>',
                ' <b>•</b> <i>Английский язык</i> <b>529</b>',
                ' <b>•</b> <i>МатЛог и ТеорАлг</i> практика <b>549</b>',
                ' <b>✕</b> Пятой пары нет']

up_thursday = [' <b>•</b> <i>Теория вероятности и случайные процессы</i> лекция <b>530</b>',
               ' <b>•</b> <i>Современные математические системы</i> лекция <b>508</b>',
               ' <b>•</b> <i>Философия</i> лекция <b>509</b>',
               ' <b>•</b> <i>СМС</i> практика <b>233</b> (вторая группа)',
               ' <b>✕</b> Пятой пары нет']

up_friday = [' <b>•</b> <i>Философия</i> практика <b>303</b>',
             ' <b>•</b> <i>ОДУ</i> практика <b>534</b>',
             ' <b>•</b> <i>Физра</i>',
             ' <b>✕</b> Четвёртой пары нет',
             ' <b>✕</b> Пятой пары нет']


down_week = {
    0: down_monday,
    1: down_tuesday,
    2: down_wednesday,
    3: down_thursday,
    4: down_friday
}

up_week = {
    0: up_monday,
    1: up_tuesday,
    2: up_wednesday,
    3: up_thursday,
    4: up_friday
}
