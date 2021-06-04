import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

data = pd.read_csv("./Input/output3.csv")

print(sns.relplot(data=data,x="gyro_x",y="gyro_z",hue="activity"))

newframe=pd.DataFrame({
    "acceleration_x":data["acceleration_x"].abs(),
    "acceleration_y":data["acceleration_y"].abs(),
    "activity":data["activity"]
})

print(sns.relplot(data=newframe,x="acceleration_x",y="acceleration_y",hue="activity"))

plt.show()

set(data["activity"])
labels=data.activity

data_dropped=data.drop(["id","date","time","activity"],axis=1)
features=data_dropped.values

LABELS=labels.values
FEATURES=features

from sklearn.model_selection import train_test_split


LABELS = np.nan_to_num(LABELS)
FEATURES = np.nan_to_num(FEATURES)


x_train,x_test,y_train,y_test=train_test_split(FEATURES,LABELS,test_size=0.3,random_state=1)

from sklearn.ensemble import RandomForestClassifier

RanFor=RandomForestClassifier(n_estimators=100,random_state=1)

RanFor.fit(x_train,y_train)
y_pred = RanFor.predict(x_test)

pickle.dump(RanFor, open('FitnessTracker.pkl','wb'))

from sklearn.metrics import *

print('Training Accuracy:',accuracy_score(y_train,RanFor.predict(x_train)))

print('Test Accuracy:',accuracy_score(y_test,RanFor.predict(x_test)))

print('Recall score:',recall_score(y_test,RanFor.predict(x_test)))

print('Precision score:',precision_score(y_test,RanFor.predict(x_test)))


