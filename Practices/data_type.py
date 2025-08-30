# Data Types
# string, int, float, list, dictionary, tuple

# name1 = "Gravity"
# name2 = "Guy"
# print(name1, name2)
# print(name1 + " " + name2)

# h1 = "Hello World"


# print(f"h1: {h1}")

# print(f"Uppercased: {h1.upper()}")
# print(f"Lowercased: {h1.lower()}")
# print(f"Titlecased: {h1.title()}")

# # Comparing Numbers
# x = 10
# y = 5

# print(x > y)
# print(x < y)

# # Simple calculator
# num1 = 15
# num2 = 5

# print(f"Num1: {num1}")
# print(f"Num2: {num2}")

# print(f"Subtract: {num1 - num2}")
# print(f"Add: {num1 + num2}")
# print(f"Divide: {num1 / num2}")
# print(f"Multiply: {num1 * num2}")


# # Getting user inputs (text)
# userInput = input("What is your name: ")
# print(f"My name is {userInput}!")
# print(f"{userInput} is a badass programmer.")


# # Getting user inputs (Number)
# age = input("How old are you? ")
# print(f"Am {age} years old")


# Converting user inputs
# height = input("What is your height? ")
# height = float(height)
# print(f"Am {height}fts tall")


# height = input("What is your height? ").strip()

# if not height:
#     print("Entry cannot be empty")
# elif not height.isdigit(): # checks if all characters in the string are digits (integers only, floats and negatives not allowed)
#     print("Entry must be a valid number")
# else:
#     # if isinstance(height, float):
#     if "." in height:
#         height = float(height)
#     else:
#         height = int(height)
#         print(f"Am {height} meters tall")



# height = input("What is your height? ").strip()
# if not height:
#     print("Entry cannot be empty")
# else:
#     try:
#         height = float(height)
#         print(f"Am {height} meters tall")
#     except ValueError:
#         print("Entry must be a valid number")
#     except Exception as e:
#         print(f"An error occurred: {e}")




# Loop until valid input is given
while True:
    height = input("What is your height? ").strip()

    if not height:
        print("Entry cannot be empty")
        continue

    try:
        height = float(height)
        print(f"Am {height} meters tall")
        break  # ✅ exit loop once valid input is given
    except ValueError:
        print("Entry must be a valid number")


# # Cleaner version
# height = input("What is your height? ").strip()

# if not height:
#     print("Entry cannot be empty")
# else:
#     try:
#         # Try converting to float (works for both int and decimal inputs)
#         height = float(height)
#         print(f"I am {height} meters tall")
#     except ValueError:
#         print("Entry must be a valid number")


# Difference between .strip(), .split(), .join() and .replace() is that: 
# .strip() removes whitespace from the beginning and end of a string
# .split() splits a string into a list of substrings based on a specified delimiter
# .join() joins a list of strings into a single string with a specified delimiter
# .replace() replaces occurrences of a specified substring with another substring in a string