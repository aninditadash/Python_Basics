# A proper subset must contain a fewer elements than its superset, and a proper superset must contain more
# elements than the subset.

animals = {"Turtle",
           "Horse",
           "Robin",
           "Python",
           "Hedgehog",
           "Cat",
           "Dog",
           "Wren",
           "Aardvark",
           "Pigeon"}

birds = {"Robin", "Wren", "Pigeon"}

print(f"birds is a subset of animals: {birds.issubset(animals)}")
print(f"animals is a superset of birds: {animals.issuperset(birds)}")

print(f"animals is a subset of birds: {animals.issubset(birds)}")
print(f"birds is a superset of animals: {birds.issuperset(animals)}")

print(f"birds <= animals : {birds <= animals}")     # Subset
print(f"birds < animals : {birds < animals}")       # Proper subset

print(f"animals >= birds : {animals >= birds}")     # Superset
print(f"animals > birds : {animals > birds}")       # Proper superset

print("================================================================================")

# subset and superset methods cannot check if a set is a proper subset or superset.
# <, <= , >, >= operators are able to perform this task properly.
print("To check for subset and proper subsets")
garden_birds = {"Pigeon", "Wren", "Robin"}
print(f"garden_birds == birds : {garden_birds == birds}")
print(f"garden_birds <= birds : {garden_birds <= birds}")  # check subset
print(f"garden_birds < birds  : {garden_birds < birds}")  # check proper subset, meaning a subset but not the same set

print("================================================================================")

print("To check if one set is not a subset of another")
more_birds = {'Wren', 'Budgie', 'Shallow'}
print(f"garden_birds >= more_birds : {garden_birds >= more_birds}")

print("================================================================================")

# Set disjoint operation
