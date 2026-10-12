#Write a program to perform file and directory operation using os and sys module.

import os
import sys

print("Current Directory:",os.getcwd())
if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Directory Created.")

file=open("MyFolder/Semple.txt","w")
file.write("Hello,Python")
file.close()
print("File Created.")
print("Directory contents:",os.listdir("MyFolder"))

print("\nPython Version:",sys.version)

print("Command-line Arguments:",sys.argv)

os.remove("MyFolder/Semple.txt")
print("File Deleted.")

os.rmdir("MyFolder")
print("Directory Deleted.")
