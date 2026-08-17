#7. Write a program to create a dictionary and demonstrate dictionary methods and iteration.

student = {"name": "Surbhi","age": 27,"course" : "MCA"}

print("===============Print============")
print("Keys : ",student.keys())
print("Values : " ,student.values())

print("\n===============Update=============")
student["city"] = "rajkot"
print("Keys : ",student.keys())
print("Values : ",student.values())

print("\n===============Function===============")
print("Lenth of Dictionary : ",len(student))
