import seaborn as sns
import matplotlib.pyplot as plt
day=[1,1,1,1,2,2,3,3,3]
sns.countplot(x=day)
plt.title("Number of records for 3 Days")
plt.xlabel("Day")
plt.ylabel("Count")
plt.show()
