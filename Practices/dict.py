# # A Simple Dictionary
# alien_0 = {"color": "green", "points": 5}
# alien_1 = {"color": "blue", "points": 10}
# alien_2 = {"color": "red", "points": 20}

# print(alien_0)
# print(f"Alien 0 Color: {alien_0["color"]}")
# print(f"Alien 0 Points: {alien_0["points"]}")
# print(f"Alien 2 Color: {alien_2["color"]}")
# print(f"Alien 2 Points: {alien_2["points"]}")

# new_points = alien_1['points']
# print(f'\nYou just earned {new_points} points')
# print(f'New Points Type: {type(new_points)}')


# # Adding info to dictionaries
# alien_4 = {"color": "black", "points": 25}
# print(f"Alien 4: {alien_4}")

# alien_4["x_position"] = 0
# alien_4["y_position"] = 25

# print(f"Alien 4: {alien_4}")


# # Starting with an Empty Dictionary
# alien_4 = {}
# alien_4["color"] = "purple"
# alien_4["points"] = 15

# print(f"Alien 4: {alien_4}")


# # Modifying Values in a Dictionary
# alien_4 = {'color': 'blue'}
# print(f"\nThe alien is {alien_4['color']} in color")

# alien_4['color'] = 'red'
# print(f"\nThe alien is now {alien_4['color']} in color")

# alien_4 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

# if alien_4['speed'] == 'slow':
#     x_increment = 1
# elif alien_4['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a fast Alien
#     x_increment = 5

# # The new position is the old position plus the increment.
# alien_4['x_position'] = alien_4['x_position'] + x_increment

# print(f"New X Position: {alien_4['x_position']}")

# alien_4['speed'] = 'fast'

# # Removing Key-Value Pairs
# alien_4 = {'color': 'green', 'points': 5}
# del alien_4['points']
# del alien_4['color']
# print(alien_4)


# # A Dictionary of Similar Objects
# favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python",}

# print(f"Edward: {favorite_languages['edward']}")
# edward_language = favorite_languages["edward"].title()
# print(edward_language)

# # Using get() to Access Values
# print(alien_4['points'])

# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned')
# print(point_value)


# # Looping Through a Dictionary
# # Looping Through All Key-Value Pairs
# user_1 = {'username': 'dev_demon', 'first': 'dev', 'last': 'demon'}

# for key, value in user_1.items():
#     # print(f"{key}: {value}")
#     print(f"\nKey: {key}")
#     print(f"\nValue: {value}")

# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }

# for name, language in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite laguage is {language.title()}")


# # Looping Through All the Keys in a Dictionary
# for name in favorite_languages.keys():
#     print(f"\n{name.upper()}")

# index = 0
# for name in favorite_languages:
#     index = index +1
#     print(f'Name {index}: {name}')

# favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python',}

# friends = ["phil", "sarah"]

# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}")


# # for name, language in favorite_languages.items():
# #     print(name.title())

# #     if name in friends:
# #         print(f"\t{name.title()}, I see you love {language}")

# if 'erin' not in favorite_languages.keys():
#     print("Erin pls take a poll!")


# Looping Through a Dictionary’s Keys in a Particular Order
# favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python", "kyle": "javascript", "dani": "php"}

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll")


# # Looping Through All Values in a Dictionary
# favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python", "kyle": "javascript", "dani": "php"}

# for language in sorted(favorite_languages.values()):
#     print(language.title())
# This sorts the values in alphabetical order

# # To see each value choosen without repitition, we can use a set (a collection in which each item must be unique).
# for language in sorted(set(favorite_languages.values())):
#     print(f"\n{language.upper()}")

# for language in set(favorite_languages.values()):
#     print(f"\n{language.upper()}")


# # Nesting
# alien_0 = {"color": "green", "points": 5}
# alien_1 = {"color": "yellow", "points": 10}
# alien_2 = {"color": "red", "points": 15}
# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# # Make an empty list for storing aliens.
# aliens = []

# # Make 30 green aliens.
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# # print(aliens)
# for alien in aliens[:5]:
#     print(alien)

# # Show how many aliens have been created.
# print(f"Total number of aliens: {len(aliens)}")

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['point'] = '10'

