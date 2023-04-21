from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
# height (cm), input data, each row is a data point
# mtran dau vao(mtran dac trung)
X = np.array([[147, 155, 153, 158, 160, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg) ma tran dau ra
y = np.array([ 49, 52, 51, 54, 56, 59, 60, 62, 63, 64, 66, 67, 68])
# plt.plot(X,y,"go")
# plt.xlim(140,190)
# plt.ylim(45,75)
# plt.xlabel("height")
# plt.ylabel("weight")
# plt.title("LinearRe Cân nặng")
# plt.show()
# Building Xbar
#ma tran dơn vi
one = np.ones((X.shape[0], 1))
# ghép 2 matran vs nhau(one và x:có cùng số hàng giống nhau)
# ghep theo hang axis = 1,theo cot axis = 0
Xbar = np.concatenate((one, X), axis = 1) 
print(Xbar)
# Calculating weights of the fitting line
A = np.dot(Xbar.T, Xbar)  # nhan x vs x chuyen vi cua no
b = np.dot(Xbar.T, y)     # nhan x vs y
w = np.dot(np.linalg.pinv(A), b) # nhan 2 ma tran-ham tinh toan matran nghich đảo của A
# weights
w_0, w_1 = w[0], w[1]
y1 = w_1*150 + w_0
y2 = w_1*163 + w_0

print('Input 150cm, true output 50kg, predicted output %.2fkg' %(y1) )
print('Input 163cm, true output 58kg, predicted output %.2fkg' %(y2) )

