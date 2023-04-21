from __future__ import print_function
from sklearn.svm import SVC
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#bai 1
# X = np.array([[0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50,
# 2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50]]).T
# y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

# X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7 , shuffle = False)
# model = SVC(kernel = 'linear', C = 1e5) # just a big number
# model.fit(X_train, y_train)
# w = model.coef_
# b = model.intercept_
# print('w = ', w)
# print('b = ', b)
# y_pred = model.predict(X_test)
# count = y_pred.size
# dem = 0;
# for i in range(count):
#     print('Thuc te: ',y_test[i],' svm:',y_pred[i])
#     if(y_test[i] == y_pred[i]):
#         dem = dem + 1
# print('Xs phan lop dung: ',dem/count*100)
#--------------------------------
#bai 2
# data = pd.read_csv('Housing_data_price.csv')
# X = np.array(data[['bedrooms','bathrooms','stories','guestroom','basement','hotwaterheating','airconditioning','parking','prefarea','furnishingstatus']].values)    
# y = np.array(data['price_segment']).T
# for i, j in enumerate(X):
# 	for k in range(3,10):
# 		if(j[k] == "yes"):
# 			j[k] = 3
# 		elif(j[k] == "no"):
# 			j[k] = 1
# 		elif(j[k] == "furnished"):
# 			j[k] = 4
# 		elif(j[k] == "semi-furnished"):
# 			j[k] = 5
# 		elif(j[k] == "unfurnished"):
# 			j[k] = 6

# X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7 , shuffle = False)	


# clf = SVC(kernel = 'linear' , C = 1e5).fit(X_train, y_train)
# w_0=clf.intercept_
# w_1=clf.coef_
# print(w_0)
# print(w_1)
# y_pred = clf.predict(X_test)
# dem = 0
# for i in range(len(y_pred)):
# 	if(y_pred[i] == y_test[i]):
# 		dem = dem + 1
# 	print('Dự đoán [',y_pred[i],'] thực tế là [', y_test[i], ']\n')
# print("Thuật toán Perceptron dự đoán đúng được ",dem,' giá trị trên tổng số ',len(y_pred))

#-----------------------------
#bai 3

# import numpy as np
# from sklearn.svm import SVC

# X = np.array([[0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50,2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50]]).T
# y = np.array([-1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1])

# X1 = X[:15]
# X2 = X[15:20]
# y1 = y[:15]
# y2 = y[15:20]

# model = SVC(kernel = 'linear', C = 1e5) # just a big number
# model.fit(X1, y1)
# w = model.coef_
# b = model.intercept_

# y_pred = model.predict(X2)
# count = y_pred.size
# dem = 0;
# for i in range(count):
#     print('Thuc te: ',y2[i],' svm:',y_pred[i])
#     if(y2[i] == y_pred[i]):
#         dem = dem + 1
# print('Xs phan lop dung: ',dem/count*100)

