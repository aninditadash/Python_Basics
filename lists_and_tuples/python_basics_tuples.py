# Tuples are ordered set of data like lists, but they are immutable like strings, i.e. they cant be changed
# once they are created
# 1) Tuples are used to protect the integrity of data.
# 2) Tuples can be unpacked all the time, as entries cant be changed once created, so we always know
# how many values need to be unpacked

tuple1 = "a", "b", "c"
tuple2 = ("d", "e", "f")

print(f"tuple1 = {tuple1}, tuple2 = {tuple2}")
print(f"tuple1[0] = {tuple1[0]}")
print(f"tuple1[1] = {tuple1[1]}")

# TypeError: 'tuple' object does not support item assignment
# tuple1[2] = "f"

print("================================================================================")

# Convert tuple to list
print("Convert tuple to list")
list1 = list(tuple1)
print(f"list(tuple1) = {list(tuple1)}")
list1[2] = "f"
print(f"list1 = {list1}")

print("================================================================================")

# Unpacking a tuple
print("Unpacking a tuple")
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

data = 1, 2, 3
x, y, z = data
print(x)
print(y)
print(z)

print("================================================================================")

# Unpacking a list
print("Unpacking a list")
data_list = [10, 20, 30]
# Below line mutates the list, so unpacking the list values give ValueError: too many values to unpack (expected 3)
# data_list.append(40)
x1, y1, z1 = data_list
print(x1)
print(y1)
print(z1)

print("================================================================================")

# Nested tuples and lists
nested_lists_sum = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
]
print(len(nested_lists_sum))
for x, y, z in nested_lists_sum:
    print("List item in nested list {} + {} + {} = {}".format(x, y, z, x+y+z))

print("================================================================================")

print("Implementation using tuple")
recipes_tuple = {
    "Chicken and chips": [
        ("chicken", 100),
        ("potatoes", 3),
        ("salt", 1),
        ("malt vinegar", 5),
    ],
}

for recipe, ingredients in recipes_tuple.items():
    print(f"To prepare - {recipe}, we need {ingredients}")
    for ingredient, quantity in ingredients:
        print(f"{ingredient} - {quantity}")

print("================================================================================")

print("Implementation using dictionary")
recipes_dict = {
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
}

for recipe, ingredients in recipes_dict.items():
    print(f"To prepare - {recipe}, we need {ingredients}")
    for ingredient, quantity in ingredients.items():
        print(f"{ingredient} - {quantity}")

print("================================================================================")

print("Iterating over a tuple")
ingredients_tuple = ("Chicken", "Potatoes", "Salt", "Vinegar", "Chips", "Spices")
print(f"range_tuple = {ingredients_tuple}")
print(f"Values in {ingredients_tuple}")
for item in ingredients_tuple:
    print(item)

print(f"Keys and values in {ingredients_tuple}")
for key, value in enumerate(ingredients_tuple):
    print(f"{key}: {value}")
