#Write a program t extract specific information from a text file using regular expressions.

import re

with open("data.txt","r") as file:
    text=file.read()

name=re.search(r"Name:\s*(.+)",text)
print("Name:",name.group(1) if name else "Not Found")
email=re.search(r"[\w.-]+@[\w.-]+\.\w+",text)
print("Email:",email.group() if email else "Not Found")
phone=re.search(r"\b[0-9]{10}\b",text)
print("Phone:",phone.group() if phone else "Not Found")
age=re.search(r"Age:\s*([0-9]+)",text)
print("Age:",age.group(1) if age else "Not Found")
