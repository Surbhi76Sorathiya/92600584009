class student:
    college="Marwadi University"

    def __init__(self,name):
        self.name= name

    def show(self):
        print("Student Name:",self.name)

    @classmethod
    def college_name(cls):
        print("College:",cls.college)

    @staticmethod
    def message():
        print("Welcome to Python.")

s1=student("Surbhi")

s1.show()
student.college_name()
student.message()
        
