import pandas as pd
import numpy as np
import re
import sklearn
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

# Going to use these 5 base models for the stacking
from sklearn.ensemble import (RandomForestClassifier, AdaBoostClassifier,
                              GradientBoostingClassifier, ExtraTreesClassifier)
from sklearn.svm import SVC
from sklearn.model_selection import KFold

from collections import defaultdict

import numpy as np
from sklearn import datasets
#from sklearn.ensemble import VotingRegression
from sklearn.linear_model import LogisticRegression
#from sklearn.neighbors import KNeighborsRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.naive_bayes import GaussianNB



data = pd.read_csv("seikika3.csv", index_col=0)

data=data.astype(float)

data=data.dropna()

data.isnull().sum()

t=np.array(data['着順']).T
#t.shape

x=np.array([data['芝ダ'],data['距離'],data['天候'],data['馬場'],data['馬番'],data['斤量'],data['単勝'],data['人気'],data['馬体重'],data['増減'],]).T
#x.shape
z=np.array(data["単勝オッズ"])

from sklearn.model_selection import train_test_split

x_train,x_test,t_train,t_test,z_train,z_test = train_test_split(x,t,z, test_size=0.3,random_state=0)

from sklearn.model_selection import train_test_split

x_train1,x_train2,t_train1,t_train2 = train_test_split(x_train,t_train,test_size=0.5,random_state=0)

from sklearn.ensemble import VotingRegressor
from sklearn.linear_model import LinearRegression

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor



from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_boston
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_error
from catboost import CatBoostRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.linear_model import Ridge
#from xgboost import XGBRegressor
import numpy as np

seed=60

models_dic = {
    'random forest': RandomForestRegressor(n_estimators=50, random_state=seed),
    'linear regression': LinearRegression(normalize=True),
    'knn': KNeighborsRegressor(),
    'catboost': CatBoostRegressor(custom_metric=['MAE'], random_seed=seed, logging_level='Silent')
}


from heamy.dataset import Dataset
from heamy.estimator import Regressor
from heamy.pipeline import ModelsPipeline
from catboost import CatBoostRegressor
#import adaboost
# datasetを準備
dataset = Dataset(x_test, t_test, x_train2) # X_testは今回使わないが入れないとエラーになる

# アンサンブルに使うモデルを定義
models = [
    Regressor(dataset=dataset, estimator=RandomForestRegressor, parameters={'n_estimators': 50, 'random_state': seed}, name='rf'),
    Regressor(dataset=dataset, estimator=LinearRegression, parameters={'normalize': True}, name='lr'),
    Regressor(dataset=dataset, estimator=KNeighborsRegressor, name='kr'),
    Regressor(dataset=dataset, estimator=CatBoostRegressor, parameters={'custom_metric': ['MAE'], 'random_seed': seed, 'logging_level': 'Silent'}, name='cr')
]

# pipelineを定義、2nd levelデータセットの作成
pipeline = ModelsPipeline(*models)
stack_ds = pipeline.stack(k=10, seed=seed)

# modelを作ってvalidation
stacker = Regressor(dataset=stack_ds, estimator=LinearRegression)
y_trues, y_preds = stacker.validate(k=10)

# 精度出力
# X_testを使ってpredict
y_pred = stacker.predict()
print(y_pred)

sum = 0
buy = 0
for i, yosoku in enumerate(x_test):
    if stacker.predict(x_test[i]) < 0.3:
        if t_test[i]==0:
            sum += z_test[i]
        buy += 1

print(sum)
print(buy)
print(sum/buy)