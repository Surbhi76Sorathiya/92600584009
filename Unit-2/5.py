a=int(input("Enter a number : "))

print("\n======Using Breake statement======")
for a in range(6):
    if a==5:
        break
    print(a)
print("outside of loop")

print("\n======Using Pass Statement======")
for a in range(5):
    pass
print("No output we be display because of pass statement was given.")
