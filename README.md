# 🚀 AI Learning Roadmap

## Goal

To go from a beginner to building AI applications by learning Python, programming fundamentals, data handling, and AI-related technologies step by step.

---

# 📅 Day 1: AI Fundamentals & Setup

## Topics Covered

* Artificial Intelligence (AI)
* Machine Learning (ML)
* Deep Learning (DL)
* Generative AI
* AI Applications
* Python Installation
* GitHub Setup

## Key Learnings

* AI enables machines to perform tasks that typically require human intelligence.
* ML allows systems to learn from data.
* DL uses neural networks to solve complex problems.
* Generative AI creates new content such as text, images, and code.

### AI Hierarchy

```text
Artificial Intelligence
    └── Machine Learning
            └── Deep Learning
                    └── Generative AI
```

---

# 📅 Day 2: Variables, Data Types & Operators

## Topics Covered

* Variables
* Data Types
* Operators

### Example

```python
name = "Thanvitha"
age = 20
cgpa = 8.5

print(name)
print(age)
print(cgpa)
```

### Data Types

* int
* float
* str
* bool

### Operators

* Arithmetic Operators
* Comparison Operators
* Logical Operators
* Assignment Operators

---

# 📅 Day 3: Conditional Statements & Loops

## Topics Covered

* if
* if-else
* if-elif-else
* for loop
* while loop

### Conditional Example

```python
age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

### Loop Example

```python
for i in range(1, 6):
    print(i)
```

---

# 📅 Day 4: Functions & Modules

## Topics Covered

* Functions
* Function Arguments
* Return Statements
* Modules

### Function Example

```python
def greet(name):
    return f"Hello {name}"

print(greet("Thanvitha"))
```

### Module Example

```python
import math

print(math.sqrt(25))
```

## Learning Outcomes

* Created reusable code using functions.
* Imported and used built-in modules.

---

# 📅 Day 5: Lists, Tuples, Sets & Dictionaries

## Topics Covered

* Lists
* Tuples
* Sets
* Dictionaries

### List Example

```python
students = ["Jhon", "Meera", "Sara"]

students.append("Megha")

print(students)
```

### Tuple Example

```python
numbers = (10, 20, 30)
print(numbers)
```

### Set Example

```python
fruits = {"apple", "banana", "apple"}

print(fruits)
```

### Dictionary Example

```python
student = {
    "name": "Jhon",
    "age": 21,
    "branch": "CSE"
}

print(student)
```

## Learning Outcomes

* Stored and managed collections of data.
* Learned differences between lists, tuples, sets, and dictionaries.

---

# 📅 Day 6: Object-Oriented Programming (OOP)

## Topics Covered

* Classes
* Objects
* Constructors
* Methods

### Example

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

student1 = Student("Thanvitha", 95)

student1.display()
```

## Learning Outcomes

* Created classes and objects.
* Used constructors and methods.
* Understood the basics of OOP.

---

# 📅 Day 7: File Handling, CSV Files & Exception Handling

## Topics Covered

* File Handling
* CSV Files
* Exception Handling

### File Handling

```python
with open("notes.txt", "w") as file:
    file.write("Hello AI world!")

with open("notes.txt", "r") as file:
    print(file.read())
```

### CSV Files

```python
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Marks"])
    writer.writerow(["Jhon", 95])
    writer.writerow(["Ajay", 88])
```

### Exception Handling

```python
try:
    a = int(input("Enter number: "))
    print(100 / a)

except ValueError:
    print("Invalid input!")

except ZeroDivisionError:
    print("Division by Zero not allowed!")

finally:
    print("Done!")
```

## Learning Outcomes

* Created, read, and updated files.
* Worked with CSV data.
* Handled errors using exception handling.

---

# 🎯 Progress Summary

✅ Day 1 - AI Fundamentals & Setup

✅ Day 2 - Variables, Data Types & Operators

✅ Day 3 - Conditional Statements & Loops

✅ Day 4 - Functions & Modules

✅ Day 5 - Lists, Tuples, Sets & Dictionaries

✅ Day 6 - Object-Oriented Programming (OOP)

✅ Day 7 - File Handling, CSV Files & Exception Handling

---

# 🚀 Next Up

## Day 8: NumPy Basics

Topics:

* NumPy Installation
* Arrays
* Array Operations
* Indexing & Slicing
* Mathematical Functions

Current Progress: **7 / 60 Days Completed**
