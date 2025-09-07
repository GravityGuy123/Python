# Importing on the same line
# import datetime as d, json, ppprint, time

import datetime as d
import time
import json


# Python to json strings
profile = {
    "name": "GravityGuy",
    # "hobby": "Programming",
    "hobbies": ["Programming", "Gaming", "Reading"],
    "created_at": d.datetime.now().isoformat(),
}

# Write to a json file
# with open("profile.json", "w") as f:
#     json.dump(profile, f)

# Using try and except to handle errors
try:
    with open("profile.json", "r") as f:
        profile = json.load(f)
        print(profile)
except IOError as e:
    print("File not found", e)
except json.JSONDecodeError as j:
    print("Error decoding JSON", j)
except Exception as ex:
    print("An unexpected error occurred:", ex)

# time.sleep(2)

# try:
#     with open("profile.json", "w") as f:
#         json.dump(profile, f, indent=4)
# except IOError as e:
#     print("File not found", e)
# # Read from a json file
    

# NB: If you are converting to json, it's called Serialization and if you are converting back to python or any other language, it's called Deserialization.
# If you are building for a local audience, use UTC and if you are building for local audience, use local

# windows + : or windows + . to get emojis and special characters


# Assignment
# Do age calculation using datetime module. Pass in a string.
# Practice page 11 and best practices of the book
# Find a question minimum of 2 and practice due tomorrow