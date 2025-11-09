# Try It Yourself
# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line evaluates to True or False.
# • Create at least ten tests. Have at least five tests evaluate to True and another five tests evaluate to False.
# 5-2. More Conditional Tests: You don’t have to limit the number of tests you create to ten. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

# 5.1a
car = "subaru"
age = 17
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

# 5.1b


# 5.1c
print("\nIs age <= 17? I predict True.")
print(age <= 17)


# 5-2. More Conditional Tests:
# 5-2a.
if car == "subaru":
    print(car == "subaru" )

if car != "subaru":
    print(car != "subaru" )

# 5-2b.
item = "Mouse"
if item == "Mouse":
    print(car.lower())

if car != "Mouse":
    print(car.lower())

# 5-2c.
if not age >= 18:
    print(not age >= 18)

if age == 17:
    print(age == 17)

# 5-2d.
if age > 10 and age <= 20:
    print("Qualified")

if not age > 10 and age <= 20:
    print("Unqualified")

if age > 10 or age <= 20:
    print("Qualified")

if not age > 10 or age <= 20:
    print("Unqualified")

# 5-2e.
colors = ['red', 'blue', 'purple', 'orange']

if "blue" in colors:
    print(len(colors))

if "black" in colors:
    print(colors)

# 5-2f.
if "black" not in colors:
    print(colors)

if "black" not in colors:
    print(colors)


# Try It Yourself
# 5.3a. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# 5.3b. Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
# 5.3c. Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
# 5.4a. Alien Colors #2: Choose a color for an alien as you did in Exercise 5.3, and write an if-else chain.
# 5.4b. If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# 5.4b. If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# 5.4c. Write one version of this program that runs the if block and another that runs the else block.
# 5.5a. Alien Colors #3: Turn your if-else chain from Exercise 5.4 into an if-elifelse chain.
# 5.5b. If the alien is green, print a message that the player earned 5 points.
# 5.5c. If the alien is yellow, print a message that the player earned 10 points.
# 5.5d. If the alien is red, print a message that the player earned 15 points.
# 5.5e. Write three versions of this program, making sure each message is printed for the appropriate color alien.
# 5.6a. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
# 5.6b. If the person is less than 2 years old, print a message that the person is a baby.
# 5.6c. If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# 5.6d. If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# 5.6e. If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# 5.6f. If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# 5.6g. If the person is age 65 or older, print a message that the person is an elder.
# 5.7a. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
# 5.7b. Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

# 5.3a. Alien Colors #1:
alien_color = 'red'

# 5.3b.
if alien_color == 'green':
    print("Player just earned 5 points")

# 5.3c.
if alien_color == 'red':
    print("Player just earned 5 points")

# 5.4a. Alien Colors #2:
alien_color = 'green'

# 5.4b.
if alien_color == 'green':
    print("Player just earned 5 points for shooting the alien")

# 5.4c.
elif alien_color != 'green':
    print("Player just earned 10 points")

# 5.4d.
if alien_color == 'green':
    print("Player just earned 5 points for shooting the alien")
else:
    print("Player just earned 10 points")

# 5.5a. Alien Colors #3:
alien_color = 'yellow'

# 5.5b.
if alien_color == 'green':
    print("Player earned 5 points")

# 5.5c.
elif alien_color == 'yellow':
    print("Player earned 10 points")

# 5.5c.
else:
    print("Player earned 15 points")

# 5.5d.

# 5.6a. Stages of Life:
age = 13

# 5.6b.
if age < 2:
    print("User is a Baby")

# 5.6c.
elif age < 4:
    print("User is a Toddler")

# 5.6d.
elif age < 13:
    print("User is a Kid")

# 5.6d.
elif age < 20:
    print("User is a Teenager")

# 5.6d.
elif age < 65:
    print("User is an Adult")

# 5.6d.
else:
    print("User is an Elder")

