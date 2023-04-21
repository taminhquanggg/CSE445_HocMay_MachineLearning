from __future__ import print_function 
import numpy as np
import pandas as pd
import sklearn.tree as tr
import library as lb
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('Housing_data_price.csv', parse_dates = True)
X = np.array(data[['bedrooms','bathrooms','stories','guestroom','basement','hotwaterheating','airconditioning','parking','prefarea','furnishingstatus']].values)    
y = np.array(data['price_segment']).T

for i, j in enumerate(X):
	for k in range(3,10):
		if(j[k] == "yes"):
			j[k] = 3
		elif(j[k] == "no"):
			j[k] = 1
		elif(j[k] == "furnished"):
			j[k] = 4
		elif(j[k] == "semi-furnished"):
			j[k] = 5
		elif(j[k] == "unfurnished"):
			j[k] = 6

classifier = DecisionTreeClassifier()
classifier.fit(X,y)
y_pred = classifier.predict(X)
print( y_pred)
