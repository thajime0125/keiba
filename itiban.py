import pandas as pd
import numpy as np

race = pd.read_csv('2018_data.csv')

X = np.array(race["人気"])
Y = np.array(race["着順"])
Z = np.array(race["単勝"])

sum = 0
win = 0
for i in range(30650):
    if X[i]==1:
        if Y[i]==1:
            win+=Z[i]
        sum+=1

print(sum)
print(win)
print(win/sum)
