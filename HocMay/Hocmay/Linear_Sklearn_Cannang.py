from sklearn import datasets, linear_model
import numpy as np

# height (cm)-mtran dau vao
X = np.array([[147, 155, 153, 158, 160, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)-ma tran dau ra
y = np.array([ 49, 52, 51, 54, 56, 59, 60, 62, 63, 64, 66, 67, 68])
 
#ham hoi quy tuyen tinh
regr = linear_model.LinearRegression()#Biến regr chứa một đối tượng LinearRegression trong bộ thư viện Scikit-learn

regr.fit(X, y)#Fit() thực hiện tính toán tối ưu hóa các tham số w_0 và w_1, phương thức này trả về một model

print('scikit-learns solution : w_1 = ',regr.coef_[0], 'w_0 = ',regr.intercept_)

w_0=regr.intercept_
w_1=regr.coef_[0]

y1 = w_1*150 + w_0
y2 = w_1*163 + w_0

print('Input 150cm, true output 50kg, predicted output %.2fkg' %(y1) )
print('Input 163cm, true output 58kg, predicted output %.2fkg' %(y2) )