import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("week2_mini_project/netflix.csv")

# Data Cleaning
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df = df.dropna(subset=["date_added"])
df["rating"] = df["rating"].fillna(df["rating"].mode()[0])
df = df.dropna(subset=["duration"])

# Create dashboard
plt.figure(figsize=(15,10))

# 1. Movies vs TV Shows
plt.subplot(2,2,1)
sns.countplot(x="type", data=df)
plt.title("Movies vs TV Shows")

# 2. Top 5 Countries
plt.subplot(2,2,2)
sns.countplot(
    y="country",
    data=df,
    order=df["country"].value_counts().head(5).index
)
plt.title("Top 5 Countries")

# 3. Top Ratings
plt.subplot(2,2,3)
sns.countplot(
    y="rating",
    data=df,
    order=df["rating"].value_counts().head(5).index
)
plt.title("Most Common Ratings")

# 4. Release Year Trend
plt.subplot(2,2,4)
year_count = df["release_year"].value_counts().sort_index()
sns.lineplot(x=year_count.index, y=year_count.values)
plt.title("Release Year Trend")
plt.xlabel("Year")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.show()