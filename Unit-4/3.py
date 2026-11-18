class student:
    college="Marwadi University"

    def __init__(self,name,age):
        self.name =name
        self.age =age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("College:",student.college)

s1=student("Surbhi",27)
s2=student("Vishwa",21)

s1.display()
print()
s2.display()
