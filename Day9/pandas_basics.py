import pandas as pd
data={
    "name":["ram","sita","krishna","radha","shiva"],
    "Branch":["CSE","ECE","CSE","CAI","MEC"],
    "Marks":[95,80,75,94,82]
}
df=pd.DataFrame(data)
print(df)
print(df.head(3))
print(df.tail(2))
print(df.info())
print(df.describe())
print(df["Marks"])
print(df.loc[2])



