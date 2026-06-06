def numcheck(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
n=int(input("enter number to check:"))
result=numcheck(n)
print(result)