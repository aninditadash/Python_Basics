# Dictionary is a collection of values, that are stored using a key.
vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimmy': 'Suzuki Jimmy 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

print(f"vehicles['fiesta'] = {vehicles['fiesta']}")
print(f"vehicles.get('er5') = {vehicles.get('er5')}")

# If the key doesn't exist, .get(<key>) will return None, whereas indexing will crash with a KeyError.
# print(vehicles.get('Fiesta'))   # Returns None
# print(vehicles['Fiesta'])       # Will give KeyError
# get() method is useful if we are not sure if the key exists or not
# Indexing is faster than get() method

print("================================================================================")

# Adding item to a dictionary
print("Adding/updating items in dictionary")

# Dictionaries preserve the insertion order
vehicles['starfigher'] = 'Lockheed F-104'

# Changing values in a dictionary
vehicles['virago'] = 'Yamaha XV535'

# Iterating over a dictionary
for key in vehicles:
    print(key, vehicles[key], sep=" = ")

print("================================================================================")

# Note: In python3, use enumerate() function to iterate over sequences and .items() to iterate over dictionaries
for key, value in vehicles.items():
    print(key, value, sep=" : ")

print("================================================================================")

# Remove items from a dictionary
print("Remove items from dictionary")
vehicles['toy'] = 'Optimus Prime'
print(vehicles['toy'])
del vehicles['toy']

# When removing items from dictionary using index and item does not exist, it will give KeyError
# del vehicles['barbie']
# Python provides pop() method to delete items from dict, if it doesn't exist, we get KeyError
# Can be used to check if particular item is already deleted from the list
# vehicles.pop('barbie')
# Passing None or any other item in above code will not cause the program to crash, and it will be returned.

result = vehicles.pop('barbie', None)
print(result)           # None
result = vehicles.pop('barbie', 'Vehicle not found')
print(result)           # Vehicle not found
fiesta = vehicles.pop('fiesta', 'Vehicle not found')
print(fiesta)

print("================================================================================")

# Using setdefault() method of dictionary
# setdefault() returns the value from the dictionary if key exists, if key doesn't exist, creates a new
# entry for the key and assigns the default value to it and returns the default value
# get() method when passed with default value also performs similar functionality like setdefault() but
# it does not add the key to the dictionary

pantry = {
    "chicken": 500,
    "lemon": 2
}
print("Checking pantry items...")
for key, value in sorted(pantry.items()):
    print(f"{key} = {value}")

chicken_qty = pantry.setdefault("chicken", 0)
print(f"\nchicken - {chicken_qty}")

beans_qty = pantry.setdefault("beans", 0)
print(f"beans - {beans_qty}")
#
ketchup_qty = pantry.get("ketchup", 0)
print(f"ketchup - {ketchup_qty}")

print("\nPantry now contains...")
for key, value in sorted(pantry.items()):
    print(f"{key} = {value}")
