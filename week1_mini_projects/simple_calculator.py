def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2
def power(n1,n2):
    return n1**n2

print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n"
      "5. power\n"
      "6. Exit\n")
while True:

    sel = int(input("Select operation (1-6): "))
    if sel == 6:
        print("Thank you for using the calculator!")
        break

    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    if sel == 1:
        print(n1, "+", n2, "=", add(n1, n2))
    elif sel == 2:
        print(n1, "-", n2, "=", sub(n1, n2))
    elif sel == 3:
        print(n1, "*", n2, "=", mul(n1, n2))
    elif sel == 4:
        if n2 != 0:
            print(n1, "/", n2, "=", div(n1, n2))
        else:
            print("Cannot divide by zero")
    elif sel== 5:
        print(n2,"**",n2,"=",power(n1,n2))
    else:
        print("Invalid input")