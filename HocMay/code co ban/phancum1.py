from sklearn import datasets
from sklearn import metrics
from sklearn.cluster import KMeans

dataset = datasets.load_iris()
dataset.data[0:6]
X = dataset.data
Y=dataset.target
print(Y)
kmeans = KMeans(n_clusters=3).fit(X)
pred_label = kmeans.predict(X)
print(pred_label)