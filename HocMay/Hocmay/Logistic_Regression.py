#https://github.com/tiepvupsu/tiepvupsu.github.io/blob/master/assets/LogisticRegression/LogisticRegression_post.ipynb
from __future__ import print_function
import numpy as np
import matplotlib as plt

def sigmoid(S):
#S: an numpy array
#return sigmoid function of each element of S
    return 1/(1 + np.exp(-S))

def prob(w, X):
#X: a 2d numpy array of shape (N, d). N datatpoint, each with size d
#w: a 1d numpy array of shape (d)
    return sigmoid(X.dot(w))

def loss(w, X, y, lam): # hàm mất mát
#X, w as in prob
#y: a 1d numpy array of shape (N). Each elem = 0 or 1
    z = prob(w, X)
    return -np.mean(y*np.log(z) + (1-y)*np.log(1-z)) + 0.5*lam/X.shape[0]*np.sum(w*w)

def logistic_regression(w_init, X, y, lam = 0.001, lr = 0.1, nepoches = 2000):
    # lam - reg paramether, lr - learning rate, nepoches - number of epoches
    N, d = X.shape[0], X.shape[1]
    w = w_old = w_init
    loss_hist = [loss(w_init, X, y, lam)] # store history of loss in loss_hist
    ep = 0
    while ep < nepoches:
        ep += 1
        mix_ids = np.random.permutation(N)
        for i in mix_ids:
            xi = X[i]
            yi = y[i]
            zi = sigmoid(xi.dot(w))
            w = w - lr*((zi - yi)*xi + lam*w)
            loss_hist.append(loss(w, X, y, lam))
        if np.linalg.norm(w - w_old)/d < 1e-6:
            break
        w_old = w
    return w, loss_hist

X = np.array([[0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50,
2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50]]).T
y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])
# bias trick
N= X.shape[0]
Xbar = np.concatenate((X, np.ones((N, 1))), axis = 1)
w_init = np.random.randn(Xbar.shape[1])
lam = 0.0001
w, loss_hist = logistic_regression(w_init, Xbar, y, lam, lr = 0.05, nepoches = 500)
print(w)
print(w[0])
print(w[1])
print(loss(w, Xbar, y, lam))

hours = 5
print(sigmoid(w[0]*hours + w[1]))

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

