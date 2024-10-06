# A sequence is an ordered collection of items
# Python 3 Sequence types => str, list, tuple, range, bytes and bytearray
# A sequence is ordered because we can refer to the item using its index value
# dictionary is a mutable data structure in Python
# Mutable data types in Python - list, dict, set, bytearray
# we can change the value of mutable objects without the object being destroyed and recreated

# id(object) -> Return the identity or unique id for a specified object. All objects in Python has its own
# unique id. The id is assigned to the object when it is created. If Python destroys and recreates that object
# its id will change. Helps us to know if an object is changed or Python has to create new object.
# In case of mutable object, id will remain same as it is not re-created.

# Since list is a mutable object, when updating the list, Python does not create a new list
# hence, id value remains the same
directions_list = ["north", "south", "east", "west"]
another_list = directions_list
print(f"id(directions_list) = {id(directions_list)}")
print(f"id(another_list) = {id(another_list)}")

directions_list.append("north-east")
print(f"id(directions_list) = {id(directions_list)}")
print(f"id(another_list) = {id(another_list)}")

another_list.append("north-west")
print(another_list)
print(directions_list)

print("================================================================================")

# Immutable objects cant be change. When we update its value a new object is created and attached to the same
# variable. Mutable object update the same object.
# Immutable objects in Python - int, float, bool (sub class of int), str, tuple, frozenset, bytes

result = True
another_result = result
print(f"id(result) = {id(result)}")
print(f"id(another_result) = {id(another_result)}")
result = False
print(f"id(result) = {id(result)}")

print("================================================================================")

# Even though string object is mutated (as Python created a new string object),
# the second variable (another_str_result) assigned to it has the original id
# value and is not changed. Hence, string is an immutable object.

str_result = "Correct"
another_str_result = str_result
print(f"str_result = {str_result} id(str_result) = {id(str_result)}")
print(f"another_str_result = {another_str_result} | id(another_str_result) = {id(another_str_result)}")
str_result += "ion"
print(f"str_result = {str_result} id(str_result) = {id(str_result)}")
print(f"another_str_result = {another_str_result} | id(another_str_result) = {id(another_str_result)}")
