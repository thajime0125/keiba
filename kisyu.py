from urllib import request  # urllib.requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート
import pandas as pd

frame = ["騎手","勝利数"]
df = pd.DataFrame(columns=frame)
url = 'https://db.netkeiba.com/?pid=jockey_leading&year=2018'
response = request.urlopen(url)
soup = BeautifulSoup(response, "html.parser")
response.close()

table = soup.find('table', class_='nk_tb_common race_table_01')
rows = table.find_all('tr')[2:]

for row in rows:
    kisyu = row.find_all('td')[1].text
    syori = row.find_all('td')[4].text

    se = pd.Series([kisyu, syori],index=frame)
    df = df.append(se, frame)

df.to_csv('kisyudata.csv', encoding='utf-8')