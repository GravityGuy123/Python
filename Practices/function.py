# py function.py

# def create_multiplier(factor):
#     """Creates a function that multiplies by a specific factor"""

#     def multiplier(number):
#         return number * factor  # 'factor' is captured from outer scope

#     return multiplier


# # Create specialized functions
# double = create_multiplier(2)
# triple = create_multiplier(3)

# print(double(5))  # Output: 10
# print(triple(5))  # Output: 15

# def greet():
#     print("Hello!")
#     print("Nice to meet you!")
#     print("Have a great day!")

# greet()

# def sum(a, b):
#     return a + b

# print(sum(2, 3))


# def exp(num1, num2):
#     print(num1 * num2)

# exp(4, 10)


# def greet_user():
#     """ Display a simple greeting. """
#     print("Hello!")

# greet_user()

# Passing Arguments (types)
# 1. Positional Arguments
# 2. Keyword Arguments


# # Positional Arguments
# # Where position of arguments matters

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name}")

# describe_pet('hamster', 'harry')

# # Multiple Function Calls
# # You can call a function as many times as you want

# describe_pet('dog', 'bubly')
# describe_pet('parrot', 'saskay')


# # Order Matters in Positional Arguments
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name}")

# describe_pet("harry", "hamster")


# # Keyword Arguments
# # Where an argument is associated with a keyword. ()
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet(animal_type="hamster", pet_name="harry",)


# # Position os arguments does not matter
# describe_pet(pet_name="harry", animal_type="hamster")


# # Default Values
# def describe_pet(pet_name, animal_type = 'dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name="willie")


# # Equivalent Function Calls
# def describe_pet(pet_name, animal_type = 'dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hary', 'hamster')
# describe_pet(pet_name='mawi', animal_type='parrot')
# describe_pet(animal_type='bunny', pet_name='clover')


# # Avoiding Argument Errors
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet()


# import random

# # 1. List of descriptive words
# descriptiveWords = ["vibrant", "sleek", "modern", "bold", "minimalist", "elegant", "dynamic", "creative", "innovative", "aesthetic", "stunning", "professional", "unique", "refined", "energetic", "charming", "sophisticated", "graceful", "eye-catching", "fresh", "artistic", "powerful", "captivating", "stylish", "versatile", "clean", "bright", "luxurious", "radiant", "polished"]

# # 2. Get user's name
# use_name = input("What your name? ")

# # 3. Pick a random word
# random_word = random.choice(descriptiveWords)

# def describeWords(name, word):
#     """Describe a website using a random descriptive word."""
#     print(f"Hello {name}, your website is looking {word}")

# describeWords("GravityGuy", random_word)


# # Default Values
# # Setting a default value for an argument allows you to make that argument optional during function calls.
# def descibe_pet(pet_name, animal_type="dog"):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# descibe_pet("bubbly")
# descibe_pet(pet_name="bubbly")


# # 1.
# numbers = []

# # 3.
# def add_numbers(a, b):
#     print(f"{a} + {b} = {a + b}")
#     return a + b

# # 2.
# for number in range(10):

#     # 4.
#     result = add_numbers(number * 5, number * number)

#     # 5.
#     numbers.append(result)

# # 6.
# print(f"Numbers: {numbers}")


# # Return Values
# # Returning a Simple Value
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# # Making an Argument Optional
# def get_formatted_name(first_name, last_name, middle_name =''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(f"1. {musician}")

# musician = get_formatted_name('jimi', 'hooker', 'hendrix')
# print(f"2. {musician}")


# # Returning a Dictionary
# def build_person(first_name, last_name):
#     """ Return a dictionary of information about a person """
#     person = {'first_name': first_name, 'last_name': last_name}
#     return person

# name = build_person('jimi', 'hendrix')
# print(name)


# def build_person(first_name, last_name, age = None):
#     """ Return a dictionary of information about a person """
#     person = {'first_name': first_name, 'lastname': last_name}

#     if age:
#         person['age'] = age

#     return person

# person1 = build_person('jimi', 'hendrix')
# print('\n', person1)

# person1 = build_person('jimi', 'hendrix', 13)
# print('\n', person1)


# # Using a Function with a while Loop
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# # This is an infinite loop!
# is_active = True

# while is_active:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ").title()
#     l_name = input("Last name: ").title()
#     contd = input("Would you like to let someone else respond? (yes / no) ")

