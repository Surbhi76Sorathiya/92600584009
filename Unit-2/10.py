#write a program to generate a sequence of numbers using generator functions and yield keyword.

def num(n):
    for i in range(1,n+1):
        yield i

nu=num(6)

print("Generate Sequence : ")

for y in nu:
    print(y)
