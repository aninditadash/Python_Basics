# Dictionary view objects -> dict.keys(), dict.values(), dict.items()

d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "six"
}

pantry_items = ["chicken", "spam", "egg", "bread", "lemon"]

# New dictionary will be created from the list with list items as keys and default value as 0
new_dict = dict.fromkeys(pantry_items, 0)
print(f"new_dict: {new_dict}")

# Python2 legacy method where it was needed for iterating over dictionary's keys, we get the keys of the dictionary
dict_keys = d.keys()
print(dict_keys)

# We also get the keys of the dictionary in below code
# for item in d:
# Below code is for getting keys explicitly
for item in d.keys():
    print(item)

print("================================================================================")

d2 = {
    7: "new seven",
    10: "ten",
    3: "new three"
}

# Updating one dictionary items from another dictionary
d.update(d2)
for key, value in d.items():
    print(f"{key}: {value}")

print("================================================================================")

# Updating dictionary from other iterables like tuples
d.update(enumerate(pantry_items))
for key, value in d.items():
    print(f"{key}: {value}")

print("================================================================================")

# Dictionary .values() method
dict_values = d.values()
print(dict_values)
d[11] = 'eleven'
print(dict_values)
print("four" in dict_values)
print("eleven" in dict_values)

d_keys = list(d.keys())
d_values = list(d.values())
# Check if value `six` exists in the dictionary and find its key in dictionary if found - using legacy methods
if "six" in d_values:
    index = d_values.index("six")
    key = d_keys[index]
    print(f"{d[key]} was found at index - {index}")

# Check if value `six` exists in the dictionary and find its key in dictionary if found - dict methods
for key, value in d.items():
    if value == "six":
        print(f"{value} was found at index - {key}")

print("================================================================================")

# Copy method of dictionary - does a shallow copy of the dictionary, for complex datastructures e.g.
# if values are lists, then copy() will not work.
dict_1 = {
    1: "one",
    2: "two",
    3: "three",
    6: ["sixty", "sixty-one", "sixty-two"],
    7: ["seventy", "seventy-one", "seventy-two"]
}

dict_2 = dict_1
dict_1[4] = "four"
print(f"dict_1 {dict_1} \ndict_2 {dict_2}")

dict_3 = dict_1.copy()
dict_1[5] = "five"
dict_3[6].append("sixty-three")
print(f"dict_1 {dict_1} \ndict_2 {dict_2} \ndict_3 {dict_3}")


