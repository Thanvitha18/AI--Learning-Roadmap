import os

print("Current Folder:", os.getcwd())

with open("notes.txt","w") as file:
    file.write("Hello AI world!")
with open("notes.txt","r") as file:
    content=file.read()
print(content)
with open("notes.txt","a") as file:
    file.write("\nLearning AI Engineering")
with open("notes.txt","r") as file:
    content=file.read()
print(content)
# working with CSV Files
import csv
with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Marks"])
    writer.writerow(["Jhon",95])
    writer.writerow(["Ajay",88])
#exception handling
try:
    a=int(input("enter number:"))
    print(100/a)
except ValueError:
    print("invalid error!")
except ZeroDivisionError:
    print("Division by Zero not allowed!")
finally:
    print("Done!")