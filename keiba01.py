from urllib import request  # urllib.requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート
import pandas as pd


num = 0
frame = ["着順","馬番","馬名","性齢","負担重量","騎手","タイム","着差","推定上り","馬体重","変動","調教師","単勝人気"]
df = pd.DataFrame(columns=frame)

for i in range (108):
    num += 1
    url = 'http://www.jra.go.jp/datafile/seiseki/replay/2018/' + str(num).zfill(3) + '.html'
    response = request.urlopen(url)
    soup = BeautifulSoup(response, "html.parser")
    response.close()
    #racedata = soup.find('div', class_='race_data').text
    rows = soup.find_all('tr', class_=['oddRow','evenRow'])
    for row in rows:
        chaku = row.find('td', class_='chakuCol').text
        umaban = row.find('td', class_='umabanCol').text
        umamei = row.find('td', class_='umameiCol').text
        seirei = row.find('td', class_='seireiCol').text
        hutan = row.find('td', class_='hutanCol').text
        kishu = row.find('td',  class_='jocCol').text
        time = row.find('td', class_='timeCol').text
        chakusa = row.find('td', class_='chakusaCol').text
        agari = row.find('td', class_='suiteiCol').text
        batai = row.find('td', class_='bataiCol').text
        zogen = row.find('td', class_='zougenCol').text
        choukyo = row.find('td', class_='choukyoCol').text
        ninki = row.find('td', class_='ninkiCol').text

        se = pd.Series([chaku, umaban, umamei, seirei, hutan, kishu, time, chakusa, agari, batai, zogen, choukyo, ninki], index=frame)
        df = df.append(se, frame)

    print("finish" + str(i))

df.to_csv('racedata.csv', mode='a', encoding='utf-8')

#   time.sleep(1)






