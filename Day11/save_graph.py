import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [100, 150, 200, 180, 250]

plt.plot(days, sales, color="Red", marker="o")

plt.title("Sales Report")
plt.xlabel("Days")
plt.ylabel("Sales")

plt.savefig("Day11/sales_graph.png",dpi=300)

plt.show()