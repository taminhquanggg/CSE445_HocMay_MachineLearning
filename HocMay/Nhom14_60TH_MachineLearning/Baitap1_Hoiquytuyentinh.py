from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#lấy và xử lý data
data = pd.read_csv("Data_Car.csv")
print(data)
X = np.array(data[['DOORNUMBER','CARLENGTH','CARWIDTH','CARHEIGHT','CYLINDERNUMBER','ENGINESIZE','COMPRESSINRATIO','HORSEPOWER']].values)
Y = np.array(data['PRICE']).T
#chia data theo tỷ lệ
xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=0.3, shuffle = False)	# chia data theo tỷ lệ

print("Train: \n")
print(xtrain,'\n',ytrain)
print("Test: \n")
print(xtest,'\n',ytest)


#use hồi quy
regr1 = linear_model.LinearRegression() #Bình phương nhỏ nhất thông thường Hồi quy tuyến tính.
regr1.fit(xtrain,ytrain) #use hồi quy




w_0=regr1.intercept_    # số hạng đập lập trong mô hình tuyến tính
print('w_0 = ',w_0,'\n')
w_1=regr1.coef_			# hệ số ước lượng
print('w_1 = ',w_1,'\n')


#thực hiện test
pre = []

for i in range(len(ytest)):
     kqDuDoan = np.dot(w_1, xtest[i]) + w_0    #tính kqddoan
     pre.append(kqDuDoan)
     print('Với xtest là ' + str(xtest[i]) + ' thì kết quả dự đoán là '+ str(round(kqDuDoan,2)) + ' kết quả thực tế là '+ str(ytest[i]) + '\n')
     print('Sai lệch : ',round(abs(ytest[i] - round(kqDuDoan,2)),2),'\n')





#pre = regr1.predict(xtest)
#print('Đánh giá sai số ',round(np.sqrt(mean_squared_error(ytest, pre)), 3))

#vẽ biểu đồ
plt.style.use('dark_background')
plt.title("Đồ thị biểu diễn giá xe")
plt.ylabel("Giá xe")
#plt.scatter(ytest,pre)
# # plt.scatter(ytest,ytest,'yellow')
plt.plot(ytest,'red')
plt.plot(pre,'blue')
plt.show()









