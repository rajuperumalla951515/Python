# Python Basics and Definitions

# 1. Variables
# A variable is a named storage location used to store data.
name = "Python"
age = 21
print("Variable Example:", name, age)

# 2. Data Types
# Data types define the kind of value a variable can hold.
number = 10          # int
price = 25.5         # float
message = "Hello"    # str
is_active = True      # bool
print("Data Types:", type(number), type(price), type(message), type(is_active))

# 3. Operators
# Operators are used to perform operations on variables and values.
addition = 5 + 3
multiplication = 4 * 2
comparison = (10 > 5)
print("Operators:", addition, multiplication, comparison)

# 4. Conditional Statements
# if, elif, and else are used to make decisions in a program.
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
else:
    print("Grade: C")

# 5. Loops
# Loops are used to repeat a block of code.
print("For loop:")
for i in range(1, 5):
    print(i)

count = 1
print("While loop:")
while count <= 3:
    print(count)
    count += 1

# 6. Functions
# A function is a reusable block of code that performs a specific task.
def greet(user):
    return "Hello, " + user

print(greet("Deva"))

# 7. List
# A list is an ordered and mutable collection of items.
fruits = ["apple", "banana", "mango"]
fruits.append("grape")
print("List:", fruits)

# 8. Tuple
# A tuple is an ordered and immutable collection of items.
coordinates = (10, 20)
print("Tuple:", coordinates)

# 9. Dictionary
# A dictionary stores data in key-value pairs.
student = {"name": "Ravi", "age": 20, "course": "Python"}
print("Dictionary:", student)
print("Student name:", student["name"])

# 10. Set
# A set is an unordered collection of unique values.
numbers = {1, 2, 2, 3, 4}
print("Set:", numbers)

# 11. Class and Object
# A class is a blueprint and an object is an instance of a class.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        return f"Car: {self.brand} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.show_details())

# Summary:
# Variables store data, data types define value categories, operators perform actions,
# conditions check logic, loops repeat tasks, functions reuse code, and collections such as
# lists, tuples, dictionaries, and sets organize data efficiently.

# Factorial example using memoization
memo = {}

def factorial_memo(n):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = n * factorial_memo(n - 1)
    return memo[n]

print("Factorial:", factorial_memo(5))

# Random numbers
import random
print("Random float:", random.random())
print("Random integer:", random.randint(1, 100))

# Fibonacci sequence

def fibonacci_series(num):
    a, b = 0, 1
    if num == 0:
        return []
    elif num == 1:
        return [a]
    sequence = [a, b]
    for _ in range(2, num):
        a, b = b, a + b
        sequence.append(b)
    return sequence

print("Fibonacci:", fibonacci_series(8))