#     if contd.lower() == 'no':
#         is_active = False

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# # Printing a List of People Who Responded after the Loop ends
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# # This is an infinite loop until user stops it
# is_active = True
# names = []  # store all names here

# while is_active:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ").title()
#     l_name = input("Last name: ").title()

#     formatted_name = get_formatted_name(f_name, l_name)
#     names.append(formatted_name)  # add to list

#     contd = input("Would you like to let someone else respond? (yes / no): ").lower()
#     if contd == "no":
#         is_active = False

# # Print all names after loop ends
# print("\nHello to everyone:")
# for name in names:
#     print(f" - {name}")


# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# # This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     if f_name.lower() == 'q' or l_name.lower() == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# # Passing a List
# def greet_users(names):
#     """Print a simple greeting to each user in the list."""

#     for name in names:
#         message = f"\nHello {name.title()}"
#         print(message)


# user_names = ['hannah', 'ty', 'margot']
# greet_users(user_names)


# # Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"\nPrinting Model: {current_design}")
#     completed_models.append(current_design)

# # Display all completed models
# print("\nThe following models have been printed:")

# for completed_model in completed_models:
#     print(completed_model)


# def print_models(unprinted, completed):
#     """"Print models and move them into completed models"""

#     while unprinted:
#         current_design = unprinted.pop()
#         print(f"Printing Models: {current_design}")
#         completed.append(current_design)

# def show_completed_models(completed):
#     """Show completed models"""

#     print("\nCompleted models:")
#     for complete in completed:
#         print(complete)

# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# # Preventing a Function from Modifying a List
# def print_models(unprinted, completed):
#     while unprinted:
#         current_design = unprinted.pop()
#         print(f"Printing: {current_design}")
#         completed.append(current_design)

# def show_printed_designs(completed):
#     print("\nThe following models have been printed:")

#     for complete in completed:
#         print(complete)

# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_designs = []

# print_models(unprinted_designs[:], completed_designs)
# show_printed_designs(completed_designs)

# print(f"\nUnprinted Designs: {unprinted_designs}")
# print(f"\nCompleted Designs: {completed_designs}")


# # Passing an Arbitrary Number of Arguments
# Using * to accept as many arguments as possible

# def make_pizza(*toppings):
#     """Print the list of toppings"""
#     print(toppings)
#     # print(type(toppings))

# make_pizza("pepperoni")
# make_pizza("mushrooms", "green peppers", "extra cheese")


# # Looping through
# def make_pizza(*toppings):
#     """Print the list of toppings"""

#     for topping in toppings:
#         print(f"\n- {topping}")

# make_pizza("pepperoni")
# make_pizza("mushrooms", "green peppers", "extra cheese")


# # Mixing Positional and Arbitrary Arguments
# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")

#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(16, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# # Using Arbitrary Keyword Arguments
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last

#     return user_info

# user_profile = build_profile('albert', 'einstein', location = 'princeton', field='physics')

# print(user_profile)


# def build_profile(first, last, **user_info):
#     """Build a person's profile with the provided information"""

#     profile = {"first_name": first, "last_name": last}
#     profile.update(user_info)

#     return profile


# user_info = build_profile("Gravity", "guy", state="Anambra", country="Nigeria")
# print(user_info)


# # Storing Your Functions in Modules
# # Importing an Entire Module
# import pizza

# pizza.make_pizza(16, "pepperoni")
# pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# When you import the entire module, you need to use the module name as a prefix + . + function name to call a function from the module.


# # Importing Specific Functions
# from func import greet_person

# greet_person('abigael')
# greet_person('dani')


# from func import introduce

# introduce('dani', 23)
# introduce('emily', 17)


# # Using as to Give a Function an Alias
# from pizza import make_pizza as mp

# mp(9, "mushrooms", "green peppers", "extra cheese")


# from func import introduce as intro

# intro('gravityguy', 27)


# # Using as to Give a Module an Alias
# import pizza as p

# p.make_pizza(16, "pepperoni")
# p.make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# # Importing All Functions in a Module
# # You can tell Python to import every function in a module by using the asterisk (*) operator:

# from pizza import *

# make_pizza(16, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# Try It Yourself
# 8.15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
# 8.16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches: import module_name from module_name import function_name from module_name import function_name as fn import module_name as mn from module_name import *
# 8.17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.


