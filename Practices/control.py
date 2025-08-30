# condition1 = 5
# condition2 = 0

# # Using Truthy Values. 
# if condition1:
#     print(f"{condition1} is True")
# else:
#     print(f"{condition1} is False")

# # Using Falsy Values. 
# if condition2:
#     print(f"{condition2} is True")
# else:
#     print(f"{condition2} is False")

# In python, numbers are truthy in the sense that if you use a variable with a  value whose data type is number and then use it as a condition without stating anything for the condition. It will evaluate to be true as it is above.

# String is true if it has a value and false if it is empty. I.e if it has up to one character, it is true. If it has no character, it is false.

# pow() is used to raise a number to the power of another number



# if 3 > 5:
#     print("Greater than")
# elif 3 < 5:
#     print("Less than")
# else:
#     print("Unrecognized")


# Boolean operators if, elif, else, or, and, not etc

age = input("Enter your age: ")
if not age:
    print("No value entered")
else:
    age = int(age)
    if age > 19:
        print("Adult")
    elif age > 18 and age < 20:
        print("Adult Teenager")
    elif age >= 10 and age < 18:
        print("Teenager")
    else:
        print("Too young")


if age < 18 or age > 60:
    print("Dependats")
else:
    print("Your part of the labour force")










# Truth values


# PEMDAS
# P - Paranthesis
# E - Exponent
# M - Multiplication
# D - Division
# A - Addition
# S - Subtraction