# num = 0

# while num <= 20:
#     print(num)
#     num += 5

# num2 = 20
# while num2 >= 0:
#     print(num2)
#     num2 -= 4


# n = 0
# while n <= 20:
#     print(n)
#     n += 5


# choice = input("Enter your choice: ")

# if choice == "1":
#     print("Hello there!")
# elif choice == "2":
#     print("Goodbye!")
# elif choice == "quit":
#     print("Thanks for using the program!")
# else:
#     print("Invalid choice. Please try again.")


# numbers = [1, 3, 5, 7, 9, 11]

# for n in numbers:
#     print(n)

# # Using Range() to iterate. range(stop)
# for r in range (5):
#     print(r)

# # Iterating from one point to another. range(start, stop)
# for y in range(5, 21):
#     print(y)


# # Iterating from one point to another. range(start, stop, step)
# for x in range(10, 110, 10):
#     print(x)

# for e in range(2, 11, 2):
#     print(e)


# Looping through words (str data type)

# # Looping from a variable
# code = "Python"
# for letter in code:
#     print(letter)

# program = "JavaScript"
# for pg in program:
#     print(pg)

# # Looping from a created string
# for h_s in "house":
#     print(h_s)

# for ct in "curtain":
#     print(ct)


# # Looping through an lists while printing the value with a concatenated string
# fruits = ['apple', 'banana', 'cherry', 'grape', 'guava']
# for fr in fruits:
#     print(f'I love {fr}')

# food = ['Okra soup', 'excessive veggies', 'nagging people', 'snubs']
# for fd in food:
#     print(f"I hate {fd}")




# fruit = ["apples", "oranges", "berries", "grapes", "papaya"]
# food = ['HTML', 'CSS', 'JavaScript', 'TypeScript', 'Python']

# for ut in fruit:
#     for oo in food:
#         print(f"I love {ut} and {oo}")

student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92}
# Loop through keys
for name in student_grades:
    print(name)

# Loop through values
for grade in student_grades.values():
    print(grade)

# Loop through key-value pairs
for name, grade in student_grades.items():
    print(f"{name}: {grade}")
