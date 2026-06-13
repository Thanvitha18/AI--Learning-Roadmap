import matplotlib.pyplot as plt
days=[1,2,3,4,5]
product_a=[100,180,200,150,250]
product_b=[80,100,190,200,300]
plt.plot(days,product_a,color="yellow",marker="*",label="Product A")
plt.plot(days,product_b,color="gray",marker="^",label="Product B")
plt.title("Sales comparsion of two products")
plt.xlabel("Days")
plt.ylabel("Sales amount")
plt.legend()
plt.grid()
plt.show()