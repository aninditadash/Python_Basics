# Python 3 Sequence types - str, list, tuple, range, bytes and bytearray (sequence is an ordered collection of items)
# Ordered because we can refer to the item using its index value
# Mutable objects - list, dict, set, bytearray
# Can change the value of mutable objects without the object being destroyed and recreated

# Since list is a mutable object, when updating the list, Python does not create a new list
# hence, id value remains the same
directions_list = ["north", "south", "east", "west"]
another_list = directions_list
print(id(directions_list))
print(id(another_list))

directions_list.append("north-east")
print(id(directions_list))
print(id(another_list))

another_list.append("north-west")
print(another_list)
print(directions_list)


# Immutable objects cant be changed, when we update its value a new object is created and attached to the same
# variable. Mutable object update the same object.
# Immutable objects in Python - int, float, bool (sub class of int), str, tuple, frozenset, bytes

# id(object) -> Return the identity or unique id for a specified object. All objects in Python has its own
# unique id. The id is assigned to the object when it is created. If Python destroys and recreates that object
# its id will change. Helps us to know if an object is changed or Python has to create new object.

result = True
another_result = result
print(id(result))
print(id(another_result))
result = False
print(id(result))
print("================================================================================")

# Even though string object is mutated (as Python created a new string object),
# the second variable (another_str_result) assigned to it has the original id
# value and is not changed. Hence, string is an immutable object.
str_result = "Correct"
another_str_result = str_result
print(id(str_result))
print(id(another_str_result))
str_result += "ion"
print(id(str_result))
print(id(another_str_result))
print("================================================================================")