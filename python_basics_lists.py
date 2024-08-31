# Common sequence functions and methods
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))
print(len(even))
print(len(odd))
print("mississipi".count("ip"))
print(even.count(1))
# Fetching index of items from a list causes Python to search the list for the item, which is not efficient
print(even.index(2))

# Fetching index of items from a list using a loop causes Python to search the list for the items,
# which is not efficient especially in case of huge list
directions_list = ["north", "south", "east", "west"]
for direction in directions_list:
    print("Direction {} - {}".format((directions_list.index(direction) + 1), direction))

# enumerate() returns pairs of values of each item in the list (index and item)
# enumerate() returns tuples of (index, value)
for index, direction in enumerate(directions_list):
    print("Direction {} - {}".format(index + 1, direction))

for index, character in enumerate("abcdef"):
    print(index, character)

# List comprehension
directions = [str(i) for i in range(0, len(directions_list))]
print(directions)

# Removing items from list
directions_list.remove("north")
print(directions_list)

# Sorting lists
numbers_list = even + odd
numbers_list.extend([99, 11, 20])
numbers_list.sort(reverse=True)
print(numbers_list)

# Sort vs sorted => sort method sorts the original list, sorted function returns a new list with sorted items
pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(letters)
# Case-insensitive sorting
print(sorted(pangram, key=str.casefold))
new_numbers_list = even + odd
another_new_numbers_list = list(new_numbers_list)
print(new_numbers_list)
print(sorted(new_numbers_list, reverse=True))

# is operator checks if 2 variables are referring to the same list
print(another_new_numbers_list is new_numbers_list)

# == operator is checking if contents of 2 lists are same
print(another_new_numbers_list == new_numbers_list)

# Copying lists
numbers_list_slice = new_numbers_list[:]  # Creating copy of list using slice
numbers_list_copy = new_numbers_list.copy()  # Creating copy of list using copy method

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

# Replacing items in a list using slice
computer_parts = [
    "computer",
    "monitor",
    "keyboard",
    "mouse",
    "mouse mat"
]

# ['computer', 'monitor', 'keyboard', 't', 'r', 'a', 'c', 'k', 'b', 'a', 'l', 'l']
# In below code, the slice is replaced with the contents of the iterable, so string sequence is converted to list
# computer_parts[3:] = "trackball"
# To fix above code, put the string in a list
computer_parts[3:] = ["trackball"]
print(computer_parts)

# Deleting items from a list
computer_parts_del = [
    "computer",
    "monitor",
    "keyboard",
    "mouse",
    "mouse mat"
]
del computer_parts_del[0:2]
print(computer_parts_del)

# Join method of strings with list items
directions_list = ["north", "south", "east", "west"]
print(", ".join(directions_list))
# we can't pass an int value into the join method, it will give error
# directions_list.append(2)
# print(", ".join(directions_list))

# Split method of strings
pangram = "The quick brown fox jumps over the lazy dog"
print(pangram.split())

