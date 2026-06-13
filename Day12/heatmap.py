import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
correlation= tips.corr(numeric_only=True)
sns.heatmap(correlation,annot=True)
plt.title("Correlation Heatmap of Tips Dataset")
plt.show()