import pandas as pd
data={
    "Name":["alice","bob","Jhon","Jhon","Ravi"],
    "Age":[20,None,21,21,23],
    "City":["Delhi","Mumbai","Chicago","Chicago"," Andhra  "]
}
df=pd.DataFrame(data)
print("Original Data:")
print(df)
print("\nMissing values")
print(df.isnull().sum())
print(df["Age"].isnull().sum())
df["Age"]=df["Age"].fillna(22)
df.drop_duplicates(inplace=True)
df["City"]=df["City"].str.strip()
df["City"]=df["City"].str.upper()
df.rename(columns={"Name":"Persons"},inplace=True)
print("Cleared data")
print(df)
