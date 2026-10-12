#Write a program to copy move and delete files using shutil module.

import shutil
import os

with open("sample.txt","w") as f:
    f.write("Hello,Python")

print("File created")

shutil.copy("sample.txt","copy.txt")
print("File Copied")

shutil.move("copy.txt","move.txt")
print("File Moved")

os.remove("move.txt")
print("File Deleted")
