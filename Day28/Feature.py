import pandas as pd
data={
    "Math": [80, 65, 90],
    "Science": [70, 75, 85]
}
df=pd.DataFrame(data)
df["Avg"]= (df["Math"] + df["Science"]) / 2
print(df)