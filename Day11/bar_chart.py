import matplotlib.pyplot as plt
products=["laptop","mobile","tablet","watch"]
sales=[80,50,30,40]
plt.bar(products,sales,color="Yellow",edgecolor="red")
plt.title("Product sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()
