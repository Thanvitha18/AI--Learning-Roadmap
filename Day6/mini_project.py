class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
    def result(self):
        if self.marks>=35:
            print("Result :pass")
        else:
            print("Result :Fail")
s1=Student("Jhon",98)
s1.display()
s1.result()
print()
s2=Student("Meera",25)
s2.display()
s2.result()
print()
students = [
    Student("Kiran", 92),
    Student("Karima",29),
    Student("Sara", 78)
]
for student in students:
    student.display()
    student.result()
    print()