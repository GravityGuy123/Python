# Try It Yourself
# 7.1. Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”
# 7.2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
# 7.3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

# 7.1. Rental Car:
rental_car = input("What kind of rental car would you like? ")
print(f"\nLet me see if I can find you a {rental_car}\n")

# 7.2. Restaurant Seating:
restaurant_sitting = input("How many people are in your dinner group? ")
restaurant_sitting = int(restaurant_sitting)

if restaurant_sitting > 8:
    print("\nYou’ll have to wait for a table.\n")
else:
    print("\nYour table is ready\n")

# 7.3. Multiples of Ten:
number = input("Enter any number: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10\n")
else:
    print(f"\nThe number {number} is not a multiple of 10\n")


# Try It Yourself
# 7.4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.
# 7.5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
# 7.6a. Three Exits: Write different versions of either Exercise 7.4 or Exercise 7.5 that do each of the following at least once:
# 7.6b. Use a conditional test in the while statement to stop the loop.
# 7.6b. Use an active variable to control how long the loop runs.
# 7.6c. Use a break statement to exit the loop when the user enters a 'quit' value.
# 7.7. Infinity: Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)

# 7.4. Pizza Toppings:
prompt = "\nPlease enter a pizza topping for your pizza: "
prompt += "\nEnter 'quit' to end the program: "

pizza_toppings = ""

while pizza_toppings != "quit":
    pizza_toppings = input(prompt)

    if pizza_toppings.lower() == "quit":
        break
    else:
        print(f"I want {pizza_toppings}")

# 7.5. Movie Tickets:
user_age = input("How old are you? ")
user_age = int(user_age)

if user_age < 3:
    print("Your movie ticket is free")
elif user_age >= 3 and user_age <= 12:
    print("Your movie ticket is $10")
else:
    print("Your movie ticket is $15")

# 7.6. Three Exits:
# version 1
# 7.6a.
prompt = "\nPlease enter a pizza topping for your pizza: "
prompt += "\nEnter 'quit' to end the program: "

pizza_toppings = ""

while pizza_toppings != "quit":
    pizza_toppings = input(prompt)

    if pizza_toppings.lower() == "quit":
        break
    else:
        print(f"I want {pizza_toppings.title()}")

# version 2
# 7.6b.
prompt = "\nPlease enter a pizza topping for your pizza: "
prompt += "\nEnter 'quit' to end the program: "

active = True

while active:
    pizza_toppings = input(prompt)

    if pizza_toppings.lower() == "quit":
        active = False
    else:
        print(f"I want {pizza_toppings.title()}")

# version 3
# 7.6c.
prompt = "\nPlease enter a pizza topping for your pizza: "
prompt += "\nEnter 'quit' to end the program: "

while True:
    pizza_toppings = input(prompt)

    if pizza_toppings.lower() == "quit":
        break
    else:
        print(f"I want {pizza_toppings.title()}")

# 7.7. Infinity:
number = 5
while number <= 20:
    print(number)


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