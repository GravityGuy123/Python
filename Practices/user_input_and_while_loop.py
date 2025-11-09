# py user_input_and_while_loop.py

# .pop() (Fast, removes from the end.
# .pop(0) (Slow, removes from the beginning.)
# .remove() (Slow, searches for the value and removes by value.)


# message = input('Tell me sth and I will repeat it back to you: ')
# print(message)


# # Writing Clear Prompts
# name = input('Please enter your name: ')
# print(f'Hello {name}')


# # Multi-line Prompts
# # Prompts longer than one line
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")

# user_info = 'Hi there'
# user_info += '\nPlease enter your name: '
# name = input(user_info)
# print('Hello', name)


# # Using int() to Accept Numerical Input
# age = input('How old are you: ')
# age = int(age)

# print(age >= 18)

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")


# # The Modulo Operator
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print(f'\nThe number {number} is Even')
# else:
#     print(f'\nThe number {number} is Odd')


# # Introducing while Loops
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# print("\n")
# number = 10
# while number >= 1:
#     print(number)
#     number -= 2


# # Letting the User Choose When to Quit
# prompt = "\nTell me sth and I'll repeate it: "
# prompt += "\nEnter 'quit' to end the program: "
# message = ""
# while message != 'quit':
#     message = input(prompt)

#     # Quit regardless of the case ends the program
#     if message.lower() == 'quit':
#         break
#     print(message)


# # Using a Flag
# prompt = "\nTell me sth and I'll repeate it: "
# prompt += "\nEnter 'quit' to end the program: "

# active = True
# while active:
#     message = input(prompt)

#     if message.lower() == 'quit':
#         active = False
#     else:
#         print(message)


# # Using break to Exit a Loop
# user_input = "\nPlease enter the name of a city you have visited: "
# user_input += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(user_input)

#     if city.lower() == 'quit':
#         break
#     else:
#         print(f"I would love to visit {city}")


# # Using continue in a Loop
# current_number = 0
# while current_number <= 10:
#     current_number += 1

#     # skipping a value whenever the modulo is 0
#     if current_number % 2 == 0:
#         continue
#     print(current_number)


# # Avoiding Infinite Loops
# x = 1
# while x <= 5:
#     print(x)
#     x += 1


# # 7.4. Pizza Toppings:
# prompt = "\nPlease enter a pizza topping for your pizza: "
# prompt += "\nEnter 'quit' to end the program: "

# pizza_toppings = ""
# toppings = []

# while pizza_toppings != 'quit':
#     pizza_toppings = input(prompt)

#     if pizza_toppings.lower() == "quit":
#         break
#     else:
#         print(f"I want {pizza_toppings}")
#         toppings.append(pizza_toppings.title())

# print(f"My toppings are: {toppings}")


# Using a while Loop with Lists and Dictionaries
# Moving Items from One List to Another
# Start with users that need to be verified, and an empty list to hold confirmed users.

# unconfirmed_users =['alice', 'brian', 'candace']
# confirmed_users = []

# # Verify each user until there are no more unconfirmed users.
# # Move each verified user into the list of confirmed users.
# while unconfirmed_users:
#     # the lists starts validating from the end because of pop()
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying User: {current_user.title()}")
#     confirmed_users.append(current_user)

# # Display all confirmed users.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# # Removing All Instances of Specific Values from a List
# pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)


# # Filling a Dictionary with User Input
# responses = {}

# # Set a flag to indicate that polling is active.
# polling_active = True

# while polling_active:
#     # Prompt for the person's name and response.
#     name = input("\nWhat is your name: ")
#     mountain = input("\nWhich mountain would you like to climb today? ")

#     # Store the response in the dictionary.
#     responses[name] = mountain

#     # Find out if anyone else is going to take the poll.
#     repeate = input("\nWould you like to let someone else respond? (yes / no) ")

#     if repeate.lower() == "no":
#         polling_active = False

# # Polling is complete. Show the results.
# print("\n--- Poll Reslts ---")

# for name, mountain in responses.items():
#     print(f"{name} would like to climb {mountain}")

# print(f"Responses: {responses}")


# Try It Yourself
# 7.8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
# 7.9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
# 7.10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

# 7.8. Deli:
sandwich_orders = ["ham and cheese", "pastrami", "veggie", "chicken", "tuna", "beef"]
finished_sandwiches = []

for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order.title()} Sandwich")
    finished_sandwiches.append(sandwich_order)

print(f"\nFinished Sandwiches: {finished_sandwiches}")


# 7.9. No Pastrami:
sandwich_orders = ["ham and cheese", "pastrami", "veggie", "chicken", "pastrami", "tuna", "pastrami", "egg"]

finished_sandwiches = []

print('\n \nDeli has runout of "pastrami"')

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

for sandwich in sandwich_orders:
    print(f"I made your {sandwich.title()} Sandwich")
    finished_sandwiches.append(sandwich)

print(f"\nFinished Sandwiches: {finished_sandwiches}")


# 7.10. Dream Vacation:
vacation_responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    dream_vacation = input("\nIf you could visit one place in the world, where would you go? ")
    
    vacation_responses[name] = dream_vacation
    
    repeate = input("\nWould you like to let someone else respond? (yes / no) \n")
    if repeate.lower() == "no":
        polling_active = False

for name, vacation in vacation_responses.items():
    print(f"{name} would like to visit {vacation}")
    
print(f"\nVacation Responses: {vacation_responses}")