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



# Day 8 - NumPy Basics

## Topics Covered
- NumPy Introduction
- Creating Arrays
- Array Indexing
- Array Reshaping
- Statistical Functions
- zeros(), ones(), arange()
- Array Arithmetic Operations
- Array Slicing

## Concepts Practiced
- Accessing elements using indexing
- Finding max, min, and mean values
- Reshaping arrays
- Creating special arrays
- Performing addition, subtraction, and power operations on arrays
- Using slicing to extract portions of arrays

## Files
- numpy_basics.py

## Key Learning
NumPy provides fast and efficient numerical operations using arrays. It is the foundation for data science, machine learning, and AI development in Python. Day 7 - File Handling, CSV Files & Exception Handling
 

---

# 🎯 Progress Summary

✅ Day 1 - AI Fundamentals & Setup

✅ Day 2 - Variables, Data Types & Operators

✅ Day 3 - Conditional Statements & Loops

✅ Day 4 - Functions & Modules

✅ Day 5 - Lists, Tuples, Sets & Dictionaries

✅ Day 6 - Object-Oriented Programming (OOP)

✅ Day 7 - File handling, Exception handling , CSV files

✅ Day 8 - Numpy Basics

✅ Day 9 - Pandas Basics

# Day 9 - Pandas CSV Handling

## Topics Covered
- Reading CSV files
- pd.read_csv()
- Data inspection
- head()
- tail()
- info()
- describe()
- Column selection
- Row selection
- Data filtering
- Saving DataFrames to CSV

## Key Learning
CSV files are widely used for storing datasets. Pandas can load CSV files into DataFrames, making it easy to analyze, filter, and manipulate data for AI and Machine Learning projects.

# Day 10 - Data Cleaning & Preprocessing

## Topics Covered
- Missing Values
- Handling Null Data
- fillna()
- dropna()
- Duplicate Records
- duplicated()
- drop_duplicates()
- Renaming Columns
- Data Type Conversion
- String Cleaning

## Programs Practiced
- Missing Value Detection
- Filling Missing Values
- Removing Missing Values
- Duplicate Removal
- Column Renaming
- Data Type Conversion
- Text Formatting

## Key Learning
Real-world datasets are often messy. Data cleaning helps prepare data before analysis and machine learning.

# Day 11 - Matlotlib basics
Day11/
├── bar_chart.py
├── histogram.py ✅
├── line_plot.py
├── multiple_lines.py
├── pie_chart.py
├── save_graph.py
├── sales_graph.png
├── scatter_plot.py
└── mini_challenge.py

# Day 12 -seaborn and Data visualization

AI-Learning-Roadmap/
|
|-- Day12/
    |-- line_plot.py
    |-- bar_plot.py
    |-- histogram.py
    |-- scatter_plot.py
    |-- count_plot.py
    |-- box_plot.py
    |-- heatmap.py
# Day 13 - Exploratory Data Analysis (EDA)

## 📌 Overview

Today, I learned Exploratory Data Analysis (EDA), which is the process of understanding, cleaning, and analyzing a dataset before applying Machine Learning models.

In this day, I used Python libraries like Pandas, Seaborn, and Matplotlib to inspect data, find patterns, detect issues, and generate insights from the dataset.

---

## 🛠️ Libraries Used

- Pandas
- Seaborn
- Matplotlib

---

## 📂 Dataset Used

Seaborn built-in **tips** dataset.

The dataset contains information about:
- Total restaurant bill amount
- Tips given by customers
- Customer gender
- Smoking status
- Day of visit
- Meal time
- Number of people at the table

---

## 📚 Topics Covered

### 1. Dataset Overview
- Loading dataset using `sns.load_dataset()`
- Viewing first rows using `head()`
- Checking dataset shape
- Viewing column names
- Understanding data types using `info()`

### 2. Data Cleaning
- Checking missing values using `isnull().sum()`
- Finding duplicate rows using `duplicated().sum()`

### 3. Statistical Analysis
- Generating summary statistics using `describe()`
- Finding average values using `mean()`

### 4. Data Visualization

Created the following visualizations:

- Histogram → Distribution of total bills
- Box Plot → Detecting outliers in bill amounts
- Count Plot → Number of customers on different days
- Scatter Plot → Relationship between total bill and tip
- Heatmap → Correlation between numerical columns

---

## 📊 Insights Extracted

- Calculated the average restaurant bill.
- Counted smokers and non-smokers.
- Found the average tip given on each day.
- Identified relationships between numerical features.

---

## 🧠 Key Learnings

- EDA helps understand the quality and structure of data.
- Real-world datasets may contain missing values, duplicates, and outliers.
- Visualizations help discover hidden patterns.
- Data analysis is an important step before building Machine Learning models.

---

## 📁 Files Included

# Day 14: Kaggle Dataset Analysis - Titanic Dataset 🚢📊

