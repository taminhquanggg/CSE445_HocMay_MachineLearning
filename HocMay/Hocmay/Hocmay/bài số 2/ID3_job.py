import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import category_encoders as ce

df = pd.read_csv('job.csv')
data_X = df.iloc[:, :-1]
data_y = df.iloc[:, -1]
xtrain, xtest, ytrain, ytest = train_test_split(data_X,data_y,test_size=0.95, shuffle = False)

encoder = ce.OrdinalEncoder(cols=['Gender','Stream'])

xtrain = encoder.fit_transform(xtrain)
print(xtrain)
exit()
xtest  = encoder.fit_transform(xtest)
sc = StandardScaler()
sc.fit(xtrain)
xtrain = sc.transform(xtrain)
xtest = sc.transform(xtest)


entropy = DecisionTreeClassifier(criterion='entropy',max_depth = 5, min_samples_split = 2)
entropy.fit(xtrain,ytrain)
data = entropy.predict(xtest)
y_test = np.array(ytest)
count = 0

for i in range(len(data)):
        if data[i] == y_test[i]:
            count = count + 1
        print(i,'Dự đoán :', data[i], ', Thực tế :', y_test[i])
        
rate  = round((count/len(data))*100)
print('\nID3 cho ta tỉ lệ dự đoán như sau : ')
print('Số dự đoán đúng',count ,'trên tổng',len(data),'\nTỷ lệ đúng đạt :' ,rate,'%')

