## Basic Object-Oriented Programming (OOP) Example

# Class: A class is a blueprint for creating objects.
# Object: An object is an instance of a class.
# __init__: A constructor method that runs automatically when an object is created.

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

# Definition summary:
# - Class: blueprint/template
# - Object: real instance of a class
# - __init__: initialize object attributes
# - Method: function inside a class