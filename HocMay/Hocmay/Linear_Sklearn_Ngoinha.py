from sklearn import datasets, linear_model

import numpy as np
import matplotlib.pyplot as plt

# height (cm), input data, each row is a data point

X = np.array([
    [60,2,10],
    [40,2,5],
    [100,3,7]])
print(X)
# weight (kg)

y = np.array([10,12,20])
print(y)
# Building Xbar


# fit the model by Linear Regression

regr = linear_model.LinearRegression()

regr.fit(X, y)

# Compare two results
print('scikit-learn’s solution : w_1 = ', regr.coef_[0], 'w_0 = ', regr.intercept_)

w_0=regr.intercept_

w_1=regr.coef_[0]

a= np.array([50,2,8]).T
y1=np.dot(w_1, a) + w_0
print(y1)
