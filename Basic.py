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

# Armstrong Number Check
# Check if a number is an Armstrong number (sum of digits raised to the power of number of digits)
n = 153  # Example input (uncomment below for user input)
# n = int(input("Enter Num: "))

original = n
nod = len(str(n))

result = 0

while n > 0:
    ld = n % 10
    result = result + (ld ** nod)
    n = n // 10

print("Armstrong Sum Result:", result)

if result == original:
    print("Is Armstrong Number: Yes")
else:
    print("Is Armstrong Number: No")


# Find Divisors / Factors of a Number (Optimized O(sqrt(N)) Class approach)
# Find all positive factors of a given integer
from math import sqrt

class Factors:
    def factorsOfnumbers(self, n):
        num = n
        result = []
        s = int(sqrt(num))
        
        for i in range(1, s + 1):
            if num % i == 0:
                result.append(i)
                if num // i != i:
                    result.append(num // i)

        result.sort()
        return result

s1 = Factors()
print("Factors of 36:", s1.factorsOfnumbers(36))



# Palindrome Number Check
# Check if an integer is a palindrome by reversing its digits
class Solution(object):
    def isPalindrome(self, x):
        num = x
        result = 0

        while num > 0:
            ld = num % 10
            result = (result * 10) + ld
            num = num // 10

        return result == x

s1 = Solution()
print("Is Palindrome (-242):", s1.isPalindrome(-242))


# Hashing & Frequency Counting Concepts

# 1. Frequency Counting using Dictionary (Hash Map)
# Count occurrences of each number in a list using a Python dictionary
nums = [1, 56, 4, 8, 56, 4, 8, 3, 1, 1, 111, 46, 48, 6]
dic = {}
for num in nums:
    dic[num] = dic.get(num, 0) + 1
print("Frequency Dictionary:", dic)


# 2. Element Frequency Querying using Array Hashing
# Precompute element frequencies in a fixed-size array to quickly answer frequency queries
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

hash_dict = [0] * 11

# Count frequencies
for num in n:
    hash_dict[num] += 1

# Answer queries
print("Frequency Queries Output:")
for x in m:
    if x < 1 or x > 10:
        print(0)
    else:
        print(hash_dict[x])


# 3. Find First Duplicate / Repeating Element using Array Hashing
# Identify the first number in the list that appears more than once
nums_dup = [3, 1, 3, 2, 5, 3, 2, 1, 3, 5, 5, 5]
hash_arr = [0] * 13

for num in nums_dup:
    hash_arr[num] += 1
    if hash_arr[num] > 1:
        print("First Duplicate Element:", num)
        break


