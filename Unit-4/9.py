#write mode

f=open("Student.txt","w")
f.write("Welcome to Python")
f.write("File Handling Practical")
f.close()

#read mode
f=open("Student.txt","r")
print("Reading File:")
print(f.read())
f.close()

#append mode
f=open("Student.txt","a")
f.write("\nThis is Append Mode")
f.close()

#read update file
f=open("Student.txt","r")
print("\nAfter Append:")
print(f.read())
f.close()
