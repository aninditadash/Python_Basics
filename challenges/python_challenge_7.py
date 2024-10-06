# Create your own deep copy function without using Python's copy module
def deep_copy(d: dict) -> dict:
    """
    Create a deep copy of the dictionary, also copies `list` and `dict` values.
    :param d: dictionary to copy
    :return: A deep copy of `d`
    """
    deep_copy_dict = {}
    for key, value in d.items():
        deep_copy_dict[key] = value.copy()

    return deep_copy_dict


six_list = ["sixty", "sixty-one", "sixty-two"]
seven_list = ["seventy", "seventy-one", "seventy-two"]
dict_1 = {
    6: six_list,
    7: seven_list
}

dict_deep_copy = deep_copy(dict_1)
dict_1[6].append("sixty-three")
dict_1[7].append("seventy-three")
print(f"dict_1 {dict_1} {id(dict_1[6])}")
print(f"dict_deep_copy {dict_deep_copy} {id(dict_deep_copy[6])}")
