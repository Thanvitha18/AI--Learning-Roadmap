students=["jhon","meera","sara"]
print(students)
#accessing elements
print(students[0])
print(students[-1])
#modifying elements
students[0]="ashwin"
print(students)
#adding elements
students.append("megha")
print(students)
#removing elements
students.remove("ashwin")
print(students)
#length of a list
print(len(students))
#looping through a  list
for student in students:
    print(student)
#list functions
num=[10,50,20,35,15]
print("maximum:",max(num))
print("minimum:",min(num))
print("sum:",sum(num))
# Create a list of 5 fruits and print the first and last fruit.
fruits=["apple","cherry","orange","strawberry","mango"]
print("first fruit:",fruits[0])
print("last fruit:",fruits[-1])
#Create a list of marks and print the highest mark.
marks=[98,45,65,78,84]
print("Highest mark:",max(marks))
#Use a loop to print all fruits.
for fruit in fruits:
    print(fruit)
#list slicing
print(num[1:4])
#inserting the elements
students.insert(2,"Rahul")
print(students)
#sorting the elements
marks.sort()
print("marks:",marks)
#reversing the elements
marks.reverse()
print("marks:",marks)

