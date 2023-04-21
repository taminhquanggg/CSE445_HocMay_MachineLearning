
from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
#########################################################33
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# import category_encoders as ce
##############################################################
import numpy as np
import pandas as pd
import form as gd



data = pd.read_csv('Housing_data_price.csv')
colums = ['bedrooms','bathrooms','stories','mainroad','guestroom','basement','hotwaterheating','airconditioning','parking','prefarea','furnishingstatus']
X = np.array(data[colums].values)    
y = np.array(data['price_segment']).T
X = gd.convert_text_to_number(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7 , shuffle = False)	
logisticRegression = LogisticRegression()
logisticRegression.fit(X_train,y_train)
y_pred = logisticRegression.predict(X_test)
dem = 0
data_pre = ""
for i in range(len(y_pred)):
	if(y_pred[i] == y_test[i]):
		dem = dem + 1
	data_pre = data_pre + str('Với bộ giá trị ' +  str(X_test[i]) + ' hệ thống dự đoán [' + str(y_pred[i]) + '] thực tế là [' + str(y_test[i]) + ']\n')
data_pre = data_pre + str("Thuật toán Logistic Regression dự đoán đúng được "+ str(dem) + " giá trị trên tổng số " + str(len(y_pred)))
data_pre = data_pre + str("\nDự đoán đúng ") + str(round(((dem/len(y_pred))*100),2))



name_row= ['Phòng ngủ','Phòng Tắm','Tồn tại','Đường chính','Phòng khách','Tầng hầm','Bình nóng lạnh','Điều Hòa','Bãi đậu xe','Kho','Nội thất']
data_combobox = gd.get_Data_combobox(np.array(data[colums].values))
gd.Form(name_row,"Logistic Regression",data_pre,data_combobox,logisticRegression.predict)