import pandas as pd
import requests
from pathlib import Path
from json import loads


def vuz2_request(chat_id: int, type_of_control: str) -> str:
    """Делает парс таблицы рейтинга с http://vuz2.bru.by/rate/"""

    path = Path('bot', 'data', 'databases', 'vuz2_list', 'vuz2_list.json')
    with open(path, 'r', encoding='utf-8') as vuz2_list:
        vuz2_list = loads(vuz2_list.read())

    vuz2_user_id = vuz2_list[str(chat_id)]

    url = f'http://vuz2.bru.by/rate/{str(vuz2_user_id)}/'
    result = requests.get(url)
    table_html = result.content.decode(encoding="cp1251", errors="ignore")
    table_start = table_html.find("<table")
    table_end = table_html.find("</table>") + 8
    table = table_html[table_start: table_end]
    df = pd.read_html(table)

    list_of_controls = list(df[0].iloc[:, 0])  # Виды контроля
    items = list(df[0])[1:-1]  # Список предметов

    # Ищем нужную строку в таблице
    number_of_control = 0
    if type_of_control == 'Экзамен Дата':  # Экзамены - первая строка
        number_of_control = 0
    elif type_of_control == 'Зачёт Дата':  # Зачёты - вторая строка
        number_of_control = 1
    else:  # Оставшиеся - модули, тут могут быть: 1-ый модуль, 2-ой модуль, Итоговый модуль
        try:
            number_of_control = list_of_controls.index(type_of_control)
        except:  # У РБ нет строки Итоговый модуль
            text = '😭Простите, но у вас <u><b><i>нет</i></b></u> такой ' \
                   '<u><b><i>строчки</i></b></u> в вашей таблице рейтинга'
            return text

    # Баллы без среднего
    marks = [df[0].iloc[number_of_control, i] for i in range(1, len(df[0].iloc[0]) - 1)]

    name_of_control = {
        'Экзамен Дата': '📝Экзамены',
        'Зачёт Дата': '📖Зачёты',
        '1-ый модуль': '1️⃣Первый модуль',
        '2-ой модуль': '2️⃣Второй модуль',
        'Итоговый модуль': '✅Итоговый модуль'}
    control = name_of_control[type_of_control]

    # Начало сообщения - вид контроля
    text = f'<b>{control}:</b>\n'

    # Составляем сообщения
    sum_of_marks = 0  # Сумма для подсчета среднего балла
    count_of_marks = 0  # Количество оценок
    for item, mark in zip(items, marks):
        # Для модулей
        if type_of_control in ('1-ый модуль', '2-ой модуль', 'Итоговый модуль'):
            if mark != '-':  # В сообщение не включаем те предметы, по которым нет модулей
                if str(mark) == 'nan':  # Заменяем все nan на 0
                    mark = '0'
                text += f'✦<i>{item}</i>: <b>{mark}</b>\n'
                # Для среднего балла
                sum_of_marks += int(mark)
                count_of_marks += 1
        else:  # Для экзаменов/зачётов
            if mark != '-':  # В сообщение не включаем те предметы, по которым нет экзамена/зачёта
                if str(mark) == 'nan':  # Заменяем все nan на 0
                    mark = '0'
                text += f'✦<i>{item}</i>: <b>{mark}</b>\n'.replace('nan', 'Нет результата')
                # Для среднего балла
                sum_of_marks += int(mark)
                count_of_marks += 1

    # Добавляем строку со средним баллом
    avarage_mark = round(sum_of_marks / count_of_marks, 2)
    text += f'✦<i>Средний балл</i>: <b>{avarage_mark}</b>'

    return text
