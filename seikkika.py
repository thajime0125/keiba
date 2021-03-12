import pandas as pd

race = pd.read_csv('racedata_201801.csv', index_col=0)
race = pd.concat([race, pd.read_csv('racedata_201802.csv', index_col=0)])
race = pd.concat([race, pd.read_csv('racedata_201803.csv', index_col=0)])
race = pd.concat([race, pd.read_csv('racedata_201806.csv', index_col=0)])
race = pd.concat([race, pd.read_csv('racedata_201808.csv', index_col=0)])
race = pd.concat([race, pd.read_csv('racedata_201809.csv', index_col=0)])
race = pd.concat([race, pd.read_csv('racedata_201810.csv', index_col=0)])


frame = ["レース","芝ダ","距離","天候","馬場","着順","馬番","斤量","単勝","人気","馬体重","増減","複勝"]

df = pd.DataFrame(data=race, columns=frame)
df.to_csv('racedata_2018.csv', encoding='utf-8')