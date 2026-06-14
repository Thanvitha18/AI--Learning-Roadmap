import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
print("Average Bill")
print(tips["total_bill"].mean())
print("Smoker Count:")
print(tips["smoker"].value_counts())
print("Average tip per day:")
print(tips.groupby("day")["tip"].mean())
print(tips.columns)