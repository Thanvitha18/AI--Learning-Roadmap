from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Training data
X = np.array([[20], [40], [60], [80]])
y = np.array(["No", "No", "Yes", "Yes"])

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[50]])

print("Prediction:", prediction)