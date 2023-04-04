def create(number: int, userid: int) -> tuple:
    """Запрос для добавления пользователя (чата с ним) в белый список

    :param: number - номер пользователя
    :param: userid - id пользователя
    :param: whitelist - название таблицы в базе
    """
    request = f'INSERT INTO whitelist VALUES(?, ?);'
    user = (number, userid)
    return request, user
