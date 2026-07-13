from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
X = np.array([
    [2],
    [4],
    [6],
    [8],
    [10],
    [12]
])

y = np.array([
    0,
    0,
    0,
    1,
    1,
    1
])
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
model = LogisticRegression()

model.fit(X_train, y_train)
prediction=model.predict([[7]])
print(prediction)
prediction=model.predict(X_test)
accuracy=accuracy_score(y_test,prediction)
print("accuracy:",accuracy)
