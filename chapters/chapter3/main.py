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


# Try It Yourself
# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# a. Store the locations in a list. Make sure the list is not in alphabetical order.
# b Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
# c. Use sorted() to print your list in alphabetical order without modifying the actual list.
# d. Show that your list is still in its original order by printing it.
# e. Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# f. Show that your list is still in its original order by printing it again.
# g. Use reverse() to change the order of your list. Print the list to show that its order has changed.
# h. Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# i. Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# j. Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 42), use len() to print a message indicating the number of people you are inviting to dinner.
# 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

# 3.8 Seeing the World
# 3.8a
travel_countries = ["France", "America", "China", "Dubai", "Australia", "Tokyo"]

# 3.8b
print(f"\nOriginal List: {travel_countries}")

# 3.8c
print(f"\nTemp Sorted List: {sorted(travel_countries)}")

# 3.8d
print(f"\nOriginal List: {travel_countries}")

# 3.8e
print(f"\nTemp Reverse Sorted List: {sorted(travel_countries, reverse=True)}")

# 3.8f
print(f"\nOriginal List: {travel_countries}")

# 3.8g
travel_countries.reverse()
print(f"\nReverse Changed List 1: {travel_countries}")

# 3.8h
travel_countries.reverse()
print(f"\nReverse Changed List 2: {travel_countries}")

# 3.8i
travel_countries.sort()
print(f"\nSort Changed List 1: {travel_countries}")

# 3.8j
travel_countries.sort(reverse=True)
print(f"\nReverse Sort Changed List 1: {travel_countries}")

# 3.9 Dinner Guests:
print(f"Number of dinner guests is {len(dinner_list)}")

# 3.10 Every Function
languages = ["Spanish", "French", "Chinese", "Portuguese", "Madrian", "Hindi"]

print("Original list of languages:")
print(languages)

# Append a new language
languages.append("Arabic")
print("\nAfter append:")
print(languages)

# Insert a language at a specific position
languages.insert(2, "German")
print("\nAfter insert at index 2:")
print(languages)

# Remove a language using del
del languages[3]
print("\nAfter deleting the element at index 3:")
print(languages)

# Remove a language using pop
popped_language = languages.pop()
print("\nAfter pop (removed last element):")
print(languages)
print("Popped language:", popped_language)

# Remove a language by value
languages.remove("German")
print("\nAfter removing 'German' by value:")
print(languages)

# Temporary alphabetical sorting
print("\nSorted (temporary alphabetical):")
print(sorted(languages))

# Show list is unchanged
print("List after sorted():")
print(languages)

# Temporary reverse alphabetical sorting
print("\nSorted (temporary reverse alphabetical):")
print(sorted(languages, reverse=True))

# Reverse the list in place
languages.reverse()
print("\nAfter reverse() (in place):")
print(languages)

# Reverse again to restore original
languages.reverse()
print("\nAfter reverse() again (restored):")
print(languages)

# Sort the list permanently in alphabetical order
languages.sort()
print("\nAfter sort() in alphabetical order:")
print(languages)

# Sort the list permanently in reverse alphabetical order
languages.sort(reverse=True)
print("\nAfter sort(reverse=True) in reverse alphabetical order:")
print(languages)

# Use len() to show number of items
print("\nNumber of languages in the list:", len(languages))


# 3-11. Intentional Error: If you haven’t received an index error in one of your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.

cities = ["Nnewi", "Ihiala", "Enugwu-ukwu", "Nnobi"]
# print(f"Test Error: {cities[4]}")
print(f"Test Error: {cities[-1]}")