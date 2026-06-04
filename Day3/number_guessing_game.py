num=1234
while True:
   guess_num=int(input("enter a num to guess:"))
   if guess_num==num:
    print("number you guessed is true")
    break
   else:
    print("Try again")

