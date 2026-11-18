class animal:
    def sound(self):
        print("Animal make different sounds")

class dog(animal):
    def sound(self):
        print("Dog barks")

class cat(animal):
    def sound(self):
        print("Cat meows")

a=dog()
b=cat()

a.sound()
b.sound()
