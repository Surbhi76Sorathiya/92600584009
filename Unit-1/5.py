#5.Write a program to create and manipulate lists using indexing slicing and list comprehensions.

a=[10,20,30,40,50,60,80,90,100]

print("=============Indexing=============")
print("list [0]: ",a[0])
print("list [-1] : ",a[-1])
print("\n=============Slicing==============")
print("list[1:3] :",a[1:3])

print("\n=============Operation============")
print("Lenth of the List : ",len(a))
print("Membership in List :",30 in a)

print("\n=============Element============")
print("Add element : ",a.append(110))

print("\n=============Comprehension============")
even=[x for x in a if x%2==0]
print("even numbers : ",even)


