import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
k = int(input("Enter the number of neighbors (k): "))
features = []
for i in range(len(X_train[0])):
    feature = float(input(f"Enter feature {i+1}: "))
    features.append(feature)
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_scaled, y_train)
input_scaled = scaler.transform(np.array(features).reshape(1, -1))
prediction = knn.predict(input_scaled)

print(f"Prediction: {'Condition present' if prediction[0] == 1 else 'No condition'}")
