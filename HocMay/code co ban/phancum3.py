import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
dataset = datasets.load_iris()
dataset.data[0:6]
X = dataset.data
y = dataset.target
target_names = dataset.target_names
kmeans = KMeans(n_clusters=3).fit(X)
X_r = kmeans.predict(X)
print(X_r)

plt.figure()
colors = ['blue', 'green', 'red']
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X[y == i, 0], X[y == i, 1], color=color, alpha=0.8, lw=lw,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA of IRIS dataset')
plt.show()
