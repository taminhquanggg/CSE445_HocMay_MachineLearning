import numpy as np
import pandas as pd
###################################################
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
###################################################
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
###################################################
import form


#-----------------------------------------get_Data------------------------------------------------------- #
data = pd.read_csv("Housing_data_price.csv")
colums = ['bedrooms','bathrooms','stories','mainroad','guestroom','basement','hotwaterheating','airconditioning','parking','prefarea','furnishingstatus']
X = np.array(data[colums].values)    
y = np.array(data['price_segment']).T
#-----------------------------------------convert_data------------------------------------------------------- #
X = form.convert_text_to_number(X)
#-----------------------------------------split data------------------------------------------------------- #
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,shuffle = False)
#-----------------------------------------Use PCA------------------------------------------------------- #
pca = PCA(n_components=8)#Số lượng thành phần cần giữ
X_train_pca = pca.fit_transform(X_train)#Chỉnh mô hình với X và áp dụng giảm kích thước trên X.
X_test_pca = pca.fit_transform(X_test)
#-----------------------------------------Use ID3------------------------------------------------------- #
id3 = DecisionTreeClassifier(criterion='entropy', max_depth= 8,random_state = 105) #
id3.fit(X_train_pca,y_train)
y_pred = id3.predict(X_test_pca)
dem = 0
data_pre = ""
for i in range(len(y_pred)):
	if(y_pred[i] == y_test[i]):
		dem = dem + 1
	data_pre = data_pre + str('Với bộ giá trị ' +  str(X_test[i]) + ' hệ thống dự đoán [' + str(y_pred[i]) + '] thực tế là [' + str(y_test[i]) + ']\n')
data_pre = data_pre + str("Thuật toán ID3 dự đoán đúng được "+ str(dem) + " giá trị trên tổng số " + str(len(y_pred)))
data_pre = data_pre + str("\nDự đoán đúng: ") + str(round(accuracy_score(y_test, y_pred)*100,2)) + "%"
#-------------------------------------evaluation---------------------------------------------------#
precision = str(round(precision_score(y_test, y_pred,average='macro')*100,2))+ "%"#Tính toán số liệu cho từng nhãn và tìm giá trị trung bình không trọng số của chúng. Điều này không tính đến sự mất cân bằng nhãn.
recall = str(round(recall_score(y_test, y_pred,average='macro')*100,2)) + "%"
f1_score = str(round(f1_score(y_test,y_pred,average = 'macro')*100,2)) + "%"

#-----------------------------------------use form with data-----------------------------------------------------------#

name_row= ['Phòng ngủ','Phòng Tắm','Tồn tại','Đường chính','Phòng khách','Tầng hầm','Bình nóng lạnh','Điều Hòa','Bãi đậu xe','Kho','Nội thất']
data_combobox = form.get_Data_combobox(np.array(data[colums].values))
form.Form(name_row,"id3",data_pre,data_combobox,pca,id3.predict,precision,recall,f1_score)
