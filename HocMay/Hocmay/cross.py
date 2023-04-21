from sklearn import datasets, linear_model
import numpy as np
import matplotlib.pyplot as plt

def rate(X, y, w_0, w_1):
    total_rate = 0
    predict = 0
    for i in range(0, 15):
        predict = np.dot(X[i], w_1) + w_0
        total_rate += abs(y[i] - predict)
    return total_rate

# height (cm), input data, each row is a data point
X = np.array([[147, 150, 153, 155, 158, 160, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
X1 = X[:5]
X2 = X[5:10]
X3 = X[10:]
# weight (kg)
y = np.array([ 49, 50, 51, 52, 54, 56, 58, 59, 60, 62, 63, 64, 66, 67, 68])
y1 = y[:5]
y2 = y[5:10]
y3 = y[10:]


# fit the model by Linear Regression
regr = linear_model.LinearRegression()

X12 = np.concatenate((X1,X2), axis = 0)
y12 = np.concatenate((y1,y2), axis = 0)
regr.fit(X12, y12)

w_0=regr.intercept_
w_1=regr.coef_

print("Training:1,2 Test:3 Rate:" + str(rate(X, y, w_0, w_1)) + " w_0:" + str(w_0) + " w_1:" + str(w_1))

X13 = np.concatenate((X1,X3), axis = 0)
y13 = np.concatenate((y1,y3), axis = 0)
regr.fit(X13, y13) 

w_0=regr.intercept_
w_1=regr.coef_

print("Training:1,3 Test:2 Rate:" + str(rate(X, y, w_0, w_1)) + " w_0:" + str(w_0) + " w_1:" + str(w_1))

X23 = np.concatenate((X2,X3), axis = 0)
y23 = np.concatenate((y2,y3), axis = 0)
regr.fit(X23, y23)

w_0=regr.intercept_
w_1=regr.coef_

print("Training:2,3 Test:1 Rate:" + str(rate(X, y, w_0, w_1)) + " w_0:" + str(w_0) + " w_1:" + str(w_1))



