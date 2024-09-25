from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
import numpy as np
iris = datasets.load_iris()
X = iris.data
y = iris.target
clf = DecisionTreeClassifier()
clf.fit(X, y)
sepal_length = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_length = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))
new_flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = clf.predict(new_flower)
species = iris.target_names[prediction][0]
print(f"Predicted species: {species}")
