from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
# thuật toán perceptron xây dựng hàm tuyến tính phân chia dl thành 2 lớp tìm hệ số
# tính toán trên dl số 
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
ppn = Perceptron(random_state=0)
ppn.fit(X_train, y_train)
y_pred = ppn.predict(X_test)
dem = 0
for i in range(len(y_pred)):
	if(y_pred[i] == y_test[i]):
		dem = dem + 1
	print('Dự đoán [',y_pred[i],'] Thực tế là [', y_test[i], ']\n')
print("Thuật toán Perceptron dự đoán đúng được ",dem,' giá trị trên tổng số ',len(y_pred))




