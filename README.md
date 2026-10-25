# Python Practice Repository

This repository contains Python programs and exercises designed for learning and practicing core Python concepts, Data Structures and Algorithms (DSA), and Object-Oriented Programming (OOP).

---

## What We Have Covered

### Core Python Fundamentals
- Variables & Data Types
- Operators (Arithmetic, Comparison, Logical)
- Conditional Statements (`if`, `elif`, `else`)
- Loops (`for`, `while`)
- Functions & Memoization
- Collections: Lists, Tuples, Dictionaries, Sets
- Classes & Basic OOP (Methods, Constructors, Class & Static Methods)

### Mathematical & Number Theory Algorithms
- Armstrong Number Check
- Finding Divisors / Factors of a Number (Optimized $O(\sqrt{N})$)
- Palindrome Number Check
- Fibonacci Sequence Generator

### Hashing & Hash Map Concepts (Optimal Solutions)
- **Direct Address Array Hashing**: Precomputed integer frequencies with $O(1)$ query time
- **Character Hashing**: Fixed 26-element array mapping using `ord(char) - ord('a')` ($O(1)$ auxiliary space)
- **Hash Map (Dictionary) Frequency Counting**: General frequency counter for arbitrary items
- **Highest and Lowest Frequency Elements**: Optimal single-pass $O(N)$ identification
- **First Repeating & First Non-Repeating Elements**: Tracking duplicates and unique items in $O(N)$
- **Two Sum Problem**: Optimal single-pass hash map solution ($O(N)$ time, $O(N)$ space)
- **Longest Subarray with Sum K**: Optimal prefix sum + hash map approach ($O(N)$ time, $O(N)$ space)
- **Subarray Sum Equals K**: Count total subarrays summing to $k$ ($O(N)$ time)
- **Valid Anagram Check**: Frequency array comparison in $O(N)$ time and $O(1)$ extra space
- **Custom HashTable Implementation**: Underlying mechanics with modulo hash function, separate chaining collision resolution, and dynamic resizing

### All 5 Classic Sorting Algorithms (Optimal Implementations)
Detailed implementations with time and space complexity analysis:

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity | Stability | In-Place |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Selection Sort** | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | No | Yes |
| **Bubble Sort** (Optimized) | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | Yes | Yes |
| **Insertion Sort** (Optimized) | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | Yes | Yes |
| **Merge Sort** (Divide & Conquer) | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ | Yes | No |
| **Quick Sort** (Median-of-Three) | $O(N \log N)$ | $O(N \log N)$ | $O(N^2)^*$ | $O(\log N)$ stack | No | Yes |

*\* Quick Sort worst-case is mitigated to expected $O(N \log N)$ using median-of-three pivot selection.*

---

## Files in This Repository

- **[Basic.py](file:///Basic.py)**: Covers Python fundamentals, mathematical algorithms, optimal hashing patterns, and concise implementations of all 5 sorting algorithms.
- **[Sorting.py](file:///Sorting.py)**: Dedicated module implementing all 5 sorting algorithms (Selection, Bubble, Insertion, Merge, Quick) with optimal strategies, in-place variants, and comprehensive test drivers.
- **[Hashing.py](file:///Hashing.py)**: Dedicated module containing optimal hashing techniques, classic interview problems (Two Sum, Longest Subarray Sum, Anagrams), and a custom `HashTable` class with separate chaining and dynamic resizing.
- **[OOPS.py](file:///OOPS.py)**: Demonstrates Object-Oriented Programming (classes, objects, constructors, static methods, instance methods, and real-world examples).
- **[README.md](file:///README.md)**: Repository overview, algorithm complexity reference, and learning roadmap.

---

## Coming Soon

- Inheritance (Single, Multiple, Multilevel)
- Encapsulation & Access Modifiers
- Polymorphism & Method Overriding
- Abstraction & Abstract Base Classes
- Exception Handling (`try`, `except`, `finally`, custom exceptions)
- File Handling (reading, writing, context managers)
- Modules and Packages
- Mini Projects & LeetCode/DSA problem series

---

## Topics Status

- **Completed**: Variables, Data Types, Operators, Loops, Functions, Lists, Tuples, Dictionaries, Sets, Armstrong Number, Optimized Factor Finder, Palindrome Check, Frequency Counting & Hashing (Array, Character, Dictionary, Two Sum, Longest Subarray Sum, Custom HashTable), All 5 Sorting Algorithms (Selection, Bubble, Insertion, Merge, Quick Sort), and Basic OOP.
- **In Progress**: Advanced OOP paradigms, recursion patterns, and linked data structures.
- **Upcoming**: Inheritance, Encapsulation, Polymorphism, File Handling, and Mini Projects.

---

## Purpose

This repository is dedicated to learning, practicing, and mastering Python programming, Data Structures, and Algorithms through clear, optimal, and beginner-to-advanced examples.

---

## License

This project is created for educational and learning purposes.
