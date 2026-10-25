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


# 4. Character Hashing (Fixed-size Array Hashing)
# Count character occurrences in O(N) time and O(1) auxiliary space
word = "antigravitypython"
char_hash = [0] * 26
for ch in word:
    char_hash[ord(ch) - ord('a')] += 1
print("Character Frequency for 't':", char_hash[ord('t') - ord('a')])


# 5. Highest and Lowest Frequency Elements in O(N) Time
# Find elements with max and min occurrences using a hash map
items = [1, 56, 4, 8, 56, 4, 8, 3, 1, 1, 111, 46, 48, 6]
freq_map = {}
for x in items:
    freq_map[x] = freq_map.get(x, 0) + 1

max_elem, max_freq = items[0], 0
min_elem, min_freq = items[0], float("inf")
for k, v in freq_map.items():
    if v > max_freq:
        max_freq, max_elem = v, k
    if v < min_freq:
        min_freq, min_elem = v, k
print(f"Highest Frequency Element: {max_elem} (count: {max_freq})")
print(f"Lowest Frequency Element: {min_elem} (count: {min_freq})")


# 6. Two Sum Problem (Optimal Hash Map Solution - O(N) Time, O(N) Space)
# Find two indices whose values sum up to the target
def two_sum(nums, target):
    seen = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], idx]
        seen[num] = idx
    return []

print("Two Sum Indices [2, 7, 11, 15] target=9:", two_sum([2, 7, 11, 15], 9))


# 7. Longest Subarray with Sum K (Optimal Prefix Sum + Hash Map - O(N) Time)
def longest_subarray_sum_k(arr, k):
    prefix_map = {}
    curr_sum = 0
    max_len = 0
    for i, num in enumerate(arr):
        curr_sum += num
        if curr_sum == k:
            max_len = i + 1
        rem = curr_sum - k
        if rem in prefix_map:
            max_len = max(max_len, i - prefix_map[rem])
        if curr_sum not in prefix_map:
            prefix_map[curr_sum] = i
    return max_len

print("Longest Subarray with Sum 15 in [10, 5, 2, 7, 1, 9]:", longest_subarray_sum_k([10, 5, 2, 7, 1, 9], 15))


# =====================================================================
# All 5 Classic Sorting Algorithms (Optimal Implementations)
# =====================================================================

# 1. Selection Sort Algorithm
# Selection Sort repeatedly selects the smallest element from the unsorted portion and swaps it into the sorted portion.
# Time Complexity: O(N^2) for all cases (best, average, worst)
# Space Complexity: O(1) auxiliary space (In-place)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

sample_list_selection = [64, 25, 12, 22, 11]
print("Original List for Selection Sort:", sample_list_selection)
sorted_list_selection = selection_sort(sample_list_selection.copy())
print("Sorted List (Selection Sort):", sorted_list_selection)


# 2. Bubble Sort Algorithm (Optimized)
# Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if in wrong order.
# Optimal: With swapped flag, terminates in O(N) if already sorted.
# Time Complexity: O(N) best case, O(N^2) worst/average case
# Space Complexity: O(1) auxiliary space (In-place, Stable)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

sample_list = [64, 34, 25, 12, 22, 11, 90]
print("Original List for Bubble Sort:", sample_list)
sorted_list = bubble_sort(sample_list.copy())
print("Sorted List (Bubble Sort):", sorted_list)


# 3. Insertion Sort Algorithm (Optimized)
# Builds sorted array one item at a time by shifting larger elements to the right.
# Time Complexity: O(N) best case (already sorted), O(N^2) worst/average case
# Space Complexity: O(1) auxiliary space (In-place, Stable)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

sample_list_insertion = [12, 11, 13, 5, 6]
print("Original List for Insertion Sort:", sample_list_insertion)
sorted_list_insertion = insertion_sort(sample_list_insertion.copy())
print("Sorted List (Insertion Sort):", sorted_list_insertion)


# 4. Merge Sort Algorithm (Divide and Conquer)
# Divides the array into two halves, recursively sorts them, and merges the sorted halves.
# Time Complexity: O(N log N) in all cases (best, average, worst)
# Space Complexity: O(N) auxiliary space (Stable)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge sorted halves
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

sample_list_merge = [38, 27, 43, 3, 9, 82, 10]
print("Original List for Merge Sort:", sample_list_merge)
sorted_list_merge = merge_sort(sample_list_merge.copy())
print("Sorted List (Merge Sort):", sorted_list_merge)


# 5. Quick Sort Algorithm (Divide and Conquer with Partitioning)
# Picks a pivot element and partitions array so elements <= pivot are left, and > pivot are right.
# Time Complexity: O(N log N) average/best case, O(N^2) worst case (mitigated with median pivot)
# Space Complexity: O(log N) recursion stack space (In-place)

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        # Median-of-three pivot selection for optimal partitioning
        mid = (low + high) // 2
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
        arr[mid], arr[high] = arr[high], arr[mid]

        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_idx = i + 1

        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    return arr

sample_list_quick = [10, 7, 8, 9, 1, 5]
print("Original List for Quick Sort:", sample_list_quick)
sorted_list_quick = quick_sort(sample_list_quick.copy())
print("Sorted List (Quick Sort):", sorted_list_quick)





