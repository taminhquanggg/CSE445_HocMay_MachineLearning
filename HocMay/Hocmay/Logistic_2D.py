from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
np.random.seed(22)

# X = np.array([[0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50, 
#               2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50]])
# y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

# # extened data 
# X = np.concatenate((np.ones((1, X.shape[1])), X), axis = 0)

#một mảng numpy trả về hàm sigmoid của mỗi phần tử của S
def sigmoid(s):
    return 1/(1 + np.exp(-s))

# 10000 là số vòng lặp tối đa.Trong nhiều trường hợp ta không cần chạy tới 10000 vòng mà chỉ cần vài vòng là nghiệm đã hội tụ. Nếu nghiệm hội tụ rồi mà cứ chạy tiếp thì sẽ mất thời gian, nên ta cần xem xem khi nào thì dừng được.
#  Tol chính là một cách để kiểm tra điều kiện đó./ 
def logistic_sigmoid_regression(X, y, w_init, eta, tol = 1e-4, max_count = 10000):
    w = [w_init]    
    it = 0
    N = X.shape[1]
    d = X.shape[0]
    count = 0
    check_w_after = 20
    while count < max_count:
#         it += 1
        # mix data 
        mix_id = np.random.permutation(N)
        for i in mix_id:
            xi = X[:, i].reshape(d, 1)
            yi = y[i]
            zi = sigmoid(np.dot(w[-1].T, xi))
            w_new = w[-1] + eta*(yi - zi)*xi
            count += 1
            # stopping criteria
            if count%check_w_after == 0:                
                if np.linalg.norm(w_new - w[-check_w_after]) < tol:
                    return w
            w.append(w_new)
    return w
# eta = .05 
# d = X.shape[0]
# w_init = np.random.randn(d, 1)

# w = logistic_sigmoid_regression(X, y, w_init, eta)
# print(w[-1])
# print(sigmoid(np.dot(w[-1].T, X)))
# X0 = X[1, np.where(y == 0)][0]
# y0 = y[np.where(y == 0)]
# X1 = X[1, np.where(y == 1)][0]
# y1 = y[np.where(y == 1)]

# plt.plot(X0, y0, 'ro', markersize = 8)
# plt.plot(X1, y1, 'bs', markersize = 8)

# xx = np.linspace(0, 6, 1000)
# w0 = w[-1][0][0]
# w1 = w[-1][1][0]
# threshold = -w0/w1
# yy = sigmoid(w0 + w1*xx)
# plt.axis([-2, 8, -1, 2])
# plt.plot(xx, yy, 'g-', linewidth = 2)
# plt.plot(threshold, .5, 'y^', markersize = 8)
# plt.xlabel('studying hours')
# plt.ylabel('predicted probability of pass')
# plt.savefig('lg_results.png', bbox_inches='tight', dpi = 300)
# plt.show()

means = [[2, 2], [4, 2]]
cov = [[.7, 0], [0, .7]]
N = 20
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)

plt.plot(X0[:, 0], X0[:, 1], 'bs', markersize = 8, alpha = 1)
plt.plot(X1[:, 0], X1[:, 1], 'ro', markersize = 8, alpha = 1)
plt.axis('equal')
plt.ylim(0, 4)
plt.xlim(0, 5)

# hide tikcs 
cur_axes = plt.gca()
cur_axes.axes.get_xaxis().set_ticks([])
cur_axes.axes.get_yaxis().set_ticks([])

plt.xlabel('$x_1$', fontsize = 20)
plt.ylabel('$x_2$', fontsize = 20)
plt.savefig('logistic_2d.png', bbox_inches='tight', dpi = 300)
plt.show()


X = np.concatenate((X0, X1), axis = 0).T
y = np.concatenate((np.zeros((1, N)), np.ones((1, N))), axis = 1).T
# Xbar 
Xbar = np.concatenate((np.ones((1, 2*N)), X), axis = 0)

eta = .05 
d = Xbar.shape[0]
w_init = np.random.randn(d, 1)

w = logistic_sigmoid_regression(X, y, w_init, eta, tol = 1e-4, max_count= 10000)
print(w[-1])
xm = np.arange(-1, 6, 0.025)
xlen = len(xm)
ym = np.arange(0, 4, 0.025)
ylen = len(ym)
xm, ym = np.meshgrid(xm, ym)
w0 = w[-1][0][0]
w1 = w[-1][1][0]
w2 = w[-1][2][0]
zm = sigmoid(w0 + w1*xm + w2*ym)

CS = plt.contourf(xm, ym, zm, 200, cmap='jet')

plt.plot(X0[:, 0], X0[:, 1], 'bs', markersize = 8, alpha = 1)
plt.plot(X1[:, 0], X1[:, 1], 'ro', markersize = 8, alpha = 1)
plt.axis('equal')
plt.ylim(0, 4)
plt.xlim(0, 5)

# hide tikcs 
cur_axes = plt.gca()
cur_axes.axes.get_xaxis().set_ticks([])
cur_axes.axes.get_yaxis().set_ticks([])

plt.xlabel('$x_1$', fontsize = 20)
plt.ylabel('$x_2$', fontsize = 20)
plt.savefig('logistic_2d_2.png', bbox_inches='tight', dpi = 300)
plt.show()