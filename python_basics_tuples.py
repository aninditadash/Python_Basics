# Tuples are ordered set of data like lists, but they are immutable like strings, i.e. they cant be changed
# once they are created
# 1) Tuples are used to protect the integrity of data.
# 2) Tuples can be unpacked all the time, as entries cant be changed once created, so we always know
#how many values need to be unpacked

tuple1 = "a", "b", "c"
tuple2 = ("d", "e", "f")

print(tuple1, tuple2)
print(tuple1[0])
print(tuple1[1])

# TypeError: 'tuple' object does not support item assignment
# tuple1[2] = "f"

# Convert tuple to list
list1 = list(tuple1)
print(list1)
list1[2] = "f"
print(list1)

# Unpacking a tuple
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

data = 1, 2, 3
x, y, z = data
print(x)
print(y)
print(z)

# Unpacking a list
data_list = [10, 20, 30]
# Below line mutates the list, so unpacking the list values will give error
# ValueError: too many values to unpack (expected 3)
# data_list.append(40)
x1, y1, z1 = data_list
print(x1)
print(y1)
print(z1)

# Nested tuples and lists
nested_lists_sum = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
]
print(len(nested_lists_sum))
for x, y, z in nested_lists_sum:
    print("List item in nested list {} + {} + {} = {}".format(x, y, z, x+y+z))
