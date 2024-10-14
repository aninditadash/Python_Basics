# Set is an unordered collection with no duplicate entries
# Keys of a dictionary are similar to a set, since Python 3.7, keys in dictionary are ordered.
# No way to access individual items on a set
# Most common operation we can perform on set is to test for membership. (in -> membership operator)

# Union of 2 or more sets, is the set of all items that exist in all the sets ( set1.union(set2) )( set1 | set2 )
# Elements after union appear only once. As per definition of set, items must be unique.
# Intersection of 2 or more sets is the set of items that appear in all sets ( set1.intersection(set2) )( set1 & set2 )
# Subtract one set from another (set1 - set2) ( set1.difference(set2) )
# Set theory also defines symmetric difference, set of items that are in 1 set or another but not in both, it's the
# opposite of intersection of 2 or more sets ( set1.symmetric_difference(set2) ) ( set1 ^ set2 )
# Two sets are disjoint if they do not have any common items

# One set can be a subset of another set, normal comparison operators, <, <=, >, >= to check for subsets.
# Keys of a set must be hashable, similar to a dictionary

# Since sets are unordered, they can't be indexed similar to other sequences like list

farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)
print(f"type(farm_animals) = {type(farm_animals)}")

for animal in farm_animals:
    print(animal)

print("================================================================================")

print("Indexing a sequence")
animals_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animals_list[3]
print(f"animals_list[3] = {goat}")

print("Indexing a set is not possible")
# Below code gives error => TypeError: 'set' object is not subscriptable
# goat = farm_animals[3]

print("================================================================================")

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}

# Even if sets items are same but ordering is different, Python treats them as equal as ordering does not matter
# Lists and tuples will compare equal if they contain same items in the same order
if more_animals == farm_animals:
    print("The sets are equal")
else:
    print("The sets are different")

print(f'set("12345") = {set("12345")}')
print(f'list("12345") = {list("12345")}')
print(f'tuple("12345") = {tuple("12345")}')
set_range_20 = set(range(0, 20, 2))
print(f"set(range(0, 20, 2)) = {set_range_20}")
print(f"3 in set(range(0, 20, 2)) = {3 in set_range_20}")
print(f"10 in set(range(0, 20, 2)) = {10 in set_range_20}")

print("================================================================================")

print("Convert set to list and tuple")
num_set = {1, 3, 4, 10, 14, 0}
print(f"num_set = {num_set}")
num_set_list = list(num_set)
num_set_tuple = tuple(num_set)
print(f"list(num_set) = {num_set_list}")
print(f"tuple(num_set) = {num_set_tuple}")

for item in num_set_list:
    print(f"num_set_list item {item}")

for item in num_set_tuple:
    print(f"num_set_tuple item {item}")

print("================================================================================")

# frozenset() examples
print("frozenset() are immutable sets in Python")
animals = frozenset(["cat", "dog", "lion"])
print("cat" in animals)
print("elephant" in animals)
# animals.append("camel") # Gives AttributeError: 'frozenset' object has no attribute 'append'

# Can pass list or tuples to frozenset
animals_tuple = ("cat", "dog", "horse", "sheep", "goat")
animals_frozen_set = frozenset(animals_tuple)
print(f"animals_frozen_set = {animals_frozen_set}")

animals_list = ["cat", "dog", "horse", "sheep", "goat"]
animals_frozen_set = frozenset(animals_list)
print(f"animals_frozen_set = {animals_frozen_set}")

# Since frozenset objects are immutable, they are used as keys in dictionaries or elements of other sets
student = {
    "name": "Ashmita",
    "age": 7,
    "gender": "female",
    "address": "Cyprus"
}

key = frozenset(student)
print(f"Frozen set of keys in student dictionary = {key}")
