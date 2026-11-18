#creating and writing a file
f=open("demo.txt","w")
f.write("Python Programming")
f.close()

#opening file in read mode
f=open("demo.txt","r")

#current position
print("Initial Position:",f.tell())

#reading first 6 characters
data=f.read(6)
print("Read Data:",data)

#moving pointer to position 7
f.seek(7)
print("After seek position:",f.tell())

#reading remaining data
print("Remaining Data:",f.read())
f.close()
