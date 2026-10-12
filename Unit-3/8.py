#Write a program to demonstrate basic regular expression pattern matching

import re

text="Hello Python 1234"

result=re.search("Python",text)
print("Search:",result.group() if result else "Not Found")

result=re.match("Hello",text)
print("Match:",result.group() if result else "Not Match")

result=re.findall(r"[0-9]",text)
print("Digits:",result)

result=re.sub("Python","World",text)
print("Replace:",result)

result=re.search(r"[0-9]+",text)
print("Number:",result.group() if result else "Not Found")
