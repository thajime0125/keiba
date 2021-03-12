from urllib import request  # requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート
import pandas as pd
import re

frame = ["距離","周り","馬場","着順","馬番","斤量","単勝","人気","増減","前着順","前距離","前馬番","前人気","複勝"]
df = pd.DataFrame(data=[], columns=frame)

for i in range (10):

    if i == 3 or 4 or 6:
        mawari = 0
    else:
        mawari = 1

    for j in range (5):

        for k in range (15):

            for l in range(12):

                url = 'https://race.netkeiba.com/race/result.html?race_id=2019' + str(i+1).zfill(2) + str(j+1).zfill(2) + str(k+1).zfill(2) + str(l+1).zfill(2) + '&rf=race_submenu'
                url2 = 'https://race.netkeiba.com/race/shutuba_past.html?race_id=2019' + str(i+1).zfill(2) + str(j+1).zfill(2) + str(k+1).zfill(2) + str(l+1).zfill(2) + '&rf=shutuba_submenu'
                response = request.urlopen(url)
                response2 = request.urlopen(url2)
                soup = BeautifulSoup(response, 'html.parser')
                soup2 = BeautifulSoup(response2, 'html.parser')
                response.close()
                response2.close()

                data = soup.find('div', class_='RaceData01')
                if data is None:
                    break
                racedata = data.find_all('span')
                if "障" in racedata[0].text:
                    continue
                if "ダ" in racedata[0].text:
                    continue
                kyori = re.sub('\\D', '', racedata[0].text)
                if "良" in racedata[2].text:
                    baba = 0
                else:
                    baba = 1

                table = soup.find('table', id='All_Result_Table').find('tbody')
                rows = table.find_all('tr')
                table2 = soup2.find('table', id='sort_table').find('tbody')
                rows2 = table2.find_all('tr')

                for row in rows:
                    chaku = row.find('div', class_='Rank').text
                    if str(chaku).isdecimal() == False:
                        continue
                    if int(chaku) < 4:
                        data1 = soup.find('table', class_='Payout_Detail_Table')
                        data2 = data1.find('tr', class_='Fukusho')
                        data3 = data2.find('td', class_='Payout').text.split("円")

                        if int(chaku) == 1:
                            hukusyo = data3[0]
                        elif int(chaku) == 2:
                            hukusyo = data3[1]
                        elif int(chaku) == 3:
                            hukusyo = data3[2]
                            if data3[2] is None:
                                hukusyo = 0
                    else:
                        hukusyo = 0

                    umaban = re.sub('\\D', '', row.find('td', class_='Num Txt_C').text)
                    kinryo = row.find('td', class_='Jockey_Info').text.lstrip().rstrip()
                    tansyo = row.find('td', class_='Odds Txt_R').text.lstrip().rstrip()
                    ninki = re.sub('\\D', '', row.find('span', class_='OddsPeople').text)
                    zogen = row.find('td', class_='Weight').find('small').text.rstrip(')').lstrip('(').lstrip("+")

                    for row2 in rows2:

                        if int(row2.find('td', class_='Waku').text) == int(umaban):
                            if row2.find('div', class_='Data_Item') is None:
                                paschaku = 5
                                paskyori = kyori
                                pasban = umaban
                                pasnin = ninki
                            else:
                                check = row2.find('div', class_='Data_Item')
                                paschaku = check.find('div', class_='Data01').find('span', class_='Num').text
                                paskyori = re.sub('\\D', '', check.find('div', class_='Data05').text.split(" ")[0])
                                check2 = check.find('div', class_='Data03').text.split()
                                pasban = re.sub('\\D', '', check2[1])
                                pasnin = re.sub('\\D', '', check2[2])

                                break

                    if str(paschaku).isdecimal() == False:
                        continue

                    se = pd.Series([kyori, mawari, baba, chaku, umaban, kinryo, tansyo, ninki, zogen, paschaku, paskyori, pasban, pasnin, hukusyo], index=frame)
                    df = df.append(se, frame)

                print("finish" + str(i+1).zfill(2) + str(j+1).zfill(2) + str(k+1).zfill(2) + str(l+1).zfill(2))

df.to_csv('racedata2019.csv', encoding='utf-8')