from printing_functions import print_models, show_completed_models
import pizza
from func import greet_person
import pizza as p
from func import greet_person as gp

# Try It Yourself
# 8.1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.
# 8.2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.


# 8.1. Message:
def display_message():
    """Displays a simple message"""
    print("Am learning Python Functions")


display_message()


# 8.2. Favorite Book:
def favorite_book(title):
    """Displays a favorite book"""
    print(f'\nOne of my favorite books is "{title}"')


favorite_book("Married to the devils son")


# Try It Yourself
# 8.3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
# 8.4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
# 8.5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

# 8.3. T-Shirt:
def make_shirt(size, message):
    """ Return a made shirt. """
    print(f"\nA {size} sized shirt")
    print(f"Made a {size} sized {message}")


make_shirt("large", "blue shirt")


# 8-4. Large Shirts:
def make_shirt(size="large", message="I love Python."):
    """ Return a large made shirt. """
    print(f"\nA {size} sized shirt")
    print(f"Made a {size} sized {message}")

make_shirt()
make_shirt(size="medium")
make_shirt("small", "red shirt")


# 8.5. Cities:
def describe_city(city_name, country='Nigeria'):
    """ Return a city and country. """
    print(f'\n{city_name.title()} is a city in {country.title()}')

describe_city('nnewi', 'nigeria')
describe_city('miami', 'america')
describe_city('queensland', 'australia')


# Try It Yourself
# 8.6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile" Call your function with at least three city-country pairs, and print the values that are returned.
# 8.7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.
# 8.8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.


# 8.6. City Names:
def city_country(city, country):
    """Return a place, neatly formatted."""
    place = f"\n{city} {country}"
    return place.title()


location1 = city_country("new york", "america")
print(location1)

location2 = city_country("shanhai", "china")
print(location2)

location3 = city_country("lagos", "nigeria")
print(location3)


# 8.7. Album:
def make_album(artist_name, album_title, number_of_songs=None):
    """Return a dictionary of information about an album"""
    album = {"artist_name": artist_name, "album_title": album_title}
    print("\n")

    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    return album


music = make_album("akon", "escape", 3)
print(music)

music = make_album("sia", "drunk text")
print(music)

music = make_album("sia", "suitcase", 5)
print(music)


# 8.8. User Albums:
def make_album(artist_name, album_title, number_of_songs=None):
    """Return a dictionary of information about an album"""
    album = {"artist_name": artist_name, "album_title": album_title}
    print("\n")

    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    return album


while True:
    artist = input("\nPlease choose an artist: ")
    album = input("Please select an album: ")
    contd = input("Would you like to go again? (yes / no) ")

    if contd.lower() == "no":
        music = make_album(artist, album)
        print(f"{music} is a nice album")
        break

    music = make_album(artist, album)
    print(f"{music} is a nice album")


# Try It Yourself
# 8.9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
# 8.10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.
# 8.11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

# 8.9. Messages:
text_messages = [
    "Hey, how are you?",
    "Don't forget our meeting at 10!",
    "Can you send me the file?",
    "Lunch break?",
    "I'll call you in 5 minutes.",
    "Great job on the project!",
    "See you tomorrow!",
    "Just arrived, where are you?",
    "Good morning ☀️",
    "Let’s catch up later!",
]

def show_messages(messages):
    """Print a list of text messages"""

    for message in messages:
        print("\n", message)


show_messages(text_messages)


# 8.10. Sending Messages:
def send_messages(unprinted, sent):
    """Print and send a list of text messages"""

    while unprinted:
        print("\n")
        current_message = unprinted.pop(0)
        print(current_message)
        sent.append(current_message)


messages = [
    "Hey, how are you?",
    "Don't forget our meeting at 10!",
    "Can you send me the file?",
    "Lunch break?",
    "I'll call you in 5 minutes.",
    "Great job on the project!",
    "See you tomorrow!",
    "Just arrived, where are you?",
    "Good morning ☀️",
    "Let’s catch up later!",
]
sent_messages = []

send_messages(messages, sent_messages)

print(f"\nMessages {messages}")
print(f"\nSent Messages {sent_messages}")


# 8.11. Archived Messages:
def send_messages(unprinted, sent):
    """Print and send a list of text messages"""

    while unprinted:
        print("\n")
        current_message = unprinted.pop(0)
        print(current_message)
        sent.append(current_message)


sent_messages = []

send_messages(text_messages[:], sent_messages)

print(f"\nText Messages {text_messages}")
print(f"\nSent Messages {sent_messages}")


# Try It Yourself
# 8.12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.
# 8.13. User Profile: Start with a copy of user_profile.py from page 149. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
# 8.14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly.


# 8.12. Sandwiches:
def make_sandwich(*toppings):
    """Print a tuple of sandwich toppings"""
    print("\nMaking a sandwich with the following toppings")

    for topping in toppings:
        print(topping)


make_sandwich("lettuce")
make_sandwich("tomato", "cucumber", "pickles", "onions")
make_sandwich("bell peppers", "spinach", "avocado")


# 8.13. User Profile:
def build_profile(first, last, **user_info):
    """Build a person's profile with the provided information"""
    user_info["first_name"] = first
    user_info["last_name"] = last

    return user_info


user_info = build_profile("Gravity", "guy", state="Anambra", country="Nigeria")
print(user_info)


# 8.14. Cars:
def make_car(manufacturer, model, **car_info):
    """Build car profile with provided information"""
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model

    return car_info


car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)


# 8.15. Printing Models:


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# 8.16. Imports:
# 8.16a.
pizza.make_pizza(11, "pepperoni", "onions", "cabbage")

# 8.16b.
greet_person("gravity")

# 8.16c.
p.make_pizza(11, "sauce", "bell peppers", "beef")

# 8.16d.
gp("clara")


# 8.17. Styling Functions:
print("Done")
