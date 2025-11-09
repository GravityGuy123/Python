# # If Statements
# cars = ["audi", "bmw", "subaru", "toyota"]

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# print("\n")
# names = ['edu-crypt', 'gravityguy', 'mega-pips', 'chioma', 'victoria']
# for name in names:
#     if name == 'gravityguy':
#         print(name.upper())
#     else:
#         print(name.title())

# # Conditional Tests
# requested_toppings = 'mushroom'
# if requested_toppings != 'anchovies':
#     print("Hold the anchovies")

# # Numerical Comparisons
# age = 18
# answer = int(input("Enter your answer: "))
# if answer != 18:
#     print ("Incorrect answer")
# else:
#     print ("Your answer is correct")

# # Checking Multiple Conditions
# # Using and to check multiple coditions
# first_age = 17
# sec_age = 23
# if first_age <= 21 and sec_age >= 22:
#     print(True)
# else:
#     print(False)

# # Using or to check multiple coditions
# if first_age >= 17 or sec_age <= 30:
#     print(True)
# else:
#     print(False)

# # Checking Whether a Value Is in a List
# requested_toppings = ["mushrooms", "onions", "pineapple"]
# for toppings in requested_toppings:
#     if 'mushrooms' in toppings:
#         print("True, toppings available")
#     else:
#         print("False, toppings unavailable")

# banned_users = ["andrew", "carolina", "david"]
# user = "marie"

# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish")
# else:
#     print("You are not allowed to make any posts")

# car = "subaru"
# print("Is car == 'subaru'? I predict True.")
# print(car == "subaru")

# print("\nIs car == 'audi'? I predict False.")
# print(car == "audi")


# age = 18
# if age >= 18:
#     print("You are old enough to vote")


# # If Else Statements
# age = 17
# if age >= 18:
#     print("You are old enough to vote")
#     print("Have you registered your vote")
# else:
#     print("Sorry, you are too young to vote")
#     print("Pls register your vote when you nturn 18")


# # The if-elif-else Chain
# age = int(input("Enter your age: "))

# if age < 4:
#     print("Admission is free")
# elif age >= 4 and age <= 18:
#     print("Admission cost is $25")
# else:
#     print("Admission cost is $40")

# The code below does the same thing are the one above
# if age < 4:
#     print("Your admission cost is $0.")

# elif age < 18:
#     print("Your admission cost is $25.")
# else:
#     print("Your admission cost is $40.")


# # Using if Statements with Lists
# requested_toppings = ["mushrooms", "green peppers", "extra cheese", "cabbages"]
# for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}")
# print("\nFinished making you pizza")


# for requested_topping in requested_toppings:
#     if requested_topping == "cabbages":
#         print('Sorry, we are out of "Cabbages" right now.')
#     else:
#         print(f"Adding {requested_topping}")
#     print("\nFinished making you pizza")


# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}")
#     print("\nFinished making you pizza")
# else:
#     print("Are you sure you want a plain pizza?")


# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping not in available_toppings:
#         print(f'Sorry, we dont have "{requested_topping}" right now.')
#     else:
#         print(f"Adding {requested_topping}")

# print("\nFinished making you pizza")


# # Checking UserNames
# # a.
# current_users = ["DevDemon", "Paragon123", "Edu-Crypt", "DevDiva", "De_Hunter", "John173"]
# print(f"\nCurrent Users: {current_users}")

# # b.
# new_users = ["KD_Banger", "Edu-Crypt", "DeHunter", "John173", "Badest-X", "Raone"]
# print(f"\nNew Users: {new_users}\n")
# current_users_copy = list(value.lower() for value in current_users)

# for new_user in new_users:
#     if new_user.lower() in current_users_copy:
#         print(f"Sorry, {new_user} is taken. Pls choose another username")
#     else:
#         print(f"{new_user} is available.")
#         current_users.append(new_user)

# print(f"\nCurrent Users: {current_users}")


# # Styling Your if Statements
# # Proper spacing improves code readability
# if age < 4:
#     is better than
# if age<4: