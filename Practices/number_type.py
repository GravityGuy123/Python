# import math
# import random as r

# num1 = math.sqrt(4)
# num2 = math.ceil(4.4)
# num3 = math.ceil(4.5)  # Ceil() rounds up to the largest integer e.g 4.5, 4.1 etc will log 5
# num4 = math.floor(4.5)  # Floor() rounds down to the lowest integer e.g 4.5 will log 4
# num5 = math.cbrt(4)
# print(f"Suare Root: {num1}")
# print(f"Ceil: {num2}")
# print(f"Ceil 2nd: {num3}")
# print(f"Floor: {num4}")
# print(f"Cube Root: {num4}")

# print(r.random() * 10)

# dice1 = r.randint(1, 6)
# dice2 = r.randint(1, 6)
# print(f"{dice1} : {dice2}")


# Every file is a module and you shouldn't create a file with the name of an existing module, function or keyword
# When importing a module, ensure you import the specific module you need. e.g you need to use the math.floor and or math.ceil in that particular file. You should only import the two as done below:

# from math import ceil # if you only need ceil in that file and
# from math import floor, sqrt  # if you only need floor and sqrt in that file

# from main import exponent
# print(exponent(3, 2))


def exponent(param: int, index: int) -> float:
    return param**index
print(2.1, 5.3)
