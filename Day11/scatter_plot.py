import matplotlib.pyplot as plt
hours=[1,2,3,4,5,6,7,8]
marks=[35,40,50,55,60,80,90,95]
plt.scatter(hours,marks,color="red",marker="^",s=300)
plt.title("StudyHours VS Marks")
plt.xlabel("Num of hrs studied")
plt.ylabel("Marks Scored")
plt.grid()
plt.show()