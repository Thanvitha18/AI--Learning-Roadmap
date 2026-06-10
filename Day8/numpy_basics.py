import numpy as np
arr=np.array([0,1,2,3,4,5,6,7,8,9])
print(arr)#creating an array of 10 numbers
print("First element: ",arr[0])
print("last element: ",arr[-1])
print("max element: ",np.max(arr))
print("min element: ",np.min(arr))
print("average: ",np.mean(arr))
new_arr=arr.reshape(2,5)
print(new_arr)
#zeros and ones and arange in numpy
print(np.zeros(5))
print(np.ones(5))
print(np.arange(1,8))
#matrix problems
arr1=np.array([1,2,3,4,5])
arr2=np.array([4,5,6,7,8])
print("Addition: ",arr1+arr2)
print("Subtraction: ",arr1-arr2)
print("Square: ",arr1**2)
print(arr1[1:3])
print(arr[:4])
print(arr1[4:])
print(arr1[::-1])

