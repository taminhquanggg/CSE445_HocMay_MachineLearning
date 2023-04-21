from sklearn import datasets
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

X = pd.read_csv("TANH3.csv") 

pca=PCA(n_components=21)
X_r=pca.fit(X).transform(X)
print(X_r)
print(pca.explained_variance_ratio_)
df=pd.DataFrame(X_r)

df1=pd.DataFrame(pca.explained_variance_ratio_)
mean_vec = np.mean(X_r, axis=0)
cov_mat = (X_r - mean_vec).T.dot((X_r - mean_vec)) / (X_r.shape[0]-1)
print('Covariance matrix n%s' %cov_mat)
cov_mat = np.cov(X_r.T)
eig_vals, eig_vecs = np.linalg.eig(cov_mat)
print('Eigenvectors n%s' %eig_vecs)
print('nEigenvalues n%s' %eig_vals)
df2=pd.DataFrame(eig_vals)
Y=df.to_csv("kq.csv")
Y1=df1.to_csv("kq1.csv")
Y2=df2.to_csv("kq2.csv")

