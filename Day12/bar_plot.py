import seaborn as sns
import matplotlib.pyplot as plt
subjects=["maths","science","english"]
Marks=[90,85,95]
sns.barplot(x=subjects,y=Marks)
plt.show()