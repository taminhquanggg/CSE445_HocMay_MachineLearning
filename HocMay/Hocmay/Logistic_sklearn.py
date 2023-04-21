from __future__ import print_function
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# X = np.array([[0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50,
# 2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50]]).T
# y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

# clf = LogisticRegression(random_state=0).fit(X, y)
# nh = clf.predict(X)
# print(nh)

#-----------------------------------
data = pd.read_csv('Housing_data_price.csv', parse_dates = True)
X = np.array(data[['bedrooms','bathrooms','stories','guestroom','basement','hotwaterheating','airconditioning','parking','prefarea','furnishingstatus']].values)    
y = np.array(data['price_segment']).T

for i, j in enumerate(X):
	for k in range(3,10):
		if(j[k] == "yes"):
			j[k] = 3
		elif(j[k] == "no"):
			j[k] = 1
		elif(j[k] == "furnished"):
			j[k] = 4
		elif(j[k] == "semi-furnished"):
			j[k] = 5
		elif(j[k] == "unfurnished"):
			j[k] = 6
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3 , shuffle = False)	
ppn = LogisticRegression(random_state=0)
ppn.fit(X_train, y_train)
y_pred = ppn.predict(X_test)
dem = 0
for i in range(len(y_pred)):
	if(y_pred[i] == y_test[i]):
		dem = dem + 1
	print('Dự đoán [',y_pred[i],'] Thực tế là [', y_test[i], ']\n')
print("Thuật toán Logistic dự đoán đúng được ",dem,' giá trị trên tổng số ',len(y_pred))