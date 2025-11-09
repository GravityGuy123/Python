# Try It Yourself
# 6.1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
# 6.2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

# 6.1. Person:
person = {'first_name': 'gravity', 'last_name': 'guy', 'age': 25, 'city': 'nnewi'}
print(f"Person First Name: {person['first_name']}")
print(f"Person Last Name: {person['last_name']}")
print(f"Person Age: {person['age']}")
print(f"Person City: {person['city']}")

# 6.2. Favorite Numbers:
friends = {'mikey': 3, 'clara': 7, 'ann': 1, 'chiagozie': 4, 'mmesoma': 6}
print(f"\nMikey fav Num: {friends['mikey']}")
print(f"Clara fav Num: {friends['clara']}")
print(f"Ann fav Num: {friends['ann']}")
print(f"Chiagozie fav Num: {friends['chiagozie']}")
print(f"Mmesoma fav Num: {friends['mmesoma']}")

# for friend in friends:
#     print(f"\n{friend.title()} Fav Num: {friends[friend]}")

# 6.3. Glossary:
# 6.3a.
glossary = {
    "key": "identifier",
    "value": "item",
    "tuple": "immutable list",
    "append": "add to end",
    "pop": "remove from end",
}

# 6.3b.
print(f"\nkey: {glossary['key']}")
print(f"\nvalue: {glossary['value']}")
print(f"\ntuple: {glossary['tuple']}")
print(f"\nappend: {glossary['append']}")
print(f"\npop: {glossary['pop']}")


# Try It Yourself
# 6.4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.
# 6.5a. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# 6.5b. Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# 6.5c. Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.
# 6.6a. Polling: Use the code in favorite_languages.py (page 97).
# 6.6b. Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
# 6.6c. Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

# 6.4.
glossary = {
    "key": "identifier",
    "value": "item",
    "tuple": "immutable list",
    "append": "add to end",
    "pop": "remove from end",
}
for key, value in glossary.items():
    print(f"\n{key.title()}: {value.title()}\n")

# 6.5a. Rivers:
rivers = {"nile": "egypt", "amazon": "brazil", "yangtze": "china"}

# 6.5b.
for river, country in rivers.items():
    print(f"River {river.title()} runs through {country.title()}")

# 6.5c.
print("\n")
for river in rivers.keys():
    print(river.title())

# 6.5d.
print("\n")
for country in rivers.values():
    print(country.title())

# 6.6a.
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python',}

# 6.6b.
persons = ['kyle', 'dani', 'sarah', 'eve', 'phil']

# 6.6c.
print('\n')
for person in persons:
    if person in favorite_languages.keys():
        print(f'Thanks {person.title()} for responding.')
    else:
        print(f'{person.title()}, you are invited to take a poll.')


# Try It Yourself
# 6.7. People: Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
# 6.8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
# 6.9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.
# 6.10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.
# 6.11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
# 6.12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.


# 6.7. People:
person1 = {"first_name": "gravity", "last_name": "guy", "age": 25, "city": "nnewi"}
person2 = {"first_name": "edu", "last_name": "crypt", "age": 27, "city": "nsukka"}
person3 = {"first_name": "feisty", "last_name": "paragon", "age": 24, "city": "nnewi"}
people = [person1, person2, person3]

for info in people:
    full_name = f"{info['first_name']} {info['last_name']}"
    age = f"{info['age']}"
    city = f"{info['city']}"

    print(f"{full_name.title()} is {age} years old and is from {city}")


# 6.8. Pets:
pet1 = {'name': 'dog', 'kind': 'mammal', 'owners_name': 'mike'}
pet2 = {"name": "goldfish", "kind": "fish", "owners_name": "evie"}
pet3 = {"name": "butterfly", "kind": "insects", "owners_name": "rex"}
pet4 = {'name': 'puppy', 'kind': 'mammal', 'owners_name': 'sarah'}
pet5 = {"name": "parrot", "kind": "bird", "owners_name": "mike"}

pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    pet_info = f"A {pet['name'].title()} is a {pet['kind']} and the owner's name is {pet['owners_name'].title()}."
    print(pet_info)


# 6.9. Favorite Places:
favorite_places = {
    "simon": {"african": "dubai", "western": "america", "asian": "china"},
    "mirabel": {"african": "seicheles", "western": "canada", "asian": "thailand"},
    "clara": {"african": "kenya", "western": "france", "asian": "singapore"},
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are: ")
    for key, place in places.items():
        print(f"{key.title()}: {place.title()}")

# 6.10. Favorite Numbers:
friends = {
    "mikey": {'1st': 3, '2nd': 1},
    "clara": {'1st': 7, '2nd': 4},
    "ann": {'1st': 1, '2nd': 9},
    "chiagozie": {'1st': 4, '2nd': 2},
    "mmesoma": {'1st': 6, '2nd': 2}
}

for friend, numbers in friends.items():
    print(f"\n{friend.title()}'s favorite numbers are:")
    for key, number in numbers.items():
        print(f"{key}: {number}")


# for friend, numbers in friends.items():
#     print(f"{friend.title()}'s favorite numbers are:")
#     print(f"1st: {numbers['1st']}, 2nd: {numbers['2nd']}\n")


# 6.11. Cities:
cities = {
    "lagos": {
        "country": "nigeria",
        "population": 14000000,
        "fact": "largest city in africa",
    },
    "abuja": {
        "country": "nigeria",
        "population": 3000000,
        "fact": "capital city of nigeria",
    },
    "paris": {
        "country": "france",
        "population": 11000000,
        "fact": "city of love",
    },
}

for city, info in cities.items():
    print(f"\n{city.title()} is in {info['country'].title()}, with a population of {info['population']} and is known to be the {info['fact']}")


# 6-12. Extensions:
for city, info in cities.items():
    print(
        f"\n{city.title()} is in {info['country'].title()}, "
        f"has a population of {info['population']:,} "
        f"and is known for being the {info['fact'].title()}."
    )
