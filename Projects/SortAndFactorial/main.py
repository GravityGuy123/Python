# Assignment
# 1a. Generate a list of integers From negative -100 to positive 100
# 1b. Print the initial list
# 1c. Write a function that will sort a list of integers in ascending orders without using the in built sort
# The function will take a list of integers and return a list of intergers.
# Print the final list


# import random as r

# # 1a.
# integers_list = []

# for a in range(20):
#     r.randint(-100, 100)
#     integers_list.append(r.randint(-100, 100))

# # 1b.
# print(f"Initial List: {integers_list}")

# # 1c.
# def sort_ascending(param: list[int]) -> list[int]:
#     sort = len(param)
#     for i in range(sort):
#         for j in range(0, sort - i - 1):
#             if param[j] > param[j + 1]:
#                 param[j], param[j + 1] = param[j + 1], param[j]
#     return param

# print(f"Final List: {sort_ascending(integers_list)}")


# def sort_ascending(param: list[int]) -> list[int]:
#     param.sort()
#     return param

# print(f"Final List: {sort_ascending(integers_list)}")



# 2. Write a function that will take an integer and return a factorial of that integer.

# Recursive Formula:
# n! = n × (n-1)!
# with base case: 0! = 1 and 1! = 1

# Iterative Formula:
# n! = n × (n-1) × (n-2) × ... × 3 × 2 × 1

# Examples:
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# 4! = 4 × 3 × 2 × 1 = 24
# 3! = 3 × 2 × 1 = 6
# 2! = 2 × 1 = 2
# 1! = 1
# 0! = 1 (by definition)

# def factorial(param: int) -> int:
#     value = param
#     value -= 1
#     print(value * value)

# num = input("Enter an integer: ")
# int(num)
# factorial(num)


def factorial(param: int) -> int:
    value = param
    result = 1
    while value > 1:
        result *= value
        value -= 1
    return result

num = input("Enter an integer: ")
num = int(num)
print(factorial(num))




# Wait first, after thursday class.
# 3a. Write a story generator
# 3b. Write a string that will be about a house, car or whatever you want.
# Create an account on vertex ai



# Assignment
# 1a. Generate a list of integers From negative -100 to positive 100
# 1b. Print the initial list
# 1c. Write a function that will sort a list of integers in ascending orders without using the in built sort
# 1d. The function will take a list of integers and return a list of intergers.
# Print the final list

# 2. Write a function that will take an integer and return a factorial of that integer.