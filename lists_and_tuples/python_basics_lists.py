# Common sequence functions and methods
print("Common list functions and methods")
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(f"min of {even} = {min(even)}")
print(f"max of {even} = {max(even)}")
print(f"min of {odd} = {min(odd)}")
print(f"max of {odd} = {max(odd)}")
print(f"length of {even} = {len(even)}")
print(f"length of {odd} = {len(odd)}")
print("mississipi".count("ip"))
print(f"even.count(1) = {even.count(1)}")
# Fetching index of items from a list causes Python to search the list for the item, which is not efficient
print(f"even.index(2) = {even.index(2)}")

print("================================================================================")

# Fetching index of items from a list using a loop causes Python to search the list for the items,
# which is not efficient especially in case of huge list
directions_list = ["north", "south", "east", "west"]
for direction in directions_list:
    print("Direction {} - {}".format((directions_list.index(direction) + 1), direction))

# enumerate() returns pairs of values of each item in the list (index and item) => returns tuples (index, value)
print("enumerate() in Python on list")
for index, direction in enumerate(directions_list):
    print("Direction {} - {}".format(index + 1, direction))

print("enumerate() in Python on string")
for index, character in enumerate("abcdef"):
    print(index, character)

print("================================================================================")

# List comprehension
print("list comprehensions in Python")
directions = [str(i) for i in range(0, len(directions_list))]
print(directions)

print("================================================================================")

# Removing items from list
print("Removing items from list")
directions_list.remove("north")
print(directions_list)

print("================================================================================")

# Sorting lists
print("Adding items in the list using + or extend() method")
numbers_list = even + odd
numbers_list.extend([99, 11, 20])
print("Sorting lists using sort() method")
numbers_list.sort(reverse=True)
print(numbers_list)

print("================================================================================")

# sort vs sorted => sort method sorts the original list, sorted function returns a new list with sorted items
print("Sorting items using sorted() function")
pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(f"{pangram} after sorting = {letters}")
# Case-insensitive sorting
print(sorted(pangram, key=str.casefold))
new_numbers_list = even + odd
another_new_numbers_list = list(new_numbers_list)
print(f"{new_numbers_list} after sorting (reverse) = {sorted(new_numbers_list, reverse=True)}")

print("================================================================================")

# is operator checks if 2 variables are referring to the same list
print("Check if a list is same as another list using identity operator <is>")
print(f"(another_new_numbers_list is new_numbers_list) = {another_new_numbers_list is new_numbers_list}")

# == operator is checking if contents of 2 lists are same
print(f"(another_new_numbers_list == new_numbers_list) = {another_new_numbers_list == new_numbers_list}")

print("================================================================================")

# Copying lists
print("List copy using copy() method and slice operator")
numbers_list_slice = new_numbers_list[:]  # Creating copy of list using slice
numbers_list_copy = new_numbers_list.copy()  # Creating copy of list using copy method

print("================================================================================")

# Case-insensitive sorting
names = [
    "anne",
    "John",
    "Jane",
    "graham",
    "Michael",
    "Terry"
]
names.sort(key=str.casefold)
print(names)

# Passing a string to sorted function will create a list with the string values in sorted order
numbers_sorted_list = sorted("3456210987")
print(numbers_sorted_list)

# Using list constructor function to create a list from any iterable
print(list("3456210987"))

print("================================================================================")

# Replacing items in a list using slice
print("Replacing items in a list")
computer_parts = [
    "computer",
    "monitor",
    "keyboard",
    "mouse",
    "mouse mat"
]

# In below code, the slice is replaced with the contents of the iterable, so string sequence is converted to list
# computer_parts[3:] = "trackball" => ['computer', 'monitor', 'keyboard', 't', 'r', 'a', 'c', 'k', 'b', 'a', 'l', 'l']
# To fix above code, put the string in a list
computer_parts[3:] = ["trackball"]
print(f"computer_parts = {computer_parts}")

print("================================================================================")

# Deleting items from a list
print("Deleting items in a list")
computer_parts_del = [
    "computer",
    "monitor",
    "keyboard",
    "mouse",
    "mouse mat"
]
del computer_parts_del[0:2]
print(computer_parts_del)

print("================================================================================")

# Join method of strings with list items
print("join() method of string to join list items")
directions_list = ["north", "south", "east", "west"]
print(", ".join(directions_list))
# we can't pass an int value into the join method, it will give error
# directions_list.append(2)
# print(", ".join(directions_list))

print("================================================================================")

# Split method of strings
print("split() method of string to split the string characters")
pangram = "The quick brown fox jumps over the lazy dog"
print(pangram.split())  # Here, separator can't be empty, by default it is => " "

