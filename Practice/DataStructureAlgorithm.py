# age = 4
# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# def add(num: int) -> int:
#     num = num + 2
#     return num

# def update_list(param: list[str]) -> list[str]:
#     param.append("dates")
#     return param

# print(add(age))
# print(age)

# update_list(fruits)
# print(fruits)








# empty_list = [] # Infered List
# print(type(empty_list)) # Explicit List



# empty_dict = {} # Infered dictionary
# empty_dict1 = dict() # Explicit dictionary
# print(type(empty_dict))
# print(type(empty_dict1))

# empty_set = set()
# empty_set = {None}
# print(type(empty_set))


# fruits = ["apple", "banana", "cherry"]

# def update_list(param: tuple) -> list[str]:
#     result = list(param)
#     result.append("dates")
#     return result

# print(update_list(tuple(fruits)))
# print(fruits)
# print(type(fruits), fruits)


# fruits = ["apple", "banana", "cherry", 3, 5, 9, 2, True, False, ["red", "blue"]]
# print(type(fruits), fruits)


# name = "Gravity"
# name_list = []
# for c in name:
#     name_list.append(c)

# print(name_list)
# list("")

# fruits = ["apple", "orange", "papaya", "mango"]
# fruits2 = ["grape", "cherry", "berry", "pea"]

# fruits.extend(fruits2)
# fruits.extend("Guava")
# print("Two lists:")
# print(fruits + fruits2)

# .append() # Adds one item to the end of a list, tuple etc.
# .insert() # Adds one item to the end of a list, tuple etc.
# .extend() # Adds two or more lists, dictionary etc together.
# .count() # counts the number of entry for a particular value.



# fruits = ["apple", "orange", "papaya", "mango", "apple", "orange", "papaya", "mango"]
# # index_of = fruits.index("papaya")
# index_of = fruits.index("papaya", 4)
# print(index_of)


# money = 1_000_000 # Most advisable method for writing monetary numbers
# print(money)

# # Removing the last value of a list with .pop()
# fruits.pop()

# # Removing a value at a particular index
# fruits.pop(1) # removes at index of 1

# # Sorting values in ascending order with .sort()
# fruits.sort()

# # Sorting values in decending order with .sort()
# fruits.sort(reverse=True) # or you sort and use .reverse()

# # Reversing the postion of values with .reverse()
# # The function (.reverse) basically reverses the position and places them from the last to the first
# fruits.reverse()


# num = [3, 1, 9, 45, 32, 12, 92, -43, -12, 0]

# def reverse_list(param: list[list]) -> list[int]:
#     l_p = len(param) -1
#     return param[l_p: 0: -1]

# print(reverse_list(num))


# def sort_ascending(param: list[int]) -> list[int]:
#     sort = len(param) +1
#     return param[sort: +1: 1]

# print(f"Final List: {sort_ascending(integers_list)}")


# import random as r

# nums = []
# for i in range(10 + 1):
#     nums.append(i)
#     print(nums)

# num1 = []
# for _ in range(13):
#     # r.randint(start, stop) # the first value is the start and 2nd is the stop.
#     num1.append(r.randint(-100, 100))

# print(num1)


# Looping  inside a list
list_int = [a for a in range(5)]
list_int2 = [a**3 for a in range(5)]
print(f"List 1: {list_int}")
print(f"List 2: {list_int2}")


# Looping directly
li = []
for q in range(5):
    li.append(q**3)

print(f"List 3: {li}")





# Learn data structure called Hash Map
# Hash Set


# wget -O name.zip link
# wget -O Python313.zip https://docs.python.org/3/archives/python-3.13-docs-pdf-a4.zip