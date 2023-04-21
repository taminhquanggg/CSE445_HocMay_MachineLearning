from sklearn import datasets, linear_model
import numpy as np
#import matplotlib.pyplot as plt
# height (cm), input data, each row is a data point
X1 = np.array([[165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y1 = np.array([ 59, 60, 62, 63, 64, 66, 67, 68])
# Building Xbar

# fit the model by Linear Regression
regr1 = linear_model.LinearRegression()
regr1.fit(X1, y1) # in scikit-learn, each sample is one row


# Compare two results
#print('scikit-learn’s solution : w_1 = ', regr.coef_[0], 'w_0 = ', regr.intercept_)
w_10=regr1.intercept_
w_11=regr1.coef_[0]

X2 = np.array([[147, 150, 153, 158, 163, 175, 178, 180, 183]]).T
# weight (kg)
y2 = np.array([ 49, 50, 51, 54, 58, 64, 66, 67, 68])

regr2 = linear_model.LinearRegression()
regr2.fit(X2, y2) # in scikit-learn, each sample is one row

w_20=regr2.intercept_
w_21=regr2.coef_[0]

X3 = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173]]).T
# weight (kg)
y3 = np.array([ 49, 50, 51, 54, 58, 59, 60, 62, 63])

regr3 = linear_model.LinearRegression()
regr3.fit(X3, y3) # in scikit-learn, each sample is one row

w_30=regr3.intercept_
w_31=regr3.coef_[0]

weights = [49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68]
heights = [147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180,183]


#X1
Cv1 = 0

for x in range(13):

    delta =  (weights[x] -  (w_11*heights[x] + w_10))
    Cv1 = Cv1 + delta * delta

print("Cv1: ",Cv1)

#X2
Cv2 = 0

for x in range(13):

    delta =  (weights[x] - (w_21*heights[x] + w_20))
    Cv2 = Cv2 + delta * delta

print("Cv2: ",Cv2)

#X3
Cv3 = 0

for x in range(13):

    delta =  (weights[x] -  (w_31*heights[x] + w_30))
    Cv3 = Cv3 + delta * delta

print("Cv3: ",Cv3)
y1 = w_21*180 + w_20
y2 = w_21*183 + w_20
print('Input 180cm, true output 67kg, predicted output %.2fkg' %(y1) )
print('Input 183cm, true output 68kg, predicted output %.2fkg' %(y2) )
