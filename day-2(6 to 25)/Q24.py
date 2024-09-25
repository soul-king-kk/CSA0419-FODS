import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
data = np.array([[1, 2], [2, 3], [3, 3], [5, 5], [6, 5], [7, 8]])  
labels = np.array([0, 0, 1, 1, 1, 1])
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
k = int(input("Enter the number of neighbors (k): "))
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
new_patient = list(map(float, input("Enter the features of the new patient (comma-separated): ").split(',')))
prediction = knn.predict([new_patient])
print(f"Predicted condition: {prediction[0]} (0 = No, 1 = Yes)")
