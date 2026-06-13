import seaborn as sns
import matplotlib.pyplot as plt
hours=[1,2,3,4,5]
marks=[50,60,70,80,90]
sns.scatterplot(x=hours,y=marks,color="red",marker="o",s=200)
plt.show()