import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = {
    "Age":[22,25,np.nan,30,28],
    "Salary":[30000,40000,50000,np.nan,60000],
    "City":["Hyderabad","Delhi","Delhi","Mumbai","Hyderabad"]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

# Missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Encoding
le = LabelEncoder()
df["City"] = le.fit_transform(df["City"])

# Scaling
scaler = StandardScaler()
df[["Age","Salary"]] = scaler.fit_transform(df[["Age","Salary"]])

print("\nProcessed Data")
print(df)

# Split
X = df[["Age","Salary"]]
y = df["City"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data")
print(X_train)

print("\nTesting Data")
print(X_test)