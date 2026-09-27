#Write a program to iterate over lists strings and dictionaries using loops.

f=["Apple","Orange","Pear","Mango"]

print("List :")

for fruit in f:
    print(fruit)

name= "Surbhi"
print("\nString :")

for ch in name:
    print(ch)

student={"name":"Surbhi","age":"27","course":"MCA"}

print("\nDictionary :")

for key,value in student.items():
    print(key, ":" ,value)
