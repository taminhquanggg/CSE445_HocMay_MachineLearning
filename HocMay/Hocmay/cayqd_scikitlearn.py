from __future__ import print_function 
from os import read
import pandas as pd
import numpy as np
import sklearn.tree as tr
import pydotplus as py
import matplotlib.pyplot as pl
from PIL import Image
import library as lb

data = pd.read_csv('thoitiet.csv', index_col = 0, parse_dates = True)

cotdata = ['outlook','temperature','humidity','wind']
x=data[cotdata]
y=data['play']
dtree = tr.DecisionTreeClassifier()
dtree= dtree.fit(x,y)
fig=pl.figure(figsize=(35,30))
_=tr.plot_tree(dtree)
fig.savefig('cay123.png')
print('end.')