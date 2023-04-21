#Python
#Import Library
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
dataset = datasets.load_iris()
dataset.data[0:6]
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create logistic regression object
model = LogisticRegression()
# Train the model using the training sets and check score
X=dataset.data
Y=dataset.target
model.fit(X, Y)
model.score(X, Y)
#Equation coefficient and Intercept
print('Coefficient: \n', model.coef_)
print('Intercept: \n', model.intercept_)
#Predict Output
predicted= model.predict(X)
print(predicted)