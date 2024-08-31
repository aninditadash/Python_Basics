# Safely deleting items from a list while iterating over it and delete a particular item based on condition
# numbers_list_del = [4, 5, 100, 120, 135, 140, 153, 165, 189, 170, 180, 200, 304, 306]
# numbers_list_del = [4, 5, 100, 120, 135, 140, 153, 165, 189, 170, 180, 200]
# numbers_list_del = [100, 120, 135, 140, 153, 165, 189, 170, 180, 200, 304, 306]
# numbers_list_del = [100, 120, 135, 140, 153, 165, 189, 170, 180, 200]
# numbers_list_del = [4, 5, 1001, 1202, 1352, 1401, 1531, 1651, 1891, 170, 180, 200, 3041, 3061]
# numbers_list_del = [4, 5, 1001, 1202, 1352, 1401, 1531, 1651, 1891, 3041, 3061]
numbers_list_del = []

min_valid = 100
max_valid = 200
# Delete the items from above list outside the range of min_valid - max_valid

# Approach 1 for sorted list
numbers_list_del_sorted = sorted(numbers_list_del)
print(numbers_list_del_sorted)

# process the low values in the list
stopIndex = 0
for index, value in enumerate(numbers_list_del_sorted):
    if value >= min_valid:
        stopIndex = index
        break
del numbers_list_del_sorted[:stopIndex]
print(numbers_list_del_sorted)

# process the high values in the list
# Approach 1 for processing high values in the list by iterating backwards and erasing the data
startIndex = 0
for index in range(len(numbers_list_del_sorted)-1, -1, -1):
    if numbers_list_del_sorted[index] <= max_valid:
        startIndex = index + 1
        break
del numbers_list_del_sorted[startIndex:]
print(numbers_list_del_sorted)

# Approach 2 for processing high values in the list by iterating forward and erasing the data
# startIndex = 0
# for index, value in enumerate(numbers_list_del_sorted):
#     if value > max_valid:
#         startIndex = index
#         break
# del numbers_list_del_sorted[startIndex:]
# print(numbers_list_del_sorted)
