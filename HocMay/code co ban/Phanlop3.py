sklearn.tree.DecisionTreeClassifier(criterion='gini',  splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0,  max_features=None, random_state=None,  max_leaf_nodes=None, class_weight=None, presort=False)
from sklearn.datasets import load_iris
iris = load_iris()
iris.data
iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( iris.data, iris.target, test_size = 0.3)
# test_size: 30% là test data còn lại 70% để làm train data.
from sklearn import tree
clf = tree.DecisionTreeClassifier(max_depth=3)
clf = clf.fit(X_train, y_train)
predicted = clf.predict(X_test)
predicted
sum(predicted==y_test)/float(len(y_test))
tree.export_graphviz(clf, out_file="tree.dot",feature_names=iris.feature_names,class_names=iris.target_names,filled=True, rounded=True)
#pip install pydotplus
#import pydotplus
#dot_data = tree.export_graphviz(clf , out_file = None , filled = True , rounded = True , special_characters = True)
#graph = pydotplus.graph_from_dot_data(dot_data)
#graph.write_pdf("graph.pdf")