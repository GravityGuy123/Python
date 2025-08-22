# Assignment
# 1a. Write a loop that runs from 1 to 100.
# 1b. if it is divisible by 3 print foo.
# 1c. if it is divisible by 5 print Bar.
# 1d. if it is divisible by both print FooBar.

# # 1a
# for num in range(101):
#     if num % 3 == 0 and num % 5 == 0:
#         print(f"{num}: FooBar")
#     elif num % 3 == 0:
#         print(f"{num}: Foo")
#     elif num % 5 == 0:
#         print(f"{num}: Bar")
#     else:
#         print(f"{num}: Neither")


# 2. Write a function that will take an integer and return a boolean and the body of the function that is the input will evaluate if it is even and return true and if it is odd return false.
# def is_even(p: int) -> bool:

# def is_even(number: int) -> bool:
#     return number % 2 == 0


# # Ask user for input safely
# user_input = input("Enter an integer: ")

# if not user_input.strip():
#     print("Input cannot be empty.")
# else:
#     if not user_input.lstrip("-").isdigit():  # handles negative numbers too
#         print("Input must be a valid integer.")
#     else:
#         user_number = int(user_input)
#         print(is_even(user_number))


# user = input()
# user.isdigit()
# user.isnumeric()
# .isnumeric() works only for non-negative integers (e.g. "123").
# It will fail for negative numbers like "-5" and for floats like "3.14".


# def is_even(number: int) -> bool:
#     return number % 2 == 0


# # Keep asking until valid integer
# while True:
#     user_input = input("Enter an integer: ")

#     if not user_input.strip():
#         print("Input cannot be empty.")
#         continue

#     if not user_input.lstrip("-").isdigit():
#         print("Input must be a valid integer.")
#         continue

#     # Valid input -> convert to int
#     user_number = int(user_input)
#     if is_even(user_number):
#         print(f"{user_number} is an even number.")
#     else:
#         print(f"{user_number} is not an even number.")
#     break


# 3. Write a function that takes an integer and return a boolean. If it is a prime number return true and if it is not return false.

# def is_even(number: int) -> bool:
#     return number % 2 == 0

def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


user_entry = input("Enter an integer: ")

if not user_entry.strip():
    print("Entry cannot be empty.")
elif not user_entry.lstrip("-").isdigit():  # allows negative numbers to be checked
    print("Input must be a valid integer.")
else:
    value = int(user_entry)
    if is_prime(value):
        print(f"{value} is a prime number.")
    else:
        print(f"{value} is not a prime number.")
