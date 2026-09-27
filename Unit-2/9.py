#Write a program to demonstrate iterators and iterables in python.

n=[10,20,30,40,50,60]

print("Iterables :")
for x in n:
    print(x)

itr=iter(n)

print("\nIterator : ")
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
