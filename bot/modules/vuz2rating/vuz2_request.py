import pandas as pd
import requests
from pathlib import Path
from json import loads


def vuz2_request(chat_id: int, number_of_control: int) -> str:
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

    conrol_names = {0: '❗️Экзамены',
                    1: '❕Зачеты',
                    3: '1️⃣Первый модуль',
                    4: '2️⃣Второй модуль',
                    7: '✅Итоговый модуль'}

    text = ''
    if number_of_control == 3 or number_of_control == 4 or number_of_control == 7:

        marks = []
        for i in range(1, len(df[0].iloc[0])):
            marks.append(df[0].iloc[number_of_control, i])

        text = f'<b><u>{conrol_names[number_of_control]}</u></b>:\n\n' \
               f'📐<i>Аналитическая геометрия:</i> <b>{marks[0]}</b>\n' \
               f'🖥<i>Вычислительные методы алгебры:</i> <b>{marks[1]}</b>\n' \
               f'📏<i>Дискретная математика:</i> <b>{marks[2]}</b>\n' \
               f'🇬🇧<i>Иностранный язык:</i> <b>{marks[3]}</b>\n' \
               f'💸<i>Коррупция и ее общественная опасность:</i> <b>{marks[4]}</b>\n' \
               f'📈<i>Математический анализ:</i> <b>{marks[5]}</b>\n' \
               f'🛠<i>Охрана труда:</i> <b>{marks[6]}</b>\n' \
               f'💻<i>Программирование:</i> <b>{marks[7]}</b>\n' \
               f'🗣<i>Разговорный иностранный язык:</i> <b>{marks[8]}</b>\n' \
               f'🏀<i>Физическая культура и спорт:</i> <b>{marks[9]}</b>\n' \
               f'🏋️‍♂️<i>Элективные курсы по физической культуре и спорту:</i> <b>{marks[10]}</b>\n' \
               f'☑️<i>Средний балл за модуль:</i> <b>{marks[11] / 100}</b>'.replace('nan', '0')

    elif number_of_control == 0:

        marks = []
        for i in range(1, len(df[0].iloc[0])):
            marks.append(df[0].iloc[number_of_control, i])

        text = f'<b><u>{conrol_names[number_of_control]}</u></b>:\n\n' \
               f'📐<i>Аналитическая геометрия:</i> <b>{marks[0]}</b>\n' \
               f'📏<i>Дискретная математика:</i> <b>{marks[2]}</b>\n' \
               f'🇬🇧<i>Иностранный язык:</i> <b>{marks[3]}</b>\n' \
               f'📈<i>Математический анализ:</i> <b>{marks[5]}</b>\n' \
               f'💻<i>Программирование:</i> <b>{marks[7]}</b>\n'.replace('nan', 'Нет результатов')

    elif number_of_control == 1:

        marks = []
        for i in range(1, len(df[0].iloc[0])):
            marks.append(df[0].iloc[number_of_control, i])

        text = f'<b><u>{conrol_names[number_of_control]}</u></b>:\n\n' \
               f'🖥<i>Вычислительные методы алгебры:</i> <b>{marks[1]}</b>\n' \
               f'💸<i>Коррупция и ее общественная опасность:</i> <b>{marks[4]}</b>\n' \
               f'🛠<i>Охрана труда:</i> <b>{marks[6]}</b>\n' \
               f'🗣<i>Разговорный иностранный язык:</i> <b>{marks[8]}</b>\n' \
               f'🏀<i>Физическая культура и спорт:</i> <b>{marks[9]}</b>\n' \
               f'🏋️‍♂️<i>Элективные курсы по физической культуре и спорту:</i> <b>{marks[10]}</b>\n'.replace('nan', 'Нет результатов')

    return text
