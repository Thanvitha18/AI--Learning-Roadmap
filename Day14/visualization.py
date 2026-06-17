import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("Day14/tested.csv")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Fare"] = df["Fare"].fillna(df["Fare"].mean())
df = df.drop("Cabin", axis=1)
plt.figure(figsize=(8,5))
sns.countplot(x=df["Survived"])
plt.title("Survival Count")
plt.xlabel("Survival Status (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
ax = sns.countplot(x=df["Pclass"])

for i in ax.containers:
    ax.bar_label(i)

plt.show()
plt.figure(figsize=(8,5))
sns.histplot(df["Age"],bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.show()
plt.figure(figsize=(8,5))
sns.boxplot(x=df["Fare"])
plt.title("Fare distribution")
plt.xlabel("Ticket Fare")
plt.show()
plt.figure(figsize=(8,5))
sns.countplot(x=df["Pclass"],hue=1)
plt.title("Passenger Class Count")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
ax = sns.countplot(x=df["Pclass"],hue=df["Survived"])

for i in ax.containers:
    ax.bar_label(i)

plt.show()
sns.countplot(x=df["Sex"],hue=df["Survived"])
plt.title("Survival by Gender")
ax = sns.countplot(x=df["Sex"])

for i in ax.containers:
    ax.bar_label(i)

plt.show()
print(df["Survived"].value_counts())
plt.figure(figsize=(8,5))
sns.countplot(x="Pclass", hue="Survived",data=df)
plt.title("Passenger Class vs Survival")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.legend(title="Survived", labels=["No (0)", "Yes (1)"])
plt.show()
#insights
print( df.groupby("Pclass")["Survived"].mean() )

print(df.groupby("Pclass")["Survived"].value_counts())
print("1st class had the highest survival rate , meaning a passenger in first calss had a better chance of survival")
print(df.groupby("Sex")["Survived"].value_counts())

print(df.groupby("Sex")["Survived"].mean())
print("This results look unusual.Let me check what dataset i am using")

print(df.groupby("Survived")["Age"].value_counts())
print(df.groupby("Survived")["Age"].mean())
plt.figure(figsize=(8,5))

sns.boxplot(x="Survived", y="Age", data=df)

plt.title("Age Distribution Based on Survival")
plt.xlabel("Survival (0 = No, 1 = Yes)")
plt.ylabel("Age")

plt.show()
print(df.groupby("Survived")["Fare"].mean())
sns.boxplot(x="Survived", y="Fare", data=df)
plt.title("Fare vs Survival")
plt.show()
print("Passengers who survived paid a much higher average fare compared to those who did not survive." )