# print(f'\nAliens : {aliens[:5]}')
# # the first 3 elements color, speed and point have been changed

# # A List in a Dictionary
# pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
# # summarize the order
# print(f'You ordered a {pizza['crust']}-crust pizza with the following toppings')
# for topping in pizza['toppings']:
#     print('\t'+ topping)


# favorite_languages = {
#     "jen": ["python", "ruby"],
#     "sarah": ["c"],
#     "edward": ["ruby", "go"],
#     "phil": ["python", "haskell"],
# }

# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     # print(languages)
#     for language in languages:
#         print(language)

# # A Dictionary in a Dictionary
# users = {
#     "aeinstein": {"first": "albert", "last": "einstein", "location": "princeton",},
#     "mcurie": {"first": "marie", "last": "curie", "location": "paris",},
# }

# for username, user_info in users.items():
#     print(f'\nUsername: {username}')
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']

#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")


# person1 = {"first_name": "gravity", "last_name": "guy", "age": 25, "city": "nnewi"}
# person2 = {"first_name": "edu", "last_name": "crypt", "age": 27, "city": "nsukka"}
# person3 = {"first_name": "feisty", "last_name": "paragon", "age": 24, "city": "nnewi"}
# people = [person1, person2, person3]

# for info in people:
#     full_name = f"{info['first_name']} {info['last_name']}"
#     age = f"{info['age']}"
#     city = f"{info['city']}"

#     print(f"{full_name.title()} is {age} years old and is from {city}")


# pet1 = {"name": "dog", "kind": "mammal", "owners_name": "mike"}
# pet2 = {"name": "shark", "kind": "fish", "owners_name": "mike"}
# pet3 = {"name": "crocodile", "kind": "reptile", "owners_name": "mike"}
# pet4 = {"name": "puppy", "kind": "mammal", "owners_name": "mike"}
# pet5 = {"name": "parrot", "kind": "bird", "owners_name": "mike"}

# pets = [pet1, pet2, pet3, pet4, pet5]

# for pet in pets:
#     pet_info = f"A {pet['name']} is a {pet['kind']} and the owner's name is {pet['owners_name']}."
#     print(pet_info)


# favorite_places = {
#     "simon": {"african": "dubai", "western": "america", "asian": "china"},
#     "mirabel": {"african": "seicheles", "western": "canada", "asian": "thailand"},
#     "clara": {"african": "kenya", "western": "france", "asian": "singapore"},
# }

# for person, places in favorite_places.items():
#     print(f"\n{person.title()}'s favorite places are: ")
#     for key, place in places.items():
#         print(f"{key.title()}: {place.title()}")


# friends = {
#     "mikey": {"1st": 3, "2nd": 1},
#     "clara": {"1st": 7, "2nd": 4},
#     "ann": {"1st": 1, "2nd": 9},
#     "chiagozie": {"1st": 4, "2nd": 2},
#     "mmesoma": {"1st": 6, "2nd": 2},
# }

# for friend, numbers in friends.items():
#     print(f"\n{friend.title()}'s favorite numbers are:")
#     for key, number in numbers.items():
#         print(f"{key}: {number}")


# for friend, numbers in friends.items():
#     print(f"{friend.title()}'s favorite numbers are:")
#     print(f"1st: {numbers['1st']}, 2nd: {numbers['2nd']}\n")


# cities = {
#     "lagos": {
#         "country": "nigeria",
#         "population": 14000000,
#         "fact": "largest city in africa",
#     },
#     "abuja": {
#         "country": "nigeria",
#         "population": 3000000,
#         "fact": "capital city of nigeria",
#     },
#     "paris": {
#         "country": "france",
#         "population": 11000000,
#         "fact": "city of love",
#     },
# }

# # for city, info in cities.items():
# #     print(
# #         f"\n{city.title()} is in {info['country'].title()}, with a population of {info['population']} and is known to be the {info['fact']}"
# #     )

# for city, info in cities.items():
#     print(
#         f"\n{city.title()} is in {info['country'].title()}, "
#         f"has a population of {info['population']:,} "
#         f"and is known for being the {info['fact'].title()}."
#     )
