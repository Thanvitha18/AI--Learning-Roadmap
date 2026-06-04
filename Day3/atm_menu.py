balance=10000.0
while True:
    print("---ATM Menu---")
    print("1.check balance")
    print("2.withdraw")
    print("3.exit")
    choice = input("enter the choice of(1 to 3):")
    if choice=="1":
        print("current balance is {balance:.2f}")
    elif choice=="2":
        amount = float(input("enter withdrawl amount"))
        if amount>balance:
            print("insufficeint amount ... transcation cancled")
        elif amount<=0:
            print("invalid amount.. transcantion failed")
        else :
            balance-=amount
            print(f"please collect ur cash{amount:.2f}withdrawn")
    elif choice=="3":
        print("thank you for visting")
        break
    else:
        print("invalid choice:please select a valid option from 1 to 3")
