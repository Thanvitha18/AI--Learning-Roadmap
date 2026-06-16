import pandas as pd
df=pd.read_csv("Day14/tested.csv")
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Fare"]=df["Fare"].fillna(df["Fare"].mean())
df=df.drop("Cabin",axis=1)
print(df.isnull().sum())