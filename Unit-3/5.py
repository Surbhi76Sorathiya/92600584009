#Write a program t display current date and time using datetime module.

import datetime

now=datetime.datetime.now()

print("Current date and time:",now)
print("Current date:",now.date())
print("Current time:",now.time())
