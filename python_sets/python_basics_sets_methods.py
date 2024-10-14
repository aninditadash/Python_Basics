# Below code looks like it will create an empty set, but actually it creates a dictionary
numbers = {}
print(f"type(numbers) = {type(numbers)}")

# Ways to create an empty set
# numbers_set = {*""}
# numbers_set = {*{}}       => this also works
# Most proper way to create a set is to call the set function
numbers_set = set()
print(f"type(numbers_set) = {type(numbers_set)}")

print("================================================================================")

print("Adding items to a set")
numbers_set.add(1)

# while len(numbers_set) < 5:
#     next_value = int(input("Please enter your next value: "))
#     numbers_set.add(next_value)

print(numbers_set)

print("================================================================================")

data = ["blue", "red", "blue", "green", "red", "black", "blue", "white"]

print("Create a set from the list to remove duplicates")
# Use sorted() to sort the set and preserve the order when running each time, however, the order of the
# colors as appearing in the list is not preserved
unique_data = sorted(set(data))
print(f"unique_data = {unique_data}")

# Create a list of unique colors, keeping the order they appeared.
unique_data_ordered = list(dict.fromkeys(data))
print(f"dict.fromkeys(data) = {dict.fromkeys(data)}")
print(f"unique_data_ordered = {unique_data_ordered}")

print("================================================================================")

print("Delete items from a set")
small_ints = set(range(21))
print(f"small_ints = {small_ints}")

# Clear all the items in the set
small_ints.clear()
print(f"small_ints = {small_ints}")

# Remove an item from the set
small_ints = set(range(21))
small_ints.discard(10)
small_ints.remove(11)
print(f"small_ints = {small_ints}")

# Calling discard() method on the set for an item that does not exist does not throw any error
# Discard is used when we want something to be removed and no need to care if it runs again
small_ints.discard(99)
print(f"small_ints = {small_ints}")

# Calling remove() method on the set for an item that does not exist throws error.
# KeyError: 99
# Can be used to check if an item is already removed from the set.
# Can be used to know if something was already removed, and it's no longer present in the set.
# small_ints.remove(99)

# pop() method deletes an arbitrary item and returns it.
# arbitrary means you can't predict which item will be popped from the set.
print("pop() method of set")


