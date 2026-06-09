class number:
    def __init__(self,num):
        self.num=num
    def check_even_odd(self):
        if self.num%2==0:
            print("even")
        else:
            print("odd")
n1=number(8)
n1.check_even_odd()
n2=number(7)
n2.check_even_odd()
#to check prime number
class Number:
    def __init__(self, num):
        self.num = num

    def check_prime(self):

        if self.num <= 1:
            print("Not Prime")
            return

        for i in range(2, self.num):
            if self.num % i == 0:
                print("Not Prime")
                return

        print("Prime")
n1 = Number(7)
n1.check_prime()

n2 = Number(8)
n2.check_prime()

n3 = Number(11)
n3.check_prime()
#rectangle
class rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area_perimeter(self):
        area=self.length*self.width
        print("area:",area)
        perimeter=2*(self.length+self.width)
        print("Perimeter:",perimeter)

r1=rectangle(7,8)
r1.area_perimeter()
#bank account details
class Bankaccount():

    def __init__(self,depoist,withdraw,amount):
        self.depoist=depoist
        self.withdraw=withdraw
        self.amount=amount
    def check_balance(self):
        balance=(self.depoist+self.amount)-self.withdraw
        print("Balance:",balance)
bc=Bankaccount(500,200,1000)
bc.check_balance()
#student clas
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("student:",self.name)
    def result(self):
        if self.marks>=35:
            print("pass")
        else:
            print("Fail")
s1=Student("Thanvitha",95)
s1.display()
s1.result()
#inhertiance
class Vehicle:

    def start(self):
        print("Vehicle Started")

class Bike(Vehicle):
    pass

b = Bike()
b.start()
class Vehicle:

    def start(self):
        print("Vehicle Started")

class Bike(Vehicle):

    def start(self):
        print("Bike Started")

b = Bike()
b.start()
#polymorphism
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()

    

