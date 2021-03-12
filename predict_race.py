import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
race = pd.read_csv('seikika_2019.csv', index_col=0)
race = race.dropna(how='any')


X = np.array([race["馬番"], race["斤量"], race["単勝"], race["人気"], race["前着順"], race["前馬番"], race["前人気"]]).T
Y = np.array(race["着順"])
Z = np.array(race["単勝オッズ"])
import sklearn.model_selection

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge

result = 0

today = pd.read_csv('kikka.csv', index_col=0)
mm = preprocessing.MinMaxScaler() # インスタンスの作成
today_seiki = mm.fit_transform(today)


X_train, X_test, Y_train, Y_test, Z_train, Z_test = sklearn.model_selection.train_test_split(X, Y, Z)
poly = PolynomialFeatures(degree=2).fit(X_train)
X_train_poly = poly.transform(X_train)
X_test_poly = poly.transform(X_test)
today_poly = poly.transform(today_seiki)

ridge = Ridge().fit(X_train_poly, Y_train)
print(f"X_train_poly.shape : {X_train_poly.shape}")
print(f'Score with polynomial features  : {ridge.score(X_test_poly, Y_test):.3f}')

print('-'*50)

print(ridge.predict(today_poly))
