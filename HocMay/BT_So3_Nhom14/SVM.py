# Sử dụng trực tiếp thư viện sklearn
#Khai báo thư viện
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk #vẽ form
#########################################################33
from sklearn.model_selection import train_test_split
#Giải pháp bằng sklearn
from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score
# import category_encoders as ce
##############################################################
import numpy as np
import pandas as pd #các thứ viện cần thiết
import form as gd



data = pd.read_csv('data_hous_price.csv')#đọc file
print(data)
colums = ['bedrooms','bathrooms','stories','mainroad','guestroom','basement','hotwaterheating','airconditioning','parking','prefarea','furnishingstatus']
X = np.array(data[colums].values)#đưa về mảng mới nhân đc ma trận
y = np.array(data['price_segment']).T
print(X)
print(Y)
X = gd.convert_text_to_number(X)#chuyển đỗi chữ thành số
#Phân chia tập dữ liệu
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7 ,shuffle = False,  random_state = 50)	#train_test_split hàm trả về 4 giá trị, 
#đầu vào x,y: y ko cần chuyển đổi vì x để nhân còn y để so sánh, 
#train_size(0-1), shuffle: lấy từ trên xuống dưới ko lấy random(0-69)
svc = SVC(kernel = 'linear' )#công thức,kernel(lõi):hồi quy tuyến tính,kernel: thuộc tính
svc.fit(X_train,y_train)#fit: gọi tất cả các hàm đã gọi: trả về w, b
#x[...].w[] + b => y
y_pred=svc.predict(X_test)#đưa x vào để tính y#y dự đoán,kết quả dự đoán là mảng, hàm predict: dự đoán nhãn của Xtest,
dem = 0
data_pre = ""
for i in range(len(y_pred)):#len: đếm xembn bộ giá trị
	if(y_pred[i] == y_test[i]):
		dem = dem + 1#dự đoán đúng bn giá trị, bằng nhau + 1
	data_pre = data_pre + str('Với bộ giá trị ' +  str(X_test[i]) + ' hệ thống dự đoán [' + str(y_pred[i]) + '] thực tế là [' + str(y_test[i]) + ']\n')
data_pre = data_pre + str("Thuật toán SVM dự đoán đúng được "+ str(dem) + " giá trị trên tổng số " + str(len(y_pred)))
data_pre = data_pre + str("\nDự đoán đúng: ") + str(round(((dem/len(y_pred))*100),2))#vd 20/30






name_row= ['Phòng ngủ','Phòng Tắm','Tồn tại','Đường chính','Phòng khách','Tầng hầm','Bình nóng lạnh','Điều Hòa','Bãi đậu xe','Kho','Nội thất']
data_combobox = gd.get_Data_combobox(np.array(data[colums].values))
gd.Form(name_row,"SVM",data_pre,data_combobox,svc.predict)










