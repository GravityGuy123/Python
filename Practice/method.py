# num = 3

# print(type(num))
# print(type([]))

# Getting the Length for the value of a variable 
# name = "DevHunter"
# print(len(name)) # This prints the length which is 9

# Using escape character


# using Multi Line Strings
# sentence = "My name is is GravityGuy.\
#     I am  a Web Dev Student\
#         and am currently learnig Python.\
#             It is an exciting Programming Language."
# print(sentence)

# The indentation is recommended but not important in the sense that the code works with or without it.


# # Concatenating a string
# string1 = "Gravity"
# string2 = "Guy"
# result = string1 + string2
# print(result)

# st1 = "Dev"
# st2 = "Hunter"
# result = f"{st1}{st2}"
# print(result)


# # Formatting in multiple lines
# s1 = "Dev"
# s2 = "Diva"
# s3 = "at ur service"
# result = f"""
# {s1}
# {s2}
# {s3}
# """
# print(result)


# Index and slicing
string1 = "GravityGuy"
# print(string1[0]) # When one value is used, it gets the character at that index

# print(string1[0:])  # In this case, it gets the characters from index 0 to the end

# print(string1[10:]) # When the index indicated exceeds the available index, you get an empty space i.e nothing

# print(string1[:6]) # In this case, the end point was indicated to be 6 but we didn't indicate the start point, what it does is to start from the 1st index to the indicated end point


# print(string1[::2]) 
# In this case, we didn't declare the first two ":", Because we didn't declare the first ":" which is meant to indicate the starting point by default it tells the code to start slicing from the first value. The second ":" which is meant to indicate the end point by default it tells the code to end slicing at the last value. Finally, the 2 which is the 3rd value it takes is telling the code to count 1 index and start at the 2nd.

# NB: Strings are immutable, meaning they cannot be changed after they are created. However, you can create a new string based on the original one with modifications.


# Raw String



paragraph = "My name is GravityGuy. I am a web dev student and am currently learning python.\n"

# \n is used to add a new line

# print(paragraph.lower())
# print(paragraph.upper())
# print(paragraph.title())



# Using strip method to remove spaces
# Tracks the space on the left and right side of your string
# my_name = " GravityGuy "
# print(f"Has Space: {my_name}") 
# print(f"Spaceless: {my_name.strip()}")


# # Removing left space with lstrip
# print(f"LeftSpace: {my_name.lstrip()}")

# # Removing right space with rstrip
# print(f"RightSpac: {my_name.rstrip()}")


# Using Replace method to replace a string
# my_name = "G r a v i t y G u y"
# print(my_name.replace(" ", "")) # This removes all the space because, the first value is what you are targeting and the second is what you are replacing it with.




# Methods
# my_name.isdigit()
# my_name.isdecimal()
# my_name.isalnum()
# my_name.isalnum()
# my_name.isalpha()
# my_name.isascii()
# my_name.islower()
# my_name.isupper()
# my_name.isnumeric()
# my_name.istitle()
# my_name.isspace()
# my_name.startswith("f")
# my_name.endswith("e") # Both .startswith and .endswith is case sensitive


# temperature = input("What is the temperature in Celsius ")
# if type (temperature) is int or type (temperature) is float:
#     fahrenheit = ((temperature * (9 / 5)) + 32)
#     print(f"The temperature is {fahrenheit}°F")
# else:
#     temperature = int(temperature)
#     fahrenheit = ((temperature * (9 / 5)) + 32)
#     print(f"The temperature is {fahrenheit}°F")


# temperature = input("What is the temperature in Celsius? ")
# if temperature.isdigit():
#     temperature = int(temperature)
#     fahrenheit = (temperature * (9 / 5)) + 32
#     print(f"The temperature is {fahrenheit}°F")
# else:
#     try:
#         temperature = float(temperature)
#         fahrenheit = (temperature * (9 / 5)) + 32
#         print(f"The temperature is {fahrenheit}°F")
#     except ValueError:
#         print("Invalid input. Please enter a number.")


# user_email = input("Enter your email address: ")
# if user_email.count("@") == 1:
#     before_at = user_email.index("@")
#     after_at = user_email[before_at + 1 :]
#     if "." in after_at:
#         if after_at.count(".") == 1:
#             print("Valid Credentials")
#         else:
#             print("You are expected to have only one '.' after '@'.")
#     else:
#         print("There must be at least one '.' after '@'")
# else:
#     print("Invalid Credentials, there must be exactly one '@'.")









# Setup Python Profile