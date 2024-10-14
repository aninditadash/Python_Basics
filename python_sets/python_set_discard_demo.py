travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
    "razor"
}

# Here we can check the keys in dictionary to find if an item is present
print("2" in travel_mode)   # True
print("3" in travel_mode)   # False

print("Please choose your mode of travel:")
for key, value in travel_mode.items():
    print(f"{key}.{value.capitalize()}")

mode = "-"
while mode not in travel_mode:
    mode = input("> ")

if mode == "2":
    # Travelling by plane, need to remove restricted items and no need to check if item is already removed/discarded
    for item in restricted_items:
        items.discard(item)

# print the final packing list
print("Final packing list: ")
for key, value in enumerate(items):
    print(f"{key} : {value}")
