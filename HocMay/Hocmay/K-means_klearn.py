from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plot
from matplotlib.pyplot import style
style.use("seaborn-darkgrid")
#df = np.array([[2,10],[2,5],[8,4],[8,5], [7,5], [6,4], [1,2], [4,9]])
df = np.array([[2,8],[2,5],[1,2],[5,8], [7,3], [6,4], [8,4], [4,7]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(df)
pointcenter = kmeans.cluster_centers_
label = kmeans.labels_
print('Centers found by scikit-learn:',pointcenter )
print(label)
pred_label = kmeans.predict(df)
print(pred_label)

colours = ['m.','g.','r.', 'k.']
for i in range(len(df)):
    #print "Coordinates ", a[i], "labels", label[i]
    plot.plot(df[i][0], df[i][1], colours[label[i]], markersize = 10 )
for i in range(len(pointcenter)):
    plot.plot(pointcenter[i][0], pointcenter[i][1], colours[i], markersize = 12, marker='*' )
plot.show()

