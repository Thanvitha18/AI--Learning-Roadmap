#creating a set
num={10,20,30,40}
#adding the elements
num.add(60)
print(num)
#removng elements
num.remove(60)
print(num)
#length of set
print(len(num))
#looping through set
for number in num:
    print(number)
#creating set of fruits
fruits={"apple","mango","cherry","avacado"}
fruits.add("starwberry")
print("after adding a fruit:",fruits)
fruits.remove("avacado")
print("after removing a fruit:",fruits)