## 📌 Overview

On Day 14 of my AI Learning Roadmap, I worked on my first real Kaggle dataset - the Titanic dataset.

The goal was to perform Exploratory Data Analysis (EDA), clean the dataset, create visualizations, and extract meaningful insights from the data.

---

## 📂 Files

```
Day14/
│
├── dataset_loading.py   # Loading and understanding the dataset
├── data_cleaning.py     # Handling missing values and cleaning data
├── visualization.py     # Data visualization and insights
├── tested.csv           # Titanic dataset
└── README.md
```

---

## 🛠️ Libraries Used

- Pandas
- Seaborn
- Matplotlib

---

## 📊 Dataset Understanding

Performed the following operations:

- Loaded CSV dataset using `pd.read_csv()`
- Viewed first 5 rows using `head()`
- Checked dataset shape and columns
- Examined data types using `info()`
- Identified numerical and categorical columns
- Checked missing values using `isnull().sum()`
- Generated statistical summary using `describe()`

---

## 🧹 Data Cleaning

Handled missing values:

- Filled missing `Age` values using the mean age
- Filled missing `Fare` values using the mean fare
- Removed the `Cabin` column due to a high percentage of missing values

---

## 📈 Data Visualization

Created various plots to understand the dataset:

### 1. Survival Distribution
- Count plot to compare survivors and non-survivors

### 2. Age Distribution
- Histogram to analyze passenger age distribution

### 3. Fare Distribution
- Box plot to identify fare spread and outliers

### 4. Passenger Class Analysis
- Count plot to analyze the number of passengers in each class

### 5. Survival by Passenger Class
- Used `hue` in count plots to compare survival across different passenger classes

### 6. Survival by Gender
- Analyzed survival differences between male and female passengers

---

## 🔍 Key Insights

### Passenger Class
- Third-class passengers were the majority.
- Third class had the highest number of deaths.
- First class had the highest survival rate.

### Gender
- In the `tested.csv` dataset:
  - Female passengers had a 100% survival rate.
  - Male passengers had a 0% survival rate.

### Age
- Average age was almost the same for survivors and non-survivors in this dataset.

### Fare
- Survivors paid a higher average fare compared to non-survivors.

---

## 🧠 Concepts Learned

- Loading real-world CSV datasets
- Data cleaning techniques
- Handling missing values
- Removing unnecessary columns
- Univariate analysis
- Bivariate analysis
- Using `groupby()` for insights
- Understanding counts vs percentages
- Using `hue` in Seaborn visualizations
- Writing data-driven conclusions

---

## 🚀 Outcome

Day 14 helped me move from practicing with small datasets to working with a real Kaggle dataset. I learned how a Data Analyst explores raw data, cleans it, visualizes patterns, and converts observations into meaningful insights.

# Day 15: Mini Project - Netflix Dataset Analysis & Dashboard 🎬📊

## 📌 Overview

On Day 15 of my AI Learning Roadmap, I completed a mini data analysis project using the Netflix Movies and TV Shows dataset.

The goal of this project was to perform data cleaning, exploratory data analysis (EDA), create visualizations, and build a simple dashboard to discover meaningful insights about Netflix content.

---

## 📂 Project Structure

```
Day15/
│
├── netflix.csv           # Dataset
├── dataset_loading.py    # Loading and understanding the dataset
├── data_cleaning.py      # Handling missing values and cleaning data
├── visualization.py      # Individual visualizations and analysis
├── dashboard.py          # Combined dashboard with multiple graphs
└── README.md             # Project documentation
```

---

## 🛠️ Libraries Used

- Pandas
- Seaborn
- Matplotlib

---

## 📊 Dataset Information

- Total records: **8,807**
- Total columns: **12**

### Main Features

| Column | Description |
|---|---|
| show_id | Unique ID of Netflix content |
| type | Movie or TV Show |
| title | Name of the content |
| director | Director name |
| cast | Actors involved |
| country | Country where content was produced |
| date_added | Date when content was added to Netflix |
| release_year | Original release year |
| rating | Age suitability rating |
| duration | Movie duration or number of seasons |
| listed_in | Genre/category |
| description | Brief summary |

---

## 🧹 Data Cleaning

Performed the following cleaning steps:

- Filled missing `director` values with `"Unknown"`
- Filled missing `cast` values with `"Unknown"`
- Filled missing `country` values with `"Unknown"`
- Removed rows with missing `date_added`
- Filled missing `rating` values using the most common rating (mode)
- Removed rows with missing `duration`

### Dataset After Cleaning

- Final records: **8,794**
- Missing values: **0**

---

## 📈 Exploratory Data Analysis (EDA)

### 1. Movies vs TV Shows

- Movies: **6,128**
- TV Shows: **2,666**

**Insight:**
Netflix contains significantly more Movies than TV Shows.

---

### 2. Content by Country

Top countries:

- United States: 2,809
- India: 972
- United Kingdom: 418
- Japan: 244
- South Korea: 199

**Insight:**
The United States contributes the largest amount of Netflix content, with India being the second-largest contributor.

---

### 3. Content Ratings

Most common rating:

- TV-MA

**Insight:**
Most Netflix content is targeted toward mature audiences.

---

### 4. Release Year Analysis

**Insight:**

- Content releases increased significantly after the year 2000.
- The highest number of releases occurred around 2018.

---

### 5. Genre Analysis

Most common categories:

- Dramas
- International Movies

**Insight:**
Netflix provides a wide range of story-driven and internationally produced content.

---

## 📊 Dashboard

Created a dashboard containing:

- Movies vs TV Shows distribution
- Top countries producing content
- Most common content ratings
- Release year trends

---

## 🧠 Concepts Learned

Through this project, I learned:

- Working with real-world datasets
- Handling missing values
- Data cleaning techniques
- Exploratory Data Analysis (EDA)
- Creating visualizations using Seaborn and Matplotlib
- Using `groupby()`, `value_counts()`, and sorting methods
- Extracting meaningful insights from data
- Building a simple data dashboard

---

## 🚀 Outcome

This project helped me understand the complete workflow of a Data Analyst:

```
Raw Dataset
      ↓
Data Understanding
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Visualization
      ↓
Dashboard & Insights
```

Day 15 marks my first complete end-to-end data analysis mini project using a real-world Netflix dataset.
# Day 16: Linear Algebra - Matrices

## 📌 Overview
Today I learned the basics of matrices in Linear Algebra and their importance in Artificial Intelligence. I practiced creating matrices and performing different matrix operations using NumPy.

---

## 📚 Topics Covered

### What is a Matrix?
A matrix is a collection of numbers arranged in rows and columns.

Example:
```
1 2 3
4 5 6
7 8 9
```

Shape: 3 × 3 (3 rows and 3 columns)

---

### Types of Matrices
- Row Matrix
- Column Matrix
- Square Matrix
- Zero Matrix
- Identity Matrix

---

### Matrix Operations
- Matrix Addition
- Scalar Multiplication
- Transpose of a Matrix

---

## 💻 NumPy Concepts Practiced
- Creating matrices using `np.array()`
- Finding matrix shape using `.shape`
- Adding two matrices
- Multiplying a matrix by a scalar
- Creating an identity matrix using `np.identity()`
- Creating a zero matrix using `np.zeros()`
- Generating a random matrix using `np.random.rand()`
- Finding rows and columns
- Finding transpose using `.T`

---

## 🤖 Importance of Matrices in AI
- Datasets are stored as matrices.
- Images are represented as matrices of pixel values.
- Neural networks use matrix calculations.
- Matrix operations are used in machine learning algorithms.

---

## ✅ Practice Completed
- Created a 3 × 3 matrix
- Checked matrix shape
- Performed matrix addition
- Performed scalar multiplication
- Created identity and zero matrices
- Generated a random matrix
- Found rows and columns
- Calculated transpose

---

## 🎯 Key Learnings
- A matrix has rows and columns.
- Matrix dimensions are important for operations.
- NumPy makes matrix calculations easy.
- Matrices are a foundation of AI and Machine Learning.

---

## 🚀 Day 16 Completed
Learned the basics of matrices and implemented matrix operations using NumPy.

# Day 17: Vectors and Dot Product using NumPy
📌 Overview

Today, I learned the basics of vectors and performed vector operations using NumPy. Vectors are important in Machine Learning and AI.

## 💻 Programs
Created vectors using NumPy
Performed addition and subtraction
Performed scalar multiplication
Calculated dot product using np.dot()
## 📝 Key Learnings
A vector is a collection of numbers.
Vector operations are used in mat
hematical calculations.
Dot product gives a single value by multiplying corresponding elements and adding them.
Vectors are widely used in AI and Machine Learning.
## 🚀 Day 17 Completed

Successfully completed Day 17 of my AI Learning Roadmap by learning vectors and dot product using NumPy.

# Day 18: Statistics Basics using Python
## 📌 Overview

Today, I learned basic statistics concepts that are important in AI and Machine Learning.

## 📚 Topics Covered
Mean
Median
Mode
Variance
Standard Deviation
## 💻 Programs
Calculated mean using NumPy
Calculated median using NumPy
Calculated mode using statistics/SciPy
Calculated variance and standard deviation using NumPy
## 📝 Key Learnings
Mean gives the average value of data.
Median gives the middle value of sorted data.
Mode gives the most frequently occurring value.
Variance shows how spread out the data is.
Standard deviation tells the amount of variation from the mean.
## 🚀 Day 18 Completed

Successfully completed Day 18 of my AI Learning Roadmap by learning basic statistics concepts used in AI and Machine Learning.





Current Progress: **18 / 60 Days Completed**
