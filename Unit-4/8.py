from abc import ABC, abstractmethod

#abstraction
class bank(ABC):
    @abstractmethod
    def interest(self):
        pass

#Encapsulation and Abstraction
class sbi(bank):
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance += amount

    def display(self):
        print("Account Balance:",self.__balance)

    def interest(self):
        print("Interest Rate:5%")

obj =sbi(10000)

obj.deposit(2000)
obj.display()
obj.interest()
                     
