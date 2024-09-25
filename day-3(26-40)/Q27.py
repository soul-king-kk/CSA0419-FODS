import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
data = pd.read_csv("D:/Slot-D/fods/code/Q27sample.csv")
X = data[['Usage Minutes', 'Contract Duration']]
y = data['Churn Status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
for i, churn in enumerate(predictions):
    print(f'Customer {i + 1} will churn: {churn}')
