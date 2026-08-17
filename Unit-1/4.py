#4. Write a program to demonstrate string operation including slicing formating and built-in string function.

string=input()

print("\n========== Slicing ==========")
print("String : ",string)
print("First 5 characters : ",string[:5])
print("Last 5 characters : ",string[-5:])
print("Character from 5 to 10 : ",string[5:10])
print("Reverse String : ",string[::-1])

print("\n========== Formating ==========")
name=input("Enter Name : ")
course=input("Enter Course : ")
print(f"My name is {name} and I am Studeing {course}.")

print("\n========== Built-In String ==========")
print("Uppercase : ",string.upper())
print("Lowercase : ",string.lower())
print("Title Case : ",string.title())
print("Lenth : ",len(string))
print("Count s : ",string.count("s"))
