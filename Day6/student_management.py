class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
    def result(self):
        if self.marks>=35:
            print("Result : Pass")
        else: 
            print("Result : Fail")
students = []

for i in range(5):
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    students.append(Student(name, marks))

print("\nStudent Details")

for student in students:
    student.display()
    student.result()
    print()
