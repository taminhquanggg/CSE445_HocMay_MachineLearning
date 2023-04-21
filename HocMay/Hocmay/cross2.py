from sklearn import datasets, linear_model
import numpy as np
#số phòng ngủ,diện tích, khu đô thị 
dactrung = np.array([
    [3,2000,1],
    [2,800,2],
    [2,850,1],
    [1,550,1],
    [4,2000,3]]).T
print(dactrung)
#giá bán
gia = np.array([250,300,150,78,150])
print(gia)
X1=np.array([[3,2000,1],
    [2,800,2],
    [2,850,1],]).T

y1=np.array([250,300,150]);

# fit the model by Linear Regression
regr1 = linear_model.LinearRegression()
regr1.fit(X1, y1) # in scikit-learn, each sample is one row


# Compare two results
#print('scikit-learn’s solution : w_1 = ', regr.coef_[0], 'w_0 = ', regr.intercept_)
w_10=regr1.intercept_
w_11=regr1.coef_[0]

X2=np.array([
    [2,850,1],
    [1,550,1],
    [4,2000,3]]).T

y2=np.array([150,78,150]);

regr2 = linear_model.LinearRegression()
regr2.fit(X2, y2) # in scikit-learn, each sample is one row

w_20=regr2.intercept_
w_21=regr2.coef_[0]

X3=np.array([
    [2,800,2],
    [2,850,1],
    [1,550,1]]).T

y3=np.array([300,150,78]);

regr3 = linear_model.LinearRegression()
regr3.fit(X3, y3) # in scikit-learn, each sample is one row

w_30=regr3.intercept_
w_31=regr3.coef_[0]


#X1
Cv1 = 0

for x in range(13):

    delta =  (gia[x] -  (w_11*dactrung[x] + w_10))
    Cv1 = Cv1 + delta * delta

print("Cv1: ",Cv1)

#X2
Cv2 = 0

for x in range(13):

    delta =  (gia[x] - (w_21*dactrung[x] + w_20))
    Cv2 = Cv2 + delta * delta

print("Cv2: ",Cv2)

#X3
Cv3 = 0

for x in range(13):

    delta =  (gia[x] -  (w_31*dactrung[x] + w_30))
    Cv3 = Cv3 + delta * delta

# print("Cv3: ",Cv3)
# y1 = w_21*180 + w_20
# y2 = w_21*183 + w_20
# print('Input 180cm, true output 67kg, predicted output %.2fkg' %(y1) )
# print('Input 183cm, true output 68kg, predicted output %.2fkg' %(y2) )





# from sklearn import metrics
# import numpy as np
# from sklearn.model_selection import KFold, cross_val_score
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# X = np.array([[0.2,0.1],[0.15,0.13],[0.28,0.17],[0.15,0.1],[0.8,0.7], [0.1,0.3],[0.4,0.4],[0.5,0.5],[0.6,0.6],[0.7,0.6],[0.6,0.64],[0.7,0.65]])
# y = np.array([1,1,1,1,1,1,2,2,2,2,2,2])

# knum = 4
# k_fold = KFold(n_splits=knum, shuffle=True)

# clf = LinearDiscriminantAnalysis()
# sumR = 0

# for train_indices, test_indices in k_fold.split(X):
#     print('Train: %s | test: %s' % (train_indices, test_indices))
#     clf.fit(X[train_indices],y[train_indices])
#     y_pred = clf.predict(X[test_indices])
#     print("Accuracy: ",metrics.accuracy_score(y[test_indices], y_pred))
#     print("y_test: ", y[test_indices])
#     print("y_pred: ", y_pred)
#     sumR += metrics.accuracy_score(y[test_indices], y_pred)
#     print("------------------------------")

# print("1st accuracy = ", sumR/knum)
# scores = cross_val_score(clf, X, y, cv=knum, scoring='accuracy')
# print("K-fold: ", scores)
# print("2nd accuracy: ", scores.mean())