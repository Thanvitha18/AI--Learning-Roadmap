from sklearn.svm import SVC
import numpy as np

X = np.array([[20], [30], [70], [80]])
y = np.array(["No", "No", "Yes", "Yes"])

model = SVC()

model.fit(X, y)

prediction = model.predict([[50]])

print(prediction)