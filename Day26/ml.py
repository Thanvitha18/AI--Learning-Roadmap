from sklearn.linear_model import LinearRegression
import numpy as np
X=np.array([[2],[3],[5],[7]])
Y=np.array([40,50,70,90])
model=LinearRegression()
model.fit(X,Y)
prediction=model.predict([[6]])
print(f"predicted marks for 6 hrs:{prediction[0]:.2f}")
