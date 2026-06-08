# AI Learning Roadmap – Days 1 to 6

## Overview

This repository contains my progress in learning Python and AI fundamentals as part of a 60-Day AI Learning Roadmap.

---

# Day 1: Introduction to AI & Python Setup

## Topics Covered

* Artificial Intelligence (AI)
* Machine Learning (ML)
* Deep Learning (DL)
* Generative AI
* AI Applications
* Python Installation
* VS Code Setup
* GitHub Setup

## Key Learnings

* AI enables machines to perform tasks that typically require human intelligence.
* ML is a subset of AI that learns from data.
* DL is a subset of ML that uses neural networks.
* Generative AI creates new content such as text, images, audio, and code.
* GitHub is used for version control and project hosting.

---

# Day 2: Variables, Data Types & Operators

## Topics Covered

* Variables
* Data Types
* Type Conversion
* Arithmetic Operators
* Comparison Operators
* Logical Operators
* Assignment Operators

## Data Types Learned

* Integer (`int`)
* Float (`float`)
* String (`str`)
* Boolean (`bool`)

## Sample Concepts

```python
name = "Thanvitha"
age = 20
cgpa = 8.5
```

### Operators

```python
+
-
*
/
/
//
%
**
```

---

# Day 3: Conditional Statements & Loops

## Topics Covered

* if Statement
* if-else Statement
* if-elif-else Statement
* Nested Conditions
* for Loop
* while Loop
* break
* continue

## Sample Programs

* Even or Odd
* Positive or Negative Number
* Largest of Two Numbers
* Multiplication Table
* Sum of Numbers

### Example

```python
num = 10

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# Day 4: Functions

## Topics Covered

* Function Definition
* Function Calling
* Parameters
* Arguments
* Return Statement
* Built-in Functions

## Example

```python
def greet(name):
    print("Hello", name)

greet("Thanvitha")
```

## Benefits of Functions

* Code Reusability
* Better Organization
* Easier Maintenance

---

# Day 5: Lists, Tuples, Dictionaries & Sets

## Topics Covered

### Lists

```python
students = ["Jhon", "Meera", "Sara"]
```

Operations:

* Access Elements
* Add Elements
* Remove Elements
* Update Elements

### Tuples

```python
colors = ("Red", "Green", "Blue")
```

Features:

* Ordered
* Immutable

### Dictionaries

```python
student = {
    "name": "Jhon",
    "age": 21,
    "branch": "CSE"
}
```

Operations:

* keys()
* values()
* update()
* add new key-value pairs

### Sets

```python
numbers = {1, 2, 3, 4}
```

Features:

* Unique Values
* Unordered Collection

---

# Day 6: Object-Oriented Programming (OOP)

## Topics Covered

### Classes and Objects

```python
class Student:
    pass

s1 = Student()
```

<<<<<<< HEAD
### Constructor

```python
class Student:
    def __init__(self, name):
        self.name = name
```
=======
✅ Day 5 Completed
### Next Step

➡️ Day 6: Object-Oriented Programming (OOP)

Building the foundation for real-world software development and AI applications.
>>>>>>> 4938ece0b12d9b278acff576eab3d0b6f3f161d1

### Methods

```python
class Student:
    def display(self):
        print(self.name)
```

### Inheritance

```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    pass
```

### Method Overriding

```python
class Dog(Animal):
    def sound(self):
        print("Bark")
```

### Polymorphism

```python
class Bird:
    def move(self):
        print("Flying")

class Fish:
    def move(self):
        print("Swimming")
```

## Mini Projects Completed

### Rectangle Class

* Area Calculation
* Perimeter Calculation

### BankAccount Class

* Deposit
* Withdraw
* Check Balance

### Student Class

* Display Student Details
* Check Pass/Fail Result

### Student Management System

* Create Student Objects
* Store Objects in a List
* Display Student Information
* Generate Results

---

# Skills Gained After 6 Days

* Python Fundamentals
* Problem Solving
* Conditional Logic
* Loops
* Functions
* Collections (List, Tuple, Dictionary, Set)
* Object-Oriented Programming
* Class Design
* Inheritance
* Polymorphism
* Mini Project Development

---

# Next Step

## Day 7

* File Handling
* CSV Files
* Exception Handling

Goal: Learn how to store, read, and manage data using files and handle runtime errors effectively.
