#Write a program to illustrate variable scope using local global and nonlocal variables.

x=input("Enter a value :")

def outer():
    y=input("Enter a value :")

    def inner():
        z=input("Enter a value :")

        print("Global Variable :",x)
        print("Outer Variable :",y)
        print("Inner Variable :",z)

    inner()
outer()

print("Outside Function, Global Variable :",x)
