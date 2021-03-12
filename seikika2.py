from sklearn import preprocessing
import pandas as pd
import numpy as np

race = pd.read_csv('racedata2019.csv')

for i, chaku in enumerate(race.着順):
    if chaku==1:
        race.at[i, "入賞"] = 0
    elif chaku==2:
        race.at[i, "入賞"] = 0
    elif chaku==3:
        race.at[i, "入賞"] = 0
    else:
        race.at[i, "入賞"] = 1

mm = preprocessing.MinMaxScaler() # インスタンスの作成
seiki = mm.fit_transform(race)

odds = np.array([race["着順"],race["単勝"],race["複勝"]]).T
seiki = np.concatenate([seiki, odds], 1)

frame = ["","距離","馬場","着順","馬番","斤量","単勝","人気","増減","前着順","前距離","前馬番","前人気","複勝","入賞","順位","単勝オッズ","複勝オッズ"]
df = pd.DataFrame(data=seiki, columns=frame)
df.to_csv('seikika_2019.csv', encoding='utf-8')