# 5.7. Favorite Fruit:
# 5.7a.
favorite_fruits = ['strawberries', 'apples', 'pineapples']

# 5.7b.
if 'strawberries' in favorite_fruits:
    print('You really like "strawberries"')
else:
    print('You really dont like "strawberries"')

if 'apples' in favorite_fruits:
    print('You really like "apples"')
else:
    print('You really dont like "apples"')

if 'pineapples' in favorite_fruits:
    print('You really like "pineapples"')
else:
    print('You really dont like "pineapples"')

if 'avocado' in favorite_fruits:
    print('You really like "avocado"')
else:
    print('You really dont like "avocado"')

if 'guava' in favorite_fruits:
    print('You really like "guava"')
else:
    print('You really dont like "guava"')


# Try It Yourself
# 5.8a. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:
# 5.8b. If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# 5.8c. Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
# 5.9a. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# 5.9b. If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message is printed.
# 5.10a. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# 5.10b. Make a list of five or more usernames called current_users.
# 5.10c. Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
# 5.10d. Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
# 5.10e. Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
# 5.11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# 5.11a. Store the numbers 1 through 9 in a list.
# 5.11b. Loop through the list.
# 5.11c. Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

# 5.8a. Hello Admin:
users = ["admin", "gravityguy", "chioma", "ashioma", "divine"]

# 5.9a. Check if there are users
if users:
    # 5.8b & 5.8c: Greet users
    for user in users:
        if user == "admin":
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thanks for logging in again.")
else:
    # 5.9b. No users
    print("We need to find some users")

# 5.9c. Remove all users safely
if users:
    users.clear()  # safest way to empty the list
    print(f"All users have been removed: Users: {users}")
    print("We need to find some users")

# 5.10. Checking Usernames:
# 5.10a.
current_users = ["DevDemon", "Edu-Crypt", "megapips", "DevDiva", "Paragon123", "John173"]
print(f"\nCurrent Users: {current_users}\n")

# 5.10b.
new_users = ["Raone", "KD_Banger", "BiteCruncher", "edu-crypt", "Paragon123", "JOHN", "MegAPiPs", "Badest-X"]
print(f"New Users: {new_users}\n")

# Using list comprehension to generate an independent copy
check_current_users = list(value.lower() for value in current_users)

# 5.10c.
for new_user in new_users:
    
# 5.10d.
    if new_user.lower() in check_current_users:
        print(f"{new_user} is taken enter a new username")
    else:
        print(f"{new_user} is available")
        current_users.append(new_user)

print(f"Current Users: {current_users}")


# 5.11. Ordinal Numbers:
# 5.11a.
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 5.11b.
for ordinal_number in ordinal_numbers:

    # 5.11c.
    if ordinal_number == 1:
        print(f"\n{ordinal_number}st")
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")
    elif ordinal_number == 3:
        print(f"{ordinal_number}rd")
    else:
        print(f"{ordinal_number}th")


# # A more elegant and scalable way to handle ordinal numbers to any range

# # 5.11. Ordinal Numbers:

# # 5.11a. List of numbers
# ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# # 5.11b. Function to get ordinal suffix
# def ordinal(n):
#     if 10 <= n % 100 <= 20:
#         suffix = "th"
#     else:
#         suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
#     return f"{n}{suffix}"


# # 5.11c. Loop through numbers and print with suffix
# for ordinal_number in ordinal_numbers:
#     print(ordinal(ordinal_number))


# Try It Yourself
# 5.12. Styling if statements: Review the programs you wrote in this chapter, and make sure you styled your conditional tests appropriately.
# 5.13. Your Ideas: At this point, you’re a more capable programmer than you were when you started this book. Now that you have a better sense of how real-world situations are modeled in programs, you might be thinking of some problems you could solve with your own programs. Record any new ideas you have about problems you might want to solve as your programming skills continue to improve. Consider games you might want to write, data sets you might want to explore, and web applications you’d like to create.

# 5.12.
print("Done")

# 5.13.