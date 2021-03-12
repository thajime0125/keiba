import pandas as pd
import numpy as np
from pandas import Series,DataFrame

import matplotlib.pyplot as plt
from sklearn import linear_model

data = pd.read_csv('seikika.csv')
frame = ["レース","芝ダ","距離","天候","馬場","着順","馬番","斤量","単勝","人気","馬体重","増減"]

#インスタンス
linear_regression = linear_model.LinearRegression()

#説明変数を縦(1)の列と指定して削除します！
X = data.drop("着順", 1)

#Yに目的変数を入れます！
Y = data.着順

#print(X.head())
#print(Y.head())

linear_regression.fit(X,Y)

coefficient['f_names'] = DataFrame(boston.feature_names)


