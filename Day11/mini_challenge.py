import matplotlib.pyplot as plt
students=["Asha","Rahul","Rohan","Jhon","Ravi"]
marks=[80,95,90,75,88]
plt.bar(students,marks,color="Red",edgecolor="Black")
plt.title("Student Marks")
plt.xlabel("students")
plt.ylabel("marks")
plt.show()
hours=[2,4,6,8,10]
marks=[80,95,90,75,88]
plt.scatter(hours,marks,color="green",marker="o",s=200)
plt.title("student studied hours")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.grid()
plt.show()
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 85, 70, 75, 60]
plt.hist(marks,bins=5,color="Green",edgecolor="black")
plt.title("Marks Distrubtion")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid()
plt.show()
