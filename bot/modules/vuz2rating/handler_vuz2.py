import pandas as pd
import requests

def vuz2_request(vuz2_user_id):
    url = "http://vuz2.bru.by/rate/"
    user = str(vuz2_user_id) + "/"
    url += user
    result = requests.get(url)

    table_html = result.content.decode(encoding="cp1251", errors="ignore")

    table_start = table_html.find("<table")
    table_end = table_html.find("</table>") + len("</table>")

    table = table_html[table_start: table_end]

    df = pd.read_html(table)
    result = str(df[0].iloc[3, :])

    return result


#print(vuz2_request(10034364))