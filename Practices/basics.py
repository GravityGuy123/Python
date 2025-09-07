# BASICS
# name1 = "John"
# name2 = "Doe"

# print(f"Hello {name1} {name2}")

# my_name = input("What is your name: ")
# print(f"My name is {my_name}!!!")
# print(f"My name({my_name}) is {len(my_name)} characters long.")

# if my_name.isupper():
#     print("Uppercase")
# elif my_name.islower():
#     print("Lowercase")
# else:
#     print("Tilecase")


# user_age = input("How old are you? ")
# user_age = int(user_age)
# print(f"You will be {user_age + 1} next year.")

# num1 = 23
# num1 + 1
# num1 = num1 + 1
# print(num1)

# bacon = 20
# bacon + 1
# print(bacon)

# # 7. What should the following two expressions evaluate to?
# print('spam' + 'spamspam')
# print('spam' * 3)

# print("I have eaten " + 99 + " burritos.")


# print('I told my friend, "Python is my favorite language!"')
# print("The language 'Python' is named after Monty Python, not the snake.")
# print("One of Python's strengths is its diverse and supportive community.")

# # Changing Case
# sentence = "hi there"
# print(f'Normal: {sentence}')
# print(f'Uppercase: {sentence.upper()}')
# print(f'Title: {sentence.title()}')


# first_name = "gravity"
# last_name = "guy"
# full_name = f"{first_name} {last_name}"
# print(f"My full name is {full_name.upper()}")

# # Creating new lines
# print(f"My full name is\n{full_name.upper()}")

# print("Languages:\n\tPython\n\tC\n\tJavaScript")
# x, y, z = 5, 3, 1
# # print("x\n\ty")
# print("x\ny\nz")
# print(f"{x}\n{y}\n{z}")


# Handling WhiteSpaces using lstrip(), rstrip() and strip()

# # Removing spaces on the left with lstrip()
# user_name = input("What is your name: ").lstrip()
# print(f"User's name is {user_name}")

# name1 = "             Hi Love"
# print(name1.lstrip()) # Hi Love (with no whitespace on the left)


# # Removing spaces on the right with rstrip()
# name2 = "Hola mi amor             "
# print(name2.rstrip())  # Hola mi amor (with no whitespace on the right)


# # Removing spaces from both left and right with strip()
# name3 = "            Hola mi amor             "
# print(name3.strip())  # Hola mi amor (with no whitespace on either side)


# # Practice 2.3 - 2.7
# # 2.3. Personal Message:
# name1 = "ChiSom"
# print(f"Hello {name1}, would you like to learn some Python today?")

# # 2.4 Name Cases:
# print(f"Lowercased Name: {name1.lower()}")
# print(f"Uppercased Name: {name1.upper()}")
# print(f"Titlecased Name: {name1.title()}")

# # 2.5 Famous Quote:
# print('Albert Einstein once said "A person who never made a mistake never tried anything new."')

# # 2.6 Famous Quote 2:
# famous_person = "GravityGuy"
# print(f'{famous_person} once said "At the end of the day, its not the years in the life that matters but the life lived, time spent, memories made $ legacies established."')

# # 2.7. Stripping Names:
# # print("Languages:\n\tPython\n\tC\n\tJavaScript")
# name = "       MegaPips         "
# print(f"Normal: {name}")
# print(f"LeftStrip: {name.lstrip()}")
# print(f"RightStrip: {name.rstrip()}")
# print(f"Strip: {name.strip()}")


# Numbers

# # Integers
# num1 = 5
# num2 = 2

# print(f'Add: {num1 + num2}')
# print(f'Subtract: {num1 - num2}')
# print(f'Divide: {num1 / num2}')
# print(f'Multiply: {num1 * num2}')
# print(f'Exponent: {num1 ** num2}') # Raised to power
# print(f'Modulus: {num1 % num2}') # Remainder


# # Floats
# print("Working with floats")
# num3 = 5.0
# num4 = 2.5

# print(f'Add: {num3 + num4}')
# print(f'Subtract: {num3 - num4}')
# print(f'Divide: {num3 / num4}')
# print(f'Multiply: {num3 * num4}')
# print(f'Exponent: {num3 ** num4}') # Raised to power
# print(f'Modulus: {num3 % num4}') # Remainder


# # Integers and Floats
# # When you divide any two numbers, even if they are integers that result in a whole number, you’ll always get a float:

# print(f"Dividing always result in floats: {4 / 2}") # 2.0

# # Mixing integers and floats will result in floats
# print(f"Mixing int and float: {5.5 + 2}")


# # Underscores in Numbers
# num1 = 4_000_000_000
# print(num1)


# # Multiple Assignment in one line
# x, y, z = 5, 3, 1
# # print("x\n\ty")
# print("x\ny\nz")
# print(f"{x}\n{y}\n{z}")
# # print("Languages:\n\tPython\n\tC\n\tJavaScript")

# print(f"Adding: {x + z}")


# # Constants
# MAX_CONNECTIONS = 5000

# # Practices 2.8 - 2.9
# # 2.8. Number Eight:
# print(f"Add: {5 + 3}")
# print(f"Subtract: {10 - 2}")
# print(f"Divide: {24 / 3}")

# # 2.9. Favorite Number:
# favorite_number = 3
# print(f"My favorite number is {favorite_number}")

# Comments
# # Practice 2.10
# # 2.10. Adding Comments:

# # Getting a usernames
# name = input("What is you name: ")


# “The Zen of Python” by Tim Peters
# avoid complexity and aim for simplicity whenever possible
# Simple is better than complex.
# Complex is better than complicated.
# Readability counts.
# There should be one-- and preferably only one --obvious way to do it.
# Now is better than never.


# while True:
#     weather = input("Is it rainy or sunny? ").lower().strip()
#     if not weather:
#         print("Entry cannot be empty")
#     elif weather != "rainy" and weather != "sunny":
#         print('Entry must be "rainy" or "sunny"')
#     else:
#         if weather == "rainy":
#             print("Take an umbrella")
#         elif weather == "sunny":
#             print("Umbrella not needed")
#         print(f"The weather is {weather}")
#         break


# # Lists
bicycles = ["trek", "cannondale", "redline", "specialized"]
# print(bicycles)

# # Accessing Elements in a List
# print(f"First: {bicycles[0]}\n 2nd: {bicycles[1]}\n 3rd: {bicycles[2]}")

colors = ['black', 'red', 'blue', 'orange', 'white', 'pink', 'purple']
red = colors[1]
print(f"The color is {red}")

print(f"My bicycle was a {bicycles[0].upper()}")