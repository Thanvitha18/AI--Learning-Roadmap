import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
sns.boxplot(x=tips["total_bill"])
plt.title("Total bill Analysis")
plt.xlabel("Total Bill")
plt.show()
