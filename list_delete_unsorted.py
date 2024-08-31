# Removing items from a list from backward direction
# Iterating backwards and removing items is a valuable technique as it allows the size of the sequence to be
# changed without causing any issue

# numbers_list_del = [4, 5, 100, 120, 135, 140, 153, 6, 165, 1000, 189, 170, 180, 200, 304, 306, 192, 45, 7]
# numbers_list_del = [4, 5, 1001, 1202, 1352, 1401, 1531, 1651, 1891, 3041, 3061]
numbers_list_del = [4, 5, 1001, 1202, 1352, 1401, 1531, 1651, 1891, 170, 180, 200, 3041, 3061]
# numbers_list_del = [100, 120, 135, 140, 153, 165, 189, 170, 180, 200]
# numbers_list_del = []

min_valid = 100
max_valid = 200

# Approach 1 by iterating the list backwards
# for index in range(len(numbers_list_del) - 1, -1, -1):
#     if numbers_list_del[index] < min_valid or numbers_list_del[index] > max_valid:
#         print(index, numbers_list_del)
#         del numbers_list_del[index]

# Approach 2 by using reversed function to reverse the list and then iterate over it
top_index = len(numbers_list_del) - 1
for index, value in enumerate(reversed(numbers_list_del)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del numbers_list_del[top_index - index]

print(numbers_list_del)