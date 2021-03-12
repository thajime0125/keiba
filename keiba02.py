from urllib import request  # requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート
import pandas as pd

frame = ["レース","芝ダ","距離","天候","馬場","着順","馬番","斤量","単勝","人気","馬体重","増減","複勝"]



df = pd.DataFrame(data=[], columns=frame)

for k in range(5):

    for i in range(15):

        for j in range(12):

            url = 'https://db.netkeiba.com/race/201810' + str(k+1).zfill(2) + str(i+1).zfill(2) + str(j+1).zfill(2) + '/'
            response = request.urlopen(url)
            soup = BeautifulSoup(response, "html.parser")
            response.close()

            #レースデータの取得
            data = soup.find('dl', class_='racedata fc')
            if data is None:
                break
            racedata = data.find('span').text.split()
            if "障" in racedata[0]:
                print("finish")
                continue
            elif racedata[0] == "芝右":
                sibada = racedata[7]
                kyori = racedata[1]
                tenko = racedata[5]
                baba = racedata[9]
            else:
                sibada = racedata[6]
                kyori = racedata[0].split("右")[1]
                tenko = racedata[4]
                baba = racedata[8]

            #出走馬データの取得
            table = soup.find('table', class_='race_table_01 nk_tb_common')
            rows = table.find_all('tr')

            for row in rows[1:]:
                chaku = row.find_all('td')[0].text
                if chaku=="取":
                    continue
                elif chaku=="中":
                    continue
                elif chaku=="除":
                    continue
                elif chaku=="3(降)":
                    chaku = 3
                if int(chaku) == 1:
                    data0 = soup.find('dl', class_='pay_block')
                    data1 = data0.find('table', class_='pay_table_01')
                    data2 = data1.find_all('tr')[1]
                    data3 = data2.find_all('td')[1].childGenerator()
                    huku = []
                    for d in data3:
                        huku.append(d)
                    hukusyo = huku[0]
                elif int(chaku) == 2:
                    data0 = soup.find('dl', class_='pay_block')
                    data1 = data0.find('table', class_='pay_table_01')
                    data2 = data1.find_all('tr')[1]
                    data3 = data2.find_all('td')[1].childGenerator()
                    huku = []
                    for d in data3:
                        huku.append(d)
                    hukusyo = huku[2]
                elif int(chaku) == 3:
                    data0 = soup.find('dl', class_='pay_block')
                    data1 = data0.find('table', class_='pay_table_01')
                    data2 = data1.find_all('tr')[1]
                    data3 = data2.find_all('td')[1].childGenerator()
                    huku = []
                    for d in data3:
                        huku.append(d)
                    if len(huku) > 4:
                        hukusyo = huku[4]
                    else:
                        hukusyo = 0
                else:
                    hukusyo = 0

                umaban = row.find_all('td')[2].text
                kinryo = row.find_all('td')[5].text
                tansyo = row.find_all('td')[12].text
                ninki = row.find_all('td')[13].text
                batai = row.find_all('td')[14].text.split("(")
                taiju = batai[0]
                zogen = batai[1].rstrip(")")

                se = pd.Series([str(j+1), sibada, kyori, tenko, baba, chaku, umaban, kinryo, tansyo, ninki, taiju, zogen,hukusyo], index=frame)
                df = df.append(se, frame)

            print("finish" +str(k+1).zfill(2) + str(i+1).zfill(2) + str(j+1).zfill(2))

df.to_csv('racedata201810.csv', encoding='utf-8')


