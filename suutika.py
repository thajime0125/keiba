import pandas as pd

race = pd.read_csv('racedata201806.csv', index_col=0)

for i, sibada in enumerate(race.芝ダ):
    if sibada=="芝":
        race.at[i, "芝ダ"] = 0
    elif sibada=="ダート":
        race.at[i, "芝ダ"] = 1

for i, kyori in enumerate(race.距離):
    race.at[i, "距離"] = race.at[i, "距離"].rstrip("m").lstrip("外").lstrip("内2周")

for i, tenko in enumerate(race.天候):
    if tenko=="晴" or tenko=="曇":
        race.at[i, "天候"] = 0
    else:
        race.at[i, "天候"] = 1

for i, baba in enumerate(race.馬場):
    if baba=="良":
        race.at[i, "馬場"] = 0
    else:
        race.at[i, "馬場"] = 1



frame = ["レース","芝ダ","距離","天候","馬場","着順","馬番","斤量","単勝","人気","馬体重","増減","複勝"]


race.to_csv('racedata_201806.csv', columns=frame, encoding='utf-8')


