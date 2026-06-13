import matplotlib.pyplot as plt
categories=["Electricty","Food","Travel","Fees","Others"]
expenses=[40,35,10,15,5]
plt.pie(expenses,labels=categories,colors=["Blue","Purple","Green","Yellow","pink"],autopct="1%.1f%%")
plt.title("Daily expenses")
plt.show()