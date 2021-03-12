import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn import preprocessing

test = np.array([[1,7,4.2],[2,8,4.5],[3,13,5.8],[4,16,7.1],[5,3,11.5],[6,6,11.6],[7,15,14.5],[8,11,16.0],[9,1,22.5],[10,9,32.5],[11,5,32.6],[12,14,40.4],[13,10,51.2],[14,4,69.3],[15,2,119.1],[16,12,136.6]])
mm = preprocessing.MinMaxScaler() # インスタンスの作成
seiki = mm.fit_transform(test)

race = pd.read_csv('seikika2.csv', index_col = 0)
X = np.array([race["人気"],race["馬番"],race["単勝"],]).T
Y = np.array(race["順位"])
kaiki = linear_model.LinearRegression()
kaiki.fit(X, Y)

print(kaiki.predict(seiki))
