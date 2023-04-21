import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
import category_encoders as ce

# data = pd.read_csv("thoitiet.csv")
# X = data.drop(['play'], axis=1)
# y = data['play']
# col = ['outlook','temperature','humidity','wind']


data = pd.read_csv("bai1.csv")
X = data.drop(['id','KetQua'],axis = 1)
y = data['KetQua']
col = ['MauToc','ChieuCao','CanNang','DungThuoc']


# data = pd.read_csv("bai2.csv")
# X = data.drop(['id','kq'],axis = 1)
# y = data['kq']
# col = ['Troi','ap suat','gio']

encoder = ce.OrdinalEncoder(cols= col)
X_pred = encoder.fit_transform(X)
###############################################################################################################33
svc = SVC( kernel='linear')
svc.fit(X_pred,y)
y_svc = svc.predict(X_pred)
print('svc:',accuracy_score(y, y_svc)*100)

###############################################################################################################33
logisticRegression = LogisticRegression()
logisticRegression.fit(X_pred,y)
y_logre = logisticRegression.predict(X_pred)
print('LogisticRegression:',accuracy_score(y, y_logre)*100)

###############################################################################################################33
decisionTreeClassifier = DecisionTreeClassifier(criterion='entropy', max_depth= None, random_state=0)
decisionTreeClassifier.fit(X_pred,y)
y_clf = decisionTreeClassifier.predict(X_pred)
print('DecisionTreeClassifier:',accuracy_score(y, y_clf)*100)

###############################################################################################################33
perceptron = Perceptron()
perceptron.fit(X_pred,y)
y_pct = perceptron.predict(X_pred)
print('Perceptron:',accuracy_score(y, y_pct)*100)