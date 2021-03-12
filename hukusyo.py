from urllib import request  # requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート
import pandas as pd

kaisai = 0
for k in range(5):
    kaisai += 1
    nitime = 0

    for i in range(15):
        nitime += 1
        race = 0

        for j in range(12):

            race += 1
            url = 'https://db.netkeiba.com/race/201801' + str(kaisai).zfill(2) + str(nitime).zfill(2) + str(race).zfill(2) + '/'
            response = request.urlopen(url)
            soup = BeautifulSoup(response, "html.parser")
            response.close()

            elif chaku == 1 or 2 or 3:
            data0 = soup.find('dl', class_='pay_block')
            data1 = data0.find('table', class_='pay_table_01')
            data2 = data1.find_all('tr')[1]
            data3 = data2.find_all('td')[1].childGenerator()
            huku = []
            for i in data3:
                huku.append(i)
            if chaku == 1:
                hukusyo = huku[0]
            elif chaku == 2:
                hukusyo = huku[2]
            elif chaku == 3:
                hukusyo = huku[4]
