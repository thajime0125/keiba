from urllib import request  # urllib.requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート
import pandas as pd

for j in range(12):
    url = 'https://db.netkeiba.com/race/2018010101'+ str(j+1).zfill(2) + '/'
    response = request.urlopen(url)
    soup = BeautifulSoup(response, "html.parser")
    response.close()

    #レースデータの取得
    table = soup.find('table', class_='race_table_01 nk_tb_common')
    rows = table.find_all('tr')
    for row in rows[1:]:

        chaku = row.find_all('td')[0].text
        if int(chaku)==1:
            data0 = soup.find('dl', class_='pay_block')
            data1 = data0.find('table', class_='pay_table_01')
            data2 = data1.find_all('tr')[1]
            data3 = data2.find_all('td')[1].childGenerator()
            huku = []
            for i in data3:
                huku.append(i)
            hukusyo = huku[0]
        elif int(chaku)==2:
            data0 = soup.find('dl', class_='pay_block')
            data1 = data0.find('table', class_='pay_table_01')
            data2 = data1.find_all('tr')[1]
            data3 = data2.find_all('td')[1].childGenerator()
            huku = []
            for i in data3:
                huku.append(i)
            hukusyo = huku[2]
        elif int(chaku)==3:
            data0 = soup.find('dl', class_='pay_block')
            data1 = data0.find('table', class_='pay_table_01')
            data2 = data1.find_all('tr')[1]
            data3 = data2.find_all('td')[1].childGenerator()
            huku = []
            for i in data3:
                huku.append(i)
            if len(huku) > 4:
                hukusyo = huku[4]
            else:
                hukusyo = 0
        else:
            hukusyo = 0

        print(hukusyo)
