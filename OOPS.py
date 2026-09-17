# Basic Object-Oriented Programming (OOP) Example

# Class: A class is a blueprint for creating objects.
# Object: An object is an instance of a class.
# __init__: A constructor method that runs automatically when an object is created.
# Method: A function defined inside a class.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")

# Creating an object of the Student class
student1 = Student("Deva", 21)
student1.display_info()

# Another simple OOP example
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

my_dog = Dog("Buddy", "Labrador")
my_dog.bark()

# Example 1: Student marks average
class Studentmarks:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello")

    def marksavg(self):
        total = sum(self.marks)
        average = total / len(self.marks)
        print(f"{self.name}, your average marks are: {average}")

s1 = Studentmarks("Deva", [86, 54, 98])
s1.hello()
s1.marksavg()

# Example 2: Bank account operations
class Account:
    def __init__(self, balance, accno):
        self.balance = balance
        self.accno = accno

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} has debited from {self.accno}. Your current balance is:")
        print(self.getbalance())

    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} has credited to {self.accno}. Your balance is:")
        print(self.getbalance())

    def getbalance(self):
        return self.balance

acc1 = Account(10000, "AC1")
acc1.debit(2500)
acc1.credit(5000)

# Definition summary:
# - Class: blueprint/template
# - Object: real instance of a class
# - __init__: initialize object attributes
# - Method: function inside a class
