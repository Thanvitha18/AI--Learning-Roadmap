import seaborn as sns
import matplotlib.pyplot as plt
tips=[1,2,2,2,3,3]
tips=sns.load_dataset("tips")
sns.boxplot(x=tips["total_bill"])
plt.title("Total bill Analysis")
plt.xlabel("Total Bill")
plt.show()
