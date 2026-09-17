# factorial of a num by storing in the memo ------------->
# memo = {}
# def factorial_memo(n):

#     if n == 0:
#         return 1
#     if n in memo:
#         return memo[n]
#     memo[n] = n * factorial_memo(n-1)
#     return memo[n] 

# print(factorial_memo(int(input("Enter the num: "))))
# print(memo)

# Random numbers --------------------------------->

# import random

# num = random.random()
# print(num)

# num = random.uniform(1,100)
# print(num)

# num = random.randint(1,100)
# print(num)

# num = random.randrange(0,100,2)
# print(num)

# num = random.sample(range(1,100),4)
# print(num)


# Fibonacci series ----------------->

# def fibonacci_series(num):
#     a, b = 0,1
#     if num == 0:
#         print(
#             "null"
#         )
#     elif num == 1:
#         print(a)
#     elif num > 2:
#         print(a)
#         print(b)

#         for _ in range(num-2):
#             c = a + b

#             a,b = b, c

#             print(c)

# print(fibonacci_series(int(input("num: "))))



    