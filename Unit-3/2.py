import math

a=int(input("Enter a number:"))
print("\nUsing import module")
print("Squar:",math.sqrt(a))


from math import factorial
print("\nUsing module import function")
print("Factorial :",math.factorial(a))

from math import pow,ceil
print("\nUsing Multiple module import function")
print("2 raised to 3 :",pow(2,3))
print("Ceiling of 4.3 :",ceil(4.3))
