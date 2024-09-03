# When we assign a list as key in dictionary, then the list is not created inside dictionary, instead
# it is created somewhere else in memory and that key holds a reference to that list.
# when we do shallow copy, then the references are copied into the new dictionary
import copy

six_list = ["sixty", "sixty-one", "sixty-two"]
seven_list = ["seventy", "seventy-one", "seventy-two"]
dict_1 = {
    6: six_list,
    7: seven_list
}

dict_shallow_copy_2 = {
    6: six_list,
    7: seven_list
}

dict_shallow_copy_1 = dict_1.copy()
dict_deep_copy_1 = copy.deepcopy(dict_1)
print(f"dict_1 {dict_1} \ndict_shallow_copy_1 {dict_shallow_copy_1}")
print("================================================================================")

dict_shallow_copy_1[6].append("sixty-three")   # Equivalent to six_list.append("sixty-three")
# dict_shallow_copy_2 has reference to same six_list, updating it updates for dict_1, dict_shallow_copy_1
dict_shallow_copy_2[6].append("sixty-four")
print(f"dict_1 {dict_1} \ndict_shallow_copy_1 {dict_shallow_copy_1} \ndict_shallow_copy_2 {dict_shallow_copy_2}")
print("================================================================================")

# If you need deep copy of an object, Python has copy module which provides deepcopy function, will create copies of
# lists, dictionaries and other mutable objects
print(f"dict_1 {dict_1} \ndict_shallow_copy_1 {dict_shallow_copy_1} \ndict_shallow_copy_1 {dict_shallow_copy_1}"
      f"\ndict_deep_copy_1 {dict_deep_copy_1}")
print("================================================================================")

print(f"id of dict_1 six_list - {id(dict_1[6])}")
print(f"id of dict_shallow_copy_1 six_list - {id(dict_shallow_copy_1[6])}")
print(f"id of dict_shallow_copy_2 six_list - {id(dict_shallow_copy_2[6])}")
print(f"id of dict_deep_copy_1 six_list - {id(dict_deep_copy_1[6])}")
