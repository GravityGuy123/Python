# import getpass

# password = getpass.getpass("Enter your password: ")
# print("Password received (but not shown).")



# import os

# print(os.getcwd())
# print(os.cpu_count())
# print(os.name)


# Declaring Variables
# name = "GravityGuy"
# age = 13
# isFalse = False
# print(name)
# print(age)
# print("Boolean:", isFalse)

# # Using snake case for Python
# my_details = {"name": "Simon", "age": 13}
# print(my_details)

# Creating Constants involves using uppercase
# MY_DETAILS = {"name": "Simon", "age": 13}
# print(MY_DETAILS)

# # Using input to get info just like prompt in JavaScript
# user_name = input("Enter ur name ")
# print("Age:", user_name)
# print(f"Your age is {user_name}") # Using template litherals

# # Converting data types
# age = input(f"Your age is {user_name}")
# float(age)
# int(age)


# temp_input = float(input("What's the temperature in Celsius? "))
# fahrenheitDegree = fahrenheitDegree = "°F"
# fahrenheit = (temp_input * 9 / 5) + 32
# result = str(fahrenheit) + fahrenheitDegree  # Convert to string then concatenate
# print(result)

# # or use template litherals to conca
# print(f"{fahrenheit}{fahrenheitDegree}")


## Empty String
# empty_string = "."
# print(empty_string)


# num1 = 3
# num2 = 6
# result = num1 + num2
# print(result)


# dob = input("Enter your year of birth: ")
# if dob.isdigit():
#     dob = int(dob)
#     if dob < 1900 or dob > 2025:
#         print("Invalid year of birth. Please enter a valid year between 1900 and 2025.")
#     else:
#         age = 2025 - dob
#         print(f"You are {age} years old.")


# score = 4 + 2
# score2 = 2 + 3.9

# print(type(score))
# print(score2)
# print("Multiply:", 3.5 * 2.5)
# print("Subtract:", 3.5 - 2.5)
# print("Divide:", 3.5 / 2.5)
# print("Divide1:", 7 / 2)
# print("Divide2:", 7 // 2) # Using // for floor division, which returns the largest integer less than or equal to the division result


# add = 2 + 3
# print(add)

# print("Multiply:", 7 * 3)
# print("Multiply 2:", 7 ** 3)

# mod = 5 % 2
# mod2 = 5.2 % 2
# print(type(mod), mod)  # returns int
# print(type(mod2), mod2) # returns float



email = input("Enter your email address: ")
if email.count("@") != 1:
    print("There must be exactly one '@' in you email.")
elif "." not in email:
    print("There must be atleast one '.' in your email.")
else:
    if email.count("@") == 1:
        print(f"Your email: {email.lower()} is valid")
















# Is more advisable to check for all the fail cases before checking for the pass case(s)


# 9999.9