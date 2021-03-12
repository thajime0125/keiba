import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.ensemble import VotingRegressor
#from sklearn import svm

race = pd.read_csv('seikika_2019.csv')
race = race.dropna(how='any')
X = np.array([race["馬番"], race["斤量"], race["単勝"], race["人気"], race["前着順"], race["前馬番"], race["前人気"]]).T
Y = np.array(race["着順"])
Z = np.array(race["単勝オッズ"])
import sklearn.model_selection

result = 0
from sklearn import preprocessing
satsuki = pd.read_csv('derby.csv', index_col=0)
mm = preprocessing.MinMaxScaler() # インスタンスの作成
satsuki_seiki = mm.fit_transform(satsuki)

from catboost import CatBoostRegressor
from sklearn.ensemble import (RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor, ExtraTreesRegressor)
#kaiki = GradientBoostingRegressor()
#kaiki.fit(X_train, Y_train)
#    clf = svm.SVR()
#    clf.fit(X_train,Y_train)


#X_train, X_test, Y_train, Y_test, Z_train, Z_test = sklearn.model_selection.train_test_split(X, Y, Z)
estimator = [
    ('gb', GradientBoostingRegressor()),
    ('lr', linear_model.LinearRegression()),
#        ('ab', AdaBoostRegressor()),
#        ('cb', CatBoostRegressor())
]
voting = VotingRegressor(estimator)
voting.fit(X, Y)
print(voting.predict(satsuki_seiki))
#sum = 0
#buy = 0
#for i, data in enumerate(X_test):
#    if voting.predict(X_test[i:i+1]) < 0.25:
#        if Y_test[i] == 0:
#            sum += Z_test[i]
#        buy += 1

#print(sum/buy)
#result += (sum/buy)
