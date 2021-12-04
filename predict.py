import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('music.csv')
le = LabelEncoder()
data['genre'] = le.fit_transform(data.genre)
x = data.drop(columns = 'genre')
y = data.genre
model = DecisionTreeClassifier()
x_train, x_test, y_train, y_test = train_test_split(x , y, test_size = 0.3)

def genre_predictor(age,gender):
    model.fit(x_train,y_train)
    ypred = {3:'HipHop', 4:'Jazz', 1:'Classical', 2:'Dance', 0:'Acoustic'}
    predicted = model.predict([[age,gender]])
    return ypred[int(predicted)]


def accuracy_score():
    predict = model.predict(x_test)
    score = str(metrics.accuracy_score(y_test, predict)*100)+'%'
    return score



 