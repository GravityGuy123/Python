# from function import fibonacci

# fibonacci


# Codes are organized in named spaces(folder). Everthing within the same name space can be imported and reused.
# Named Space (folder)

# # Declaring a function with docstring
# def fibonacci(num):
#     """ A function that returns a fib sequence
#     Args:
#       num(int): an integer
#     Returns:
#       list[int]:
#     """
#     result = []
#     a, b = 0, 1
#     while a < num:
#         result.append(a)
#         a, b = b, a + b
#         return result
# print(fibonacci(20))

# # Declaring a function without docstring
# def division(num, denom):
#   print(num / denom)

# division(4, 2)

# # Assigning default values to the parameter of functions
# def divide(a = 3, b = 1):
#    print(a / b)

# divide(9 / 3)

# The parameter of functions by defaults are positional in the sense that it take the actual placement like in the function above. The value 9 by default takes the position of a while the value 3 takes the position of b.
# But if you don't want to maintain the position of the argument, you can do it as done below.
# 

# def division(a, b):
#    print(a / b)

# division(b = 2 ,a = 4)

# def add(num1, num2, num3 = 25, num4 = 12):
#    print(num1 + num2 + num3 + num4)
# add(2, 3)


# When you don't know the number of arguments / paraneters that is going to be parsed.
# NB, it can be * + whatever you want but the most commonly used is *args

# print("Unknown number of arguments")
# def unknown(*args):
#   total = 0
#   for a in args:
#     total += a
#     print(total)

# unknown(2, 3, 4, 5, 6, 7, 9, 1)


# profile = {1: "Simon", 2: "Chisom", 3: "Ifenna", 4: "Chioma", 5: "Ashioma"}

# # printing  the keys
# for p in profile.keys():
#   print(f"Keys: {p}")

# # printing the values
# for v in profile.items():
#   print(f"Value: {v}")

# print(".............")

# # Accessing a particular value
# print(f"Value 1: {profile[1]}")


# fruits = ["apple" "banana", "cherry", "dates", "guava"]

# # Printing both index and value of a list
# for index, value in enumerate (fruits):
#   print(index, value)



# def make_sandwich():
#     print("Get 2 slices of bread")
#     print("Put peanut butter on one slice")
#     print("Put jelly on the other slice")
#     print("Put the slices together")
#     print("Enjoy your sandwich!")
    
# make_sandwich()


# # You use double astericks (**) if you want to use keyword argument
# def unknown(**ky):
#     for k in ky:
#       print(k)
#     return 34

# value  = unknown(name = "GravityGuy", hub = "Icehub", Proffession = "Programmer")
# print(value)
# # logs name hub Proffession 34

# def greet():
#    print("Hello", "Nice to meet you", "Have a nice day")
#    print("Nice to meet you")
#    print("Have a nice day")

# greet()

# def greet_person(name):
#     print("Hello, " + name + "!")
#     print("Nice to meet you!")
#     print("Have a great day!")

# greet_person("Mike")
# greet_person("Kings")
# greet_person("Alice")
# greet_person("Bob")
# greet_person("Charlie")


# def introduce(name, age):
#     print("Hi, am " + name + " and am " + str(age) + " years old")
#     print(f"Hi, am {name} and am {age} years old")
# introduce("gravity", 15)

# # Using Exceptions
# def division(num, den):
#   print(num / den)
# division(6, 3)

# The above code works

# def division(nume, denom):
#    print(nume / denom)

#    if nume == 0 or denom == 0:
#       print("Not divisible")
#    else:
#     division(2, 0)

# def division(nume, denom):
    
#     if nume == 0 or denom == 0:
#         print("Not divisible (cannot divide by zero)")
#     else:
#         print(nume / denom)

# division(2, 0)
# division(9, 3)


# def divide(a, b):
#     try:
#         userInput = input("Input a denomination: ")
#         num = int(userInput)
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")
#         return
    


# # 
# def dev(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#     except TypeError:
#         print("Error: Invalid input type. Please provide numbers.")
#     else:
#         print(f"The result is: {result}")
#     finally:
#         print("Execution completed.")


# Performing division 
# while True:
#     userInput = input("Input a denomination: ")
#     try:
#         num = int(userInput)
#         break
#     except ValueError as v:
#         # print("Invalid input. Please enter a valid integer.")
#         print(f"Error Occured: -> {v}.")
#     except ZeroDivisionError as z:
#         print(f"Cannot divide by zero: -> {z}.")
#     except Exception as e: # Catching all other exceptions you might not have thought of.
#         print(f"Something went wrong: -> {e}.")
# print("Done")


def divide():
    userInput = input("Input a numerator: ")
    try:
        nume = int(userInput)
        denom = int(userInput)
        result = nume / denom
        print(f"The result is: {result}")
    except ValueError as v:
        print(f"Error Occured: -> {v}.")
    except ZeroDivisionError as z:
        print(f"Cannot divide by zero: -> {z}.")

print("Done")
    


# When ever you are using or accepting external data or input, always use exception handling to avoid breaking your code.