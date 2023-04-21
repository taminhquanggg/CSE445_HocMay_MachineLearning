
from tkinter import *
from tkinter import messagebox
# Sử dụng trực tiếp thư viện sklearn
#Khai báo thư viện
import tkinter as tk
from tkinter import ttk#vẽ form
#########################################################33
from sklearn.model_selection import train_test_split#for splitting data
#Giải pháp bằng sklearn
from sklearn.linear_model import LogisticRegression#sử dụng thư viện sklearn-learn để tìm nghiệm
# from sklearn.metrics import accuracy_score#for evaluating results
# import category_encoders as ce
##############################################################
#các thứ viện cần thiết
import numpy as np#numpy: xử lý dũ liếu số, tạo và truy cập mảng
import pandas as pd#pandas:xử lý dũ liếu cấu trúc dạng bảng  tương tác dữ liệu có cấu trúc, thu thập và tiền xử lý dữ liệu
import form as gd


# đọc dữ liệu tù file.csv
data = pd.read_csv('data_hous_price.csv')
colums = ['bedrooms','bathrooms','stories','mainroad','guestroom','basement','hotwaterheating','airconditioning','parking','prefarea','furnishingstatus']
X = np.array(data[colums].values)#đưa về mảng mới nhân đc ma trận
y = np.array(data['price_segment']).T
X = gd.convert_text_to_number(X)#chuyển đỗi chữ thành số
#Phân chia tập dữ liệu
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7 , shuffle = False)#shuffle = False giống random_state=45, 
#train_test_split hàm trả về 4 giá trị, đầu vào x,y: y ko cần chuyển đổi vì x để nhân còn y để so sánh, 
#train_size(0-1), shuffle: lấy từ trên xuống dưới ko lấy random(0-69)
logisticRegression = LogisticRegression()#thực hiện training dữ liệu
logisticRegression.fit(X_train,y_train)#fit: gọi tất cả các hàm đã gọi
#Dựa vào kết quả nhận được, dự đoán việc phân loại cho tập test dùng hàm predict()
y_pred = logisticRegression.predict(X_test)#hàm predict: dự đoán nhãn của Xtest, #đưa x vào để tính y#y dự đoán,kết quả dự đoán là mảng
dem = 0
data_pre = ""
for i in range(len(y_pred)):#len: đếm xembn bộ giá trị
	if(y_pred[i] == y_test[i]):
		dem = dem + 1#dự đoán đúng bn giá trị, bằng nhau + 1
	data_pre = data_pre + str('Với bộ giá trị ' +  str(X_test[i]) + ' hệ thống dự đoán [' + str(y_pred[i]) + '] thực tế là [' + str(y_test[i]) + ']\n')
data_pre = data_pre + str("Thuật toán Logistic Regression dự đoán đúng được "+ str(dem) + " giá trị trên tổng số " + str(len(y_pred)))
data_pre = data_pre + str("\nDự đoán đúng ") + str(round(((dem/len(y_pred))*100),2))#vd 20/30



name_row= ['Phòng ngủ','Phòng Tắm','Tồn tại','Đường chính','Phòng khách','Tầng hầm','Bình nóng lạnh','Điều Hòa','Bãi đậu xe','Kho','Nội thất']
#i->name_row
#dem = 1
#i = "Phòng ngủ" trái
#dem = 2
#i = "Phòng tắm" phải


data_combobox = gd.get_Data_combobox(np.array(data[colums].values))
gd.Form(name_row,"Logistic Regression",data_pre,data_combobox,logisticRegression.predict)