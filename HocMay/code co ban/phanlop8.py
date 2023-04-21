#Python
#Import Library
from sklearn import datasets
from sklearn import metrics
from sklearn import tree
dataset = datasets.load_iris()
dataset.data[0:6]
X=dataset.data
Y=dataset.target
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create tree object
model = tree.DecisionTreeClassifier(criterion='gini') # for classification, here you can change the algorithm as gini or entropy (information gain) by default it is gini
# model = tree.DecisionTreeRegressor() for regression
# Train the model using the training sets and check score
model.fit(X, Y)
model.score(X,Y)
#Predict Output
predicted= model.predict(X)
print(predicted)