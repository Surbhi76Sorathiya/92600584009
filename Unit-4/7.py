#demostrating MRO
class a:
    def show(self):
        print("Class A")

class b(a):
    def show(self):
        print("Class B")

class c(a):
    def show(self):
        print("Class C")

class d(b,c):
    pass

obj=d()

print("Method Resoluation Order:")
print(d.mro())

print()
print("Calling show method:")
obj.show()

#demostrating Magic Method
class student:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return "Student Name:"+self.name

s1=student("Surbhi")

print()
print("Magic Method Output:")
print(s1)
