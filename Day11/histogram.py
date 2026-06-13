import matplotlib.pyplot as plt
marks=[45,50,55,60,65,70,75,80,85,90,95,75,70,80,85]
plt.hist(marks,bins=10,color="Purple",edgecolor="Black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("frequency")
plt.show()
