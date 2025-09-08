# Practices

# Try It Yourself
# Try these short programs to get some firsthand experience with Python’s lists. You might want to create a new folder for each chapter’s exercises to keep them organized.
# 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

# 3.1.
names = ["EduCript", "Chioma", "Mega-Pips", "Victoria", "Esther"]
print(f"Friend 1: {names[0]}")
print(f"Friend 2: {names[1]}")
print(f"Friend 3: {names[2]}")
print(f"Friend 4: {names[3]}")
print(f"Friend 5: {names[4]}")

# 3.2.
print(f"{names[0]} is my friend")
print(f"{names[1]} is my friend")
print(f"{names[2]} is my friend")
print(f"{names[3]} is my friend")
print(f"{names[4]} is my friend")

# 3.3.
cars = ["honda", "lexus", "mazda", "benz", "camry"]
print(f"I would like to own a {cars[0].title()}")
print(f"I would like to own a {cars[1].title()}")
print(f"I would like to own a {cars[2].title()}")
print(f"I would like to own a {cars[3].title()}")
print(f"I would like to own a {cars[4].title()}")


# Practices
# Try It Yourself
# The following exercises are a bit more complex than those in Chapter 2, but they give you an opportunity to use lists in all of the ways described.

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.


# 3.4. Guest List:
dinner_list = ['mmesoma', 'chioma', 'daniella']
print(f"\nHi {dinner_list[0]}, I would like to invite you to dinner")
print(f"Hi {dinner_list[1]}, I would like to invite you to dinner")
print(f"Hi {dinner_list[2]}, I would like to invite you to dinner")

# 3.5. Changing Guest List:
# 3.5a.
print(f"{dinner_list[1]} can't make it to the dinner")

# 3.5b.
dinner_list[1] = "chinecherem"

# 3.5c
print("\n2nd set of dinner invitaion\n")
print(f"Hi {dinner_list[0]}, I would like to invite you to dinner")
print(f"Hi {dinner_list[1]}, I would like to invite you to dinner")
print(f"Hi {dinner_list[2]}, I would like to invite you to dinner")

# 3.6. More Guests:
# 3.6a.
print("Found a bigger table so more people are invited")

# 3.6b.
dinner_list.insert(0, "oluchi")

# 3.6c.
dinner_list.insert(2, 'chisom')

# 3.6d.
dinner_list.append('stella')

# 3.6e.
print("\n3rd set of dinner invitaion\n")
print(f"Hi {dinner_list[0]}, I would like to invite you to dinner")
print(f"Hi {dinner_list[1]}, I would like to invite you to dinner")
print(f"Hi {dinner_list[2]}, I would like to invite you to dinner")
print(f"Hi {dinner_list[3]}, I would like to invite you to dinner")
print(f"Hi {dinner_list[4]}, I would like to invite you to dinner")
print(f"Hi {dinner_list[5]}, I would like to invite you to dinner")

# 3.7. Shrinking Guest List:
# 3.7a.
print("\nI can invite only two people for dinner")

# 3.7b.
print(f"\nAm sorry {dinner_list[-1]}, I can't invite to dinner as the table won't arrive in time.")
dinner_list.pop()

print(f"\nAm sorry {dinner_list[-1]}, I can't invite to dinner as the table won't arrive in time.")
dinner_list.pop()

print(f"\nAm sorry {dinner_list[-1]}, I can't invite to dinner as the table won't arrive in time.")
dinner_list.pop()

print(f"\nAm sorry {dinner_list[-1]}, I can't invite to dinner as the table won't arrive in time.\n")
dinner_list.pop()

# 3.7c.
print(f"{dinner_list[0]}, you re still invited to dinner.")
print(f"{dinner_list[1]}, you re still invited to dinner.")

# 3.7d.
del dinner_list[0]
del dinner_list[0]
print(f'\nDinner List: {dinner_list}')