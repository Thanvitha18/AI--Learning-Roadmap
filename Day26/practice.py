from sklearn.linear_model import LinearRegression
import numpy as np
#Training data
x=np.array([[2],[3],[5],[7]])
y=np.array([40,50,70,90])
#creates the model
model=LinearRegression()
model.fit(x,y )#Train the model
prediction=model.predict([[4],[6],[8]])#Make a prediction
hours = [4, 6, 8]

for hour, mark in zip(hours, prediction):
    print(f"Predicted marks for {hour} hours: {mark:.2f}")
    
print(x.shape)
print(y.shape)
print("Slope:", model.coef_)
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)
print("R² Score:", model.score(x, y))
