data={"andhra":"amaravathi","karnataka":"banglore"}
print(data)
print(data["andhra"])
data["karnataka"]="benguluru"
print(data)
data["telangana"]="hyderabad"
print(data)
del data["andhra"]
print(data)
for key in data:
    print(key)
for values in data.values():
    print(values)
for key,values in data.items():
    print(key,values)
# creating student details
students={"name":"jhon","age":21,"department":"CSE"}
print(students["name"])
students["college"]="xyz college"
print(students)
for key,value in students.items():
    print(key,":",value)
#calculating total and avgerage marks
marks={"maths":90,"physics":85,"python":95}
total=sum(marks.values())
print("Total:",total)
avg=total/3.0
print("average:",avg)
students = {"Ram": 85, "Sita": 92,"Ravi": 78, "Priya": 95,"Ajay": 88}
highest=max(students,key=students.get)
lowest=min(students,key=students.get)
print("high scores:",highest,students[highest])
print("low scorer:",lowest,students[lowest])
total=sum(students.values())
print("Total:",total)
avg=total/len(students)
print("Average:",avg)
contacts = {"Mom": "9876543210","Dad": "9876543211","Friend": "9876543212"}
print(contacts["Mom"])
name=input("enter contact name:")
if name in contacts:
    print(contacts[name])
else:
    print("contact not found")
student={"name":"jhon","age":21,"branch":"CSE"}
print("keys:",student.keys())
print("values:",student.values())
student["age"]=22
print(student)
student["college"]="XYZ college"
print(student)
if "branch"  in student:
    print("branch exists")