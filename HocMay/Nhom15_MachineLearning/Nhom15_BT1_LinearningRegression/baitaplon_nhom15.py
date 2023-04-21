from sklearn import linear_model # mô hình tuyến tính
from sklearn.model_selection import train_test_split #Chia mảng hoặc ma trận thành tập hợp con thử nghiệm và huấn luyện ngẫu nhiên
                                                    #sklearn.model_selection. train_test_split ( * mảng , test_size = Không có , train_size = Không có ,
                                                    #random_state = Không có , shuffle(xáo trộn) = True , stratify(phân tầng) = Không có )[nguồn]
from sklearn.metrics import mean_squared_error#Mất hồi quy lỗi trung bình bình phương.
import numpy as np #tính toán các mảng nhiều chiều, có kích thước lớn với các hàm đã được tối ưu áp dụng lên các mảng nhiều chiều đó
import pandas as pd #hỗ trợ cho các mảng đa chiều
import matplotlib.pyplot as plt #thư viện vẽ đồ thị rất mạnh mẽ hữu ích


data = pd.read_csv("data__oto.csv", delimiter=',') # mở ra để đọc file chứa dấu phân cách  ,
print(data)
X = np.array(data[['SOCHO','CDAI','CRONG','CCAO','SOXILAH','KTDONGCO','TILENEN','MALUC']].values)# X là ma trận đặc trưng 
Y = np.array(data['GIA']).T # y là ma trân đầu ra

regr1 = linear_model.LinearRegression() #Bình phương nhỏ nhất thông thường Hồi quy tuyến tính.#Biến regr chứa một đối tượng LinearRegression trong bộ thư viện Scikit-learn
xtrain, xtest, ytrain, ytest = train_test_split(X,Y,train_size=0.7, shuffle = False)#Chia mảng hoặc ma trận thành tập hợp con thử nghiệm và huấn luyện ngẫu nhiên# chia data theo tỷ lệ
print("Train: \n")
print(xtrain,'\n',ytrain)
print("Test: \n")
print(xtest,'\n',ytest)
regr1.fit(xtrain,ytrain) #use hồi quy_Fit() thực hiện tính toán tối ưu hóa các tham số θ0 và θ1, phương thức này trả về một model
w_0=regr1.intercept_    # số hạng đập lập trong mô hình tuyến tính
print('w_0 = ',w_0,'\n')
w_1=regr1.coef_			# hệ số ước lượng 
print('w_1 = ',w_1,'\n')

pre=[]
for i in range(len(ytest)):
    kqDuDoan = np.dot(w_1, xtest[i]) + w_0    #tính kqddoan
    pre.append(kqDuDoan)
    print('Với xtest là ' + str(xtest[i]) + ' thì kết quả dự đoán là '+ str(round(kqDuDoan,2)) + ' kết quả thực tế là '+ str(ytest[i]) + '\n')
    print('Sai lệch : ',round(abs(ytest[i] - round(kqDuDoan,2)),2),'\n')# hàm làm tròn đến 2 chữ thập phân
                        # trả về giá trị tuyệt đối

plt.style.use('dark_background')
plt.title("Đồ thị biểu diễn giá xe")
plt.ylabel("Giá xe")
plt.plot(ytest,'red')#vẽ đường thẳng y thực tế
plt.plot(pre,'blue')#vẽ đth y dự đoán
plt.show()









