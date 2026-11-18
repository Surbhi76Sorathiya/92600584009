#Single Inheritance
class perent:
    def show(self):
        print("This is Parent class")

class child(perent):
    def display(self):
        print("This is Child class")

print("Single Inheritance")
obj=child()
obj.show()
obj.display()

#Multilevel Inheritance
class a:
    def show_a(self):
        print("Class A")

class b(a):
    def show_b(self):
        print("Class B")

class c(b):
    def show_c(self):
        print("Class C")

print()
print("Multilevel Inheritance:")
obj=c()
obj.show_a()
obj.show_b()
obj.show_c()

#Multiple Inheritance
class father:
    def father(self):
        print("Father class")

class mother:
    def mother(self):
        print("Mother class")

class son(father,mother):
    def son(self):
        print("Son class")

print("Multiple Inheritance:")
obj=son()
obj.father()
obj.mother()
obj.son()
