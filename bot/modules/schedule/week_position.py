import datetime


def up_down_week():
    """Определяет, верхняя или нижняя неделя"""
    # Четные - верхние, нечетные - нижние
    number_of_week = datetime.datetime.today().isocalendar()[1]
    if number_of_week % 2:
        return 1  # Нечётная - нижняя
    else:
        return 0  # Чётная - верхняя


WEEK_POSITION = up_down_week()
