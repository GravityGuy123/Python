# Try It Yourself
# 4.1a. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# 4.1b. Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
# 4.1c. Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
# 4.2a. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# 4.2b. Modify your program to print a statement about each animal, such as A dog would make a great pet.
# 4.2c. Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would make a great pet!

# 4.1a. Pizzas:
pizzas = ["chicken", "pepperoni", "hawaiian", "margheritta"]
for pizza in pizzas:
    print(pizza)

# 4.1b.
    print(f"\n I love {pizza} pizza \n")
print("I love chicken pizza so much")
print("I love pepperoni pizza so much")
print("I love hawaiian pizza so much")
print("I love margheritta pizza so much")
print("I realy love pizza")

# 4.2a. Animals
animals = ["hen", "hawk", "duck", "parrot"]
for animal in animals:
    print(f"\n{animal}")

# 4.2b.
    print(f"A {animal} will make a great pet.")
print("These are birds")


# Try It Yourself
# 4.3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
# 4.4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
# 4.5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
# 4.6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
# 4.7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
# 4.8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
# 4.9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

# # 4.3. Counting to Twenty:
# for count in range(1, 20 + 1):
#     print(count)

# 4.4. One Million:
million = list(range(1, 1_000_000 + 1))
# for count in million:
#     print(f"Counting: {count}")

# 4.5. Summing a Million:

numbers = list(range(1, 1_000_001))
print(f"Numbers: {sum(numbers)}")

# 4.6. Odd Numbers:
odd_numbers = list(range(1, 20 + 1, 2))
for odd_number in odd_numbers:
    print(f"Odd Number: {odd_number}")

# 4.7. Threes:
print("\n")
threes = [value * 3 for value in range(3, 30 + 1)]
for three in threes:
    print(f"Three: {three}")

# 4.8. Cube:
print("\n")
cubes = []
for cube in range(1, 10 + 1):
    cube = cube ** 3
    cubes.append(cube)
    print(f"Cubes: {cube}")

# # 4.9. Cube Comprehension:
print("\n")
cubes = [value ** 3 for value in range(1, 10 + 1)]
for cube in cubes:
    print(f"Cubes Comp: {cube}")


# Try It Yourself
# 4.10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# 4.10a. Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# 4.10b. Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
# 4.10c. Print the message The last three items in the list are:. Use a slice to print the last three items in the list.
# 4.11a. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# 4.11b. Add a new pizza to the original list.
# 4.11c. Add a different pizza to the list friend_pizzas.
# 4.11d. Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
# 4.12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

# 4.10. Slices
pizzas = ["chicken", "pepperoni", "hawaiian", "margheritta", "veggies"]

# 4.10a
print("\nFirst 3 items are:")
print(pizzas[:3])

# 4.10b
print("\nThree items from the middle of the list:")
print(pizzas[1:4])

# 4.10c
print("\nLast 3 items are:")
print(pizzas[2:])

# 4.11a. My pizzas, Your pizzas
friend_pizzas = pizzas[:]

# 4.11b.
friend_pizzas.append("tacko")

# 4.11c.
friend_pizzas.append("mushroom")

# 4.11d.
print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4.12. More Loops


# Try It Yourself
# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the change.
# • The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

# 4.13a
foods = ('rice', 'beans', 'moi moi', 'noodles', 'yam')

# 4.13b
print("\n")
for food in foods:
    print(food)

# 4.13c
# food[1] = 'pasta'

# 4.13d
foods = ("rice", "abacha", "moi moi", "noodles", "egwusi soup")
print("\nModified Menu")
for food in foods:
    print(food)


# Try It Yourself
# 4.14. PEP 8: Look through the original PEP 8 style guide at https://python.org/ dev/peps/pep-0008/. You won’t use much of it now, but it might be interesting to skim through it.
# 4.15a. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8:
# 4.15b. Use four spaces for each indentation level. Set your text editor to insert four spaces every time you press tab, if you haven’t already done so (see Appendix B for instructions on how to do this).
# 4.15c. Use less than 80 characters on each line, and set your editor to show a vertical guideline at the 80th character position.
# 4.15d. Don’t use blank lines excessively in your program files

# 4.14.
print("done")

# 4.15a.
print("All pre written codes follow the afore mentions PEP 8 guidlines")

# 4.15b.
print("Done")

# 4.15c.
print("Done")

# 4.15d.
print("Done")