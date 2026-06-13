import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [100, 150, 200, 180, 250]

plt.plot(days, sales)

plt.show()
plt .plot(days,sales,color="purple",marker="^",linestyle="-.")
plt.title("Sales growth over 5 Days")
plt.xlabel("Days")
plt.ylabel("sales amount")
plt.show()