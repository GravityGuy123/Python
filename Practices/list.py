fruits = [
    "apple",
    "banana",
    "carrot",
    "dates",
    "elderberry"
]

# Iterable
# print(fruits)

# for f in fruits:
#     print(f)

# for i in range(5):
#     print(i)

length = len(fruits)
for lf in range(length):
    print(fruits[lf])


# # Lists
# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick")
# # print("Thank you everyone, that was a great magic show!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")

# # Making Numerical Lists
# # Giving the range function one value makes that value the stop point as in this case 5. Added 1 to it be make it stop at 5 itself considering that range stops an index less.
# for value in range(5 + 1):
#     print(value)

# for v in range(5): # This stops at 4
#     print(v)

# # Giving the range function two values makes the 1st the start and 2nd the stop point (of course an index less which is where the plus 1 is useful unless you make the stop an index more).
# for x in range(1, 6): # stops at 5 replacing the use of +1
#     print(x)
# # Using +1 is much more recommended than making your stop an index higher


# # Using range() to Make a List of Numbers
# numbers = list(range(1, 5 + 1))
# print(f"Numbers: {numbers}\n")

# # Giving the range function three (3) value makes the 1st the Start, 2nd the Stop and 3rd the Step at which it moves
# even_numbers = list(range(2, 10 + 1, 2))
# print(f"Even Numbers: {even_numbers}")

# squares = []
# for value in range(1, 10 + 1):
#     square = value ** 2
#     squares.append(square)
# print(f"Squares: {squares} \n")

# de_squares = []
# for v in range(3, 11):
#     de_square = v ** 3
#     de_squares.append(de_square)
# print(f"De Squares: {de_squares}")

# # Checking for the minimum and maximum values with min() and max() functions
# print(f"Minimum Value: {min(de_squares)}")
# print(f"Maximum Value: {max(squares)}")


# # List Comprehention
# even_numbers = list(range(2, 10 + 1, 2))
# print(even_numbers)

# squares = [value ** 2 for value in range(1, 10 + 1)]
# print(f"Squares: {squares}")


# sum_to_a_million = list(range(1, 1_000_000 + 1))
# for sum in sum_to_a_million:
#     sum + 2
#     # print(sum)

# sum_to_a_million = [value + 2 for value in range(1, 1_000_000)]
# # print(sum_to_a_million)

# for cube in range(1, 10 + 1):
#     cube = cube**3
#     print(cube)


# # Slicing a List
# players = ["charles", "martina", "michael", "florence", "eli"]
# print(f'Original: {players}')
# print(f'First 3: {players[0:3]}')
# print(f'2nd to 4th: {players[1:4]}')

# # Not specifying the start index makes it start from the begining of the list
# print(f"First 4: {players[:4]}")

# # Not specifying the stop index makes it stop at the end of the list.
# # In this case from 3rd index to last
# print(f"3rd to last: {players[2:]}")

# players = ["charles", "martina", "michael", "florence", "eli"]
# for player in players[1:]:
#     print(player.title())

# for player in players[:4]:
#     print(player.upper())

# # Slicing the entire list
#     print(player[:]) # Prints the entire list from beginning to end


# # Copying a List
# my_foods = ['pizza', 'burger', 'chips', 'carrot cake']
# friend_foods = my_foods[:]
# print(f"My favorite foods are: {my_foods}")
# print(f"My friends favorite foods are: {friend_foods}")

# print("\n")

# my_foods.append("ice cream")
# friend_foods.append("veggies")
# print(f"Mine 2: {my_foods}")
# print(f"Friend's 2: {friend_foods}")


# # Tuples
# # Tuples allows you to create a list of items that cannot change
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# # Items in a Tuple can't be changed or modified and would throw an error if we try to. You also can't assign to a Tuple unless you create a variable with the same name.
# dimensions[0] = 350
# dimensions.append(2)
# dimensions = (350, 50) # re-assigning a variable is valid in python
# print(dimensions)

# # If you want to define a tuple with one element, you need to include a trailing comma:
# my_t = (3,)

dimensions = (10, 3, 7, 1)
for dimension in dimensions:
    print(f"Original: {dimension}")

print("\n")
dimensions = (4, 1, 5, 9, 3)
for dimension in dimensions:
    print(f"Modified: {dimension}")

print("\n")
my_tuple = tuple(range(1, 11, 2))
print(f"Tuple: {my_tuple}")