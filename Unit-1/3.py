#3.write a program to perform to arithmetic relational and logical operations using python.

a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))

print("\n========Arithmentic Operation========")
print("Addition       : ",a+b)
print("Substraction   : ",a-b)
print("Multipilaction : ",a*b)
print("Divition       : ",a/b)
print("Floor Divition : ",a//b)

print("\n=========Relational Operation=========")
print("a == b  : ",a==b)
print("a != b  : ",a!=b)
print("a > b   : ",a>b)
print("a < b   : ",a<b)
print("a >= b  : ",a>=b)
print("a <= b  : ",a<=b)

a=True
b=False

print("\n=========Logical Operation=========")
print("a and b : ",a and b)
print("a or b  : ",a or b)
print("not a : ",not a)
