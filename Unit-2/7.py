#Write a program to demonstrate list dictionary and set comprehensions.

n=[1,2,3,4,5,6]

s=[x*x for x in n]

print("List :",s)

s_dict={x*x for x in s}

print("\nDictionary : ",s_dict)

e_set={x for x in n if x % 2==0}

print("\nSet : ",e_set)
