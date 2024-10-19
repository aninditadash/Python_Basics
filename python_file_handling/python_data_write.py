data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

plants_filename_print = "../files/flowers_print.txt"
# Approach 1 to write data to a file using print() function
with open(plants_filename_print, "w") as plants:
    for plant in data:
        print(plant, file=plants)

new_list = []
with open(plants_filename_print, "r") as plants:
    for plant in plants:
        new_list.append(plant.rstrip())

print(f"new_list \n{new_list}")

print("================================================================================")

# Below code gives '\n' at the end of each string in the list
with open(plants_filename_print, "r") as plants:
    new_plant_list = plants.readlines()

print(f"new_plant_list \n{new_plant_list}")

print("================================================================================")

plants_filename_write = "../files/flowers_write.txt"
# Approach 2 to write data to a file using write() method
with open(plants_filename_write, "w") as plants:
    for plant in data:
        # Using this method all the data is written in a single line, whereas when using the print(), new line
        # was automatically added  by the print() function
        plants.write(plant)

print("================================================================================")

# print() function calls a special method, that all objects have, before printing the object, which is __str__.
# this method returns a string representation of the object that allows print fn to print objects to the screen.
print(data)
string_representation = data.__str__()
print(type(string_representation))

# Note that text files can only hold text, it means if we try to put numbers into a text file, it will not work.
# But we can put the string representation of the numbers in the file. That means we can print numbers to a
# file, but we can't write them.

# Difference between print and write :
# print will print string representation of any object, it will include separator between multiple arguments
# (default is space, can be changed using sep keyword) and it will print the value of end keyword argument (default is
# newline character).
# write method will only write what you tell it to write, no separators or newline characters unless explicitly
# mentioned and no conversion from object to string is performed. Writing any other type than string will result in
# TypeError, we will have to convert the object to string and send to write() method.

file_name_print = "../files/test_numbers_print.txt"
with open(file_name_print, "w") as test:
    for i in range(10):
        print(i, file=test)

file_name_write = "../files/test_numbers_write.txt"
with open(file_name_write, "w") as test:
    for i in range(10):
        # Below line gives TypeError: write() argument must be str, not int
        # test.write(i)
        # test.write(str(i))
        # To add a new line using write() method
        test.write(str(i) + '\n')
