#9. Write a program to define and use user-defined functions with different types of arguments.

def add(a,b):
    return a + b
def greet(name="student"):
    print("Hello",name)

print("Sum :",add(10,20))

greet()
greet("Surbhi Sorathiya")
