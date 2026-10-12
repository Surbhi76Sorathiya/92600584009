#Wite a program to use re module function such as match search and fidall.

import re
text="Python is easy.Python is Powerful.Age is 20."

result=re.match("Python",text)
print("Match:",result.group() if result else "Not Found")

result=re.search("easy",text)
print("Search:",result.group() if result else "Not Found")

result=re.findall("Python",text)
print("Find All:",result)
