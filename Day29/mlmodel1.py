import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[2], [3], [5], [7]])
y = np.array([40, 50, 70, 90])
model=LinearRegression()
model.fit(X,y)
prediction = model.predict([[6]])
print(prediction)
print(model.coef_)
print(model.intercept_